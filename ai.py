import pyttsx3
from pyttsx3.drivers import sapi5
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
from joke.jokes import *
from joke.quotes import  *
import winsound
from batteryNotification import batteryNotifier

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good Morning sir")
        speak("Good Morning sir")
    elif hour >= 12 and hour < 18:
        print("Good Afternoon sir")
        speak("Good Afternoon sir")
    else:
        print("Good evening sir")
        speak("Good evening sir")
    speak("how may i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...\n")
        query = r.recognize_google(audio, language="en-in")
        print(f"{query}\n")
    
    except Exception as e:
        print("Can you say that again please...")
        return "None"

    return query

if __name__ == "__main__":

    wishMe()
    
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('Searching...')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            print(f"Sir the time is {strTime}")
            speak(f"sir the time is {strTime}")
            
        elif 'play music' in query:
            music_dir = "F:\songs"
            songs = os.listdir(music_dir)
            print(f"Playing {songs}")
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif 'search' in query:
            google_query = query.replace("search", "")
            webbrowser.open(f"https://www.google.com/search?q={google_query}")
            print("Opening google")
        
        
        elif 'battery' or 'remaining battery' in query:
            batteryNotifier()
        
            
