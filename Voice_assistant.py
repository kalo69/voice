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


#nachalo
def speak(text):
    engine.say(text)
    engine.runAndWait()

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()

#pozdravqva shefcheto spored chasa
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        playsound("wav/zdr.wav")
    elif hour>=12 and hour<18:
        speak("Добър Следобяд")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
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

playsound("wav/zarejdam.wav")
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
            playsound("wav/chal.wav")
            print('your personal assistant G-one is shutting down,Good bye')
            break

        
        if "много съм умен" in statement or "айкюто върти" in statement:
            playsound("wav/iq.wav")
            print("da taka e mnogo ste umen,  sir")
            break



            #wikipediata
        if 'уикипедия' in statement:
            playsound("wav/tursq wikipedia.wav")
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            playsound("wav/spored-wikipedia.wav")
            print(results)
            speak(results)

            #youtube
        elif 'отвори ютуб' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            playsound("wav/yt.wav")
            time.sleep(5)

        elif 'пусни ми новините' in statement:
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=RXPGslO_fxo")
            playsound("wav/novinite.wav")
            time.sleep(5)

        #google
        elif 'Отвори google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            playsound("wav/google.wav")
            time.sleep(5)

        #gmail
        elif 'отвори gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            playsound("wav/gmail.wav")
            time.sleep(5)
        #vreme (meteo)
        elif "какво е времето" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            playsound("wav/grada.wav")
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
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
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

        elif 'Време' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        #koi si ti
        elif 'who are you' in statement or 'what can you do' in statement:
            speak('Az sum bashtati')

        #koi ta naprai ma
        elif "Кой те е направил" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Kaloyan")
            print("I was built by Kaloyan")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'news' in statement:
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
            playsound("wav/miksa.wav")
            time.sleep(2000)
        
        #pitame
        elif 'питай' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        #log off
        elif "заминавай" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

        elif "пусни ми музика" in statement or "пусни ми музичка" in statement or "музика" in statement:
                playsound('kondo.wav')
                
time.sleep(3)

