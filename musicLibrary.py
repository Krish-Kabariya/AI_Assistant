import urllib.parse

music = {
    "daku": "https://music.youtube.com/watch?v=H2g1Q0iomMQ&si=gvFqMGbaiIMVYgMq",
    "295": "https://music.youtube.com/watch?v=RTwknWM68oE&si=tOvl_iZTa2yuXKRf",
    "mockingbird": "https://music.youtube.com/watch?v=9kznlAwE-8o&si=wqtoy1nrXisxnlqQ",
    "withoutme": "https://music.youtube.com/watch?v=tqxRidAWER8&si=awGAaJYNeItfo-Wk",
    "ektarfa" : "https://music.youtube.com/watch?v=4IAnSQKUC5Q&si=VLRebPm56I09wPKJ",
    
}

# Example: wrap in a function or use 'if' at the top level
def play_song(c, musicLibrary, speak, webbrowser):
    if c.lower().startswith("play"):
        try:
            song = c.lower().split("play", 1)[1].strip()  # get full song name
            if song in musicLibrary.music:
                webbrowser.open(musicLibrary.music[song])
                speak(f"Playing {song} from your library.")
            else:
                # If not found in library, search on YouTube
                speak(f"{song} is not in your library. Searching on YouTube.")
                query = urllib.parse.quote(song)
                url = f"https://www.youtube.com/results?search_query={query}"
                webbrowser.open(url)
        except Exception as e:
            speak("Sorry, I couldn't play the song.")
            print(f"Error: {e}")
