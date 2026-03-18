import speech_recognition as sr
import pyttsx3
import os

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query.lower()
    except Exception:
        print("Say that again please...")
        return "None"

def assistant():
    command = listen().lower()
    
    if "hello" in command:
        speak("Welcome")
        
    elif "shut" in command:
        speak("Shutting down. Goodbye!")
        #exit()
        os.system("shutdown /s /t 1")

while True:
    assistant()