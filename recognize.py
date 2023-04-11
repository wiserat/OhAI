import speech_recognition as sr
from ohbot import *


def recognize(name, lang):
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 30604.142478090707
    recognizer.dynamic_energy_threshold = True
    with sr.Microphone() as mic:
        audio = recognizer.listen(mic)
        text = recognizer.recognize_google(audio, language=lang)
        text = text.lower()
    
    if text.startswith(name.lower()):
        text = text.replace(f"{name.lower()} ", '')
        print(text)
        return text
