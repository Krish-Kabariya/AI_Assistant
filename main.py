import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os
import urllib.parse

recognizer = sr.Recognizer()
engine = pyttsx3.init()
api_key_1 = "my api key"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    pygame.mixer.init()
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def aiProcess(command):
    client = OpenAI(
        api_key="api key",
    )
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Arya skilled in general tasks like Alexa and Google Cloud. Give short responses please."},
            {"role": "user", "content": command}
        ]
    )
    return completion.choices[0].message.content

def processCommand(c):
    c = c.lower().strip()
    
    if "open google" in c:
        webbrowser.open("https://google.com")
        speak("Opening Google.")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
        speak("Opening Facebook.")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube.")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
        speak("Opening LinkedIn.")
    elif c.startswith("play"):
        try:
            song = c.replace("play", "").strip()
            if song in musicLibrary.music:
                webbrowser.open(musicLibrary.music[song])
                speak(f"Playing {song} from your library.")
            else:
                speak(f"{song} not found in library. Searching on YouTube.")
                query = urllib.parse.quote(song)
                webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        except Exception as e:
            speak("There was an error playing that song.")
            print(f"Error: {e}")
    elif "news" in c:
        response = requests.get(
            f"https://newsapi.org/v2/everything?q=india&sortBy=publishedAt&pageSize=5&language=en&apiKey={api_key_1}"
        )
        print("News API status:", response.status_code)
        print("News API response:", response.text)

        if response.status_code == 200:
            articles = response.json().get('articles', [])
            if not articles:
                speak("Sorry, I couldn't find any news at the moment.")
            else:
                speak("Here are the latest news headlines.")
                for article in articles[:5]:
                    speak(article.get('title', 'No title available'))
        else:
            speak("Sorry, I couldn't fetch the news.")
    else:
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Hi! This is Arya, your personal assistant. How can I help you?")
    while True:
        print("Listening for wake word...")
        try:
            with sr.Microphone() as source:
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=1)
            word = recognizer.recognize_google(audio)
            if word.lower() == "arya":
                speak("Yes?")
                with sr.Microphone() as source:
                    print("Listening for command...")
                    audio = recognizer.listen(source)
                try:
                    command = recognizer.recognize_google(audio)
                    print(f"You said: {command}")
                    processCommand(command)
                except sr.UnknownValueError:
                    speak("Sorry, I didn't understand that.")
        except sr.WaitTimeoutError:
            pass
        except Exception as e:
            print(f"Error: {e}")
