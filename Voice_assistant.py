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

l = ['https://www.youtube.com/watch?v=iggmiF7DNoM&list=RDiggmiF7DNoM&start_radio=1', 'https://www.youtube.com/watch?v=ZzVzYVk6Euo&list=RDZzVzYVk6Euo&start_radio=1', 'https://www.youtube.com/watch?v=vX9msKu75qs&list=RDvX9msKu75qs&start_radio=1']
#nachalo
def speak(text):
    engine.say(text)
    engine.runAndWait()

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
        speak("Добър Следобяд, сър С какво мога да ви помогна?")
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
            playsound("wav/povtorite.wav")
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
            webbrowser.open_new_tab((random.choice(l)))
           

            #wikipediata
        if 'потърси в уикипедия' in statement:
            speak("търся в уикипедия")
            statement =statement.replace("уикипедия", "Уикипедия")
            results = wikipedia.summary(statement, sentences=3)
            speak("според уикипедия")
            print(results)
            speak(results)

            #youtube
        elif 'отвори ютуб' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("отварям ютуб,сър")
            time.sleep(5)

        elif 'пусни ми новините' in statement:
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=RXPGslO_fxo")
            speak("отварям Ви новините, сър")
            time.sleep(5)

        #google
        elif 'Отвори google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("отварям гугъл, сър")
            time.sleep(5)

        #gmail
        elif 'отвори gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            playsound("wav/gmail.wav")
            time.sleep(5)
        #vreme (meteo)
        #elif "какво е времето" in statement or "кажи ми времето" in statement or "времето" in statement or "време":
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("Каков е името на града ви, сър ?")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Температурата в Келвин е " +
                      str(current_temperature) +
                      "\n Влажността в проценти е " +
                      str(current_humidiy) +
                      "\n Описание  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")


        #vreme

        elif 'час' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"часът е {strTime}")
        #koi si ti
        elif 'who are you' in statement or 'what can you do' in statement:
            speak('Аз съм Кондьо')

        #koi ta naprai ma
        elif "кой те е направил" in statement or "кой те е създал" in statement or "who discovered you" in statement:
            speak("майка ти хаха")
            print("I was built by Kaloyan")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'новини' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        #camera (nqmame skripta)
       # elif "camera" in statement or "take a photo" in statement:
       #     ec.capture(0,"robo camera","img.jpg")


        #tursene v neta
        elif 'потърси' in statement or "търси" in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(20)
        
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
            answer = next(res.results).text
            speak(answer)
            print(answer)

        #log off
        elif "заминавай" in statement or "sign out" in statement:
            speak("Добре, вашият компютър ще излезе след 10 секунди, уверете се, че излизате от всички приложения ")
            subprocess.call(["shutdown", "/l"])

        elif "пусни ми музика" in statement or "пусни ми музичка" in statement or "музика" in statement:
                playsound('kondo.wav')
                
time.sleep(3)

