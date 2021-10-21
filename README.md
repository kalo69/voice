<h1>How to install (currently)</h1>
<br>
<h2>pip install these:</h3>

<div style="text-align:center">
<li>pyttsx3</li>

<li>SpeechRecognition</li>

<li>wikipedia</li>

<li>win10toast (works for windows and windows only!!!)</li>

<li>gtts</li>

<li>playsound</li>

<li>wolframalpha</li>

you will also need pyaudio and pyspeech

note: if you have problem with pyaudio (most likely) install an older version
</div>

<h1 style="text-align:center">------BG------</h1>
<h2>if you want your tts to speak in bulgarian do this:</h2>

install TTS.Voices.MegaPack.exe
from the installer select VE_Bulgarian_Daria_22kHz

then run this code in a test.py file (i have included it in the gievn files)

####################################################

import pyttsx3

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def getvoices():
    voices = engine.getProperty('voices')
    print(voices[0].id)
    
    
getvoices()
####################################################

then debug test.py with ctrl + f5

the termial should say something like:
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\YOURTTSVOICE

after that change the voice id -- (print(voices[<span style="font-style:bold">changeme</span>].id) --  until you see somethng like this:
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices
Tokens\VE_Bulgarian_Daria_22kHz

remember the voice id and put it in my code

<h1>Now you are ready!</h1>

note: if you have a problem with the installation feel free to contact me!
