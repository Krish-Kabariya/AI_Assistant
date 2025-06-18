# Arya - Voice Controlled Virtual Assistant

Arya is a Python-based voice assistant that performs tasks like opening websites,
fetching news, answering queries using OpenAI, and playing songs from a local music 
library or YouTube. It combines speech recognition, AI interaction, and music playback 
into an interactive experience.

## Features

- 🎤 Voice-activated interaction ("Arya" as wake word)
- 🌐 Opens websites like Google, YouTube, Facebook, LinkedIn
- 📰 Fetches recent news using NewsAPI
- 🎵 Plays music from a pre-defined library or searches on YouTube
- 🤖 Answers general questions via OpenAI's GPT-3.5 Turbo

## Files

- `main.py` - The main script that listens for commands and controls all functionality.
- `client.py` - Simple standalone demo of how Arya communicates with OpenAI.
- `musicLibrary.py` - Contains a dictionary of pre-defined songs and URLs.
- `musicLibrary.cpython-313.pyc` - Compiled version of `musicLibrary.py` (not needed for manual edits).

## Requirements

Install the required packages using pip:

```bash
pip install openai speechrecognition pyttsx3 pygame gTTS requests
