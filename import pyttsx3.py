import pyttsx3

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def getvoices():
    voices = engine.getProperty('voices')
    print(voices[9].id)

getvoices()