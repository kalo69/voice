import datetime
import json
import os
import subprocess
import time
import webbrowser
import pyttsx3
import requests
import speech_recognition as sr
import wikipedia
from win10toast import ToastNotifier
import gtts
from playsound import playsound
#from ecapture import ecapture as ec
import wolframalpha
import random
import pywhatkit
from config import music
from config import how
from config import howo
from config import kondio
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

#nachalo
def speak(text):
    engine.say(text)
    engine.runAndWait()



def talk(text):
    engine.say(text)
    engine.runAndWait()


listener = sr.Recognizer()
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[9].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()




#pozdravqva shefcheto spored chasa
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
       speak("Добро утро, сър. С какво мога да ви помогна?")
    elif hour>=12 and hour<18:
        speak("Добър ден, сър С какво мога да ви помогна?")
        print("Hello,Good Afternoon")
    else:
        speak("Добър вечер, сър  С какво мога да ви помогна?")
        print("Hello,Good Evening")

#razpoznavane

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='bg-bg')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Може ли да повторите, сър")
            return "None"
        return statement

speak("Зареждам...")
print("zarejdam...")
time.sleep(1)

wishMe()




#main

if __name__=='__main__':
    

    while True:
        speak("")
        statement = takeCommand().lower()
        if statement==0:
            continue
            #kazva chao na shefcheto



        if "здравей" in statement:
            speak("Здравей, Петьо)


time.sleep(3)

