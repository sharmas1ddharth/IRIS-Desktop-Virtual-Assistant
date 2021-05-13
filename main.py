import wikipedia
import webbrowser
import os
import smtplib
import random
import winsound
import datetime
# from batteryNotification import batteryNotifier
from files.wish import wishMe, speak
from files.takeCommand import takeCommand


def takeQuery():
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

        # elif 'battery' or 'remaining battery' in query:
        #     batteryNotifier()


if __name__ == "__main__":
    takeQuery()
