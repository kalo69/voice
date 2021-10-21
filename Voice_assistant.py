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



        if "чао" in statement or "млъкни" in statement or "спри се" in statement:
            speak("Довиждане, сър")
            print('your personal assistant G-one is shutting down,Good bye')
            break

        
        if "много съм умен" in statement or "айкюто върти" in statement:
            speak("Да така е")
            print("da taka e mnogo ste umen,  sir")
            

        if "нещо" in statement:
            webbrowser.open_new_tab((random.choice(music)))
           

            #wikipediata
        if 'потърси в уикипедия' in statement:
            speak("търся в уикипедия")
            statement =statement.replace("потърси в уикипедия","")
            results = wikipedia.summary(statement, sentences=3)
            speak("според уикипедия")
            print(results)
            speak(results)
            continue

        elif 'софия' in statement:
            playsound('giga.wav')    

        elif 'пусни' in statement:
            song = statement.replace('пусни', '')
            talk('пускам ' + song)
            pywhatkit.playonyt(song)
            time.sleep(5)
            #youtube

        elif 'кажи че' in statement:
            kaji = statement.replace('кажи че', '')
            da = 'да, така е, Янко е гей'
            print(da)
            speak(da)

        elif 'кой е' in statement:
            person = statement.replace('кой е', '')
            info = wikipedia.summary(person, 1)
            print(info)
            speak(info)

        elif 'отвори ютуб' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("отварям ютуб,сър")
            time.sleep(5)

        elif 'пусни ми новините' in statement:
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=RXPGslO_fxo")
            speak("отварям Ви новините, сър")
            time.sleep(5)

        #google
        elif 'Отвори google' in statement or 'отвори google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("отварям гугъл, сър")
            time.sleep(5)

        #gmail
        elif 'отвори gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("отварям джимей, сър")
            time.sleep(5)

        elif 'здравей' in statement or 'здрасти' in statement or 'здр' in statement or 'добро утро' in statement or'добър ден' in statement or 'добър вечер' in statement:
            speak("Вече ви поздравих, сър")


        elif 'как си' in statement or 'как се чувстваш' in statement or 'такси' in statement:
            speak(random.choice(how)) 
            speak("A Вие как сте, сър")

        elif 'искаш ли' in statement or 'а искаш ли' in statement:
            speak("даааа")
            speak("татенцееее")
            speak("оххххххх")

        elif 'знаеш ли' in statement or 'знаеш' in statement:
            speak("да знам")
            speak("аз знам всичко")

        elif 'трябва' in statement or 'а трябва' in statement:
            speak("да така е")
            speak("трябва")

        elif 'не' in statement:
            speak("Добре")


        elif random.choice(howo) in statement:
            speak('Радвам се да го чуя')
            speak('С какво мога да Ви помогна, сър ?')

        elif "кой те е направил" in statement or "кой те е създал" in statement or "кой баща те е направил" in statement or 'кой баща те направил' in statement:
            speak("майка ти хаха")
            print("I was built by Kaloyan")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'новини' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        #tursene v neta
        elif 'потърси' in statement or "търси" in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
        
        elif 'пускай микса' in statement or "кондио микс" in statement or "микс" in statement:
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=Kih7h64RJF8&list=RDKih7h64RJF8&start_radio=1")
            speak("пускам микса шефеееее ")
            time.sleep(5)
        
        #pitame
        elif 'питай' in statement:
            speak('Мога да отговоря на изчислителни и географски въпроси и какъв въпрос искате да зададете сега')
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(results).text
            speak(answer)
            print(answer)

        #log off
        elif "заминавай" in statement or "sign out" in statement:
            speak("Добре, вашият компютър ще излезе след 10 секунди, уверете се, че излизате от всички приложения ")
            subprocess.call(["shutdown", "/l"])

        elif "пусни ми музика" in statement or "пусни ми музичка" in statement or "музика" in statement:
             webbrowser.open_new_tab((random.choice(music)))


        elif 'колко е часът' in statement or 'колко е часа' in statement or 'час' in statement or 'часът' in statement or 'часа' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"часът е {strTime}")

                
                
time.sleep(3)

