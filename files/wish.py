# from speak import *
import datetime


import pyttsx3
from pyttsx3.drivers import sapi5


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
    print("how may i help you")