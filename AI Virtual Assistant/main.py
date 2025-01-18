import speech_recognition as sr 
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os

# pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "f7cec633b1c84d1c873586fa32a6f406"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def aiProcess(command):
    client = OpenAI("api_key")

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages =[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses"},
        {"role": "user", "content": command}
    ]
)
    
    return completion.choices[0].message

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/everything?q=tesla&from=2024-12-13&sortBy=publishedAt&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()

            # Extract the articles
            articles = data.get('articles', [])

            # Print the headlines
            for article in articles:
                speak(article['title'])
    else:
        # Let OpenAI handle the requests
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Senti...")
    while True:
        # Listen for th ewake word "Jarvis"
        # Obtain audio from the microphone

        r = sr.Recognizer()

        # Recognize speech using Sphinx
        print("Recognizing..")
        try:
            with sr.Microphone() as source:
                print("Listening..")
                audio = r.listen(source, timeout=2, phrase_time_limit = 1)

            word = r.recognize_google(audio)
            if(word.lower() == "senti"):
                speak("Ya")

                # Listen for command
                with sr.Microphone() as source:
                    print("Senti Active..")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                processCommand(command)

        except sr.RequestError as e:
            print("Error; {0}".format(e))

        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")

        except sr.WaitTimeoutError:
            print("No speech detected within the time limit. Please try again.")
            continue

