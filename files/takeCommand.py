import speech_recognition as sr

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
