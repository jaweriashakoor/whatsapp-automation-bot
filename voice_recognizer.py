import speech_recognition as sr
import pyttsx3
import sounddevice as sd
import numpy as np

engine = pyttsx3.init()

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def listen(duration=4, fs=44100):
    print("Listening...")

    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()

    recording = recording.flatten()  # Fix: flatten 2D array to 1D

    r = sr.Recognizer()
    audio_data = sr.AudioData(recording.tobytes(), fs, 2)  # 2 bytes per sample

    try:
        command = r.recognize_google(audio_data)
        return command.lower()
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return ""

if __name__ == "__main__":
    speak("Say something!")
    result = listen()
    if result:
        speak("You said: " + result)
    else:
        speak("I didn't catch that.")