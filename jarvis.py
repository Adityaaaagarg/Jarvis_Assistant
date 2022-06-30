import speech_recognition as sr
import os
import pyttsx3
import time
import webbrowser
from pywinauto import application
import pyjokes
from scripts import *
import wikipedia

def speak(aud):
    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices') 
    engine.setProperty('voice',voices[0].id)
    engine.say(aud)
    engine.runAndWait()


def wish():
    tym=time.localtime()
    if tym.tm_hour<12:
        speak("Good Morning")

    elif tym.tm_hour>=12 and tym.tm_hour<17:
           speak("Good Afternoon")

    else :
        speak("Good Evening")       
    
    speak("I am Jarvis. How may i help you")
    
    
def take_command():
  r=sr.Recognizer()
  with sr.Microphone() as source:
       audio=r.listen(source)

       try:
           text=r.recognize(audio)
           print(text)
           return text
       except:
       
           return "None"




if __name__=="__main__":
    
    # wish()
 while(1):
    print("Listening...")
    command=take_command().lower()
    
    if command=='':
        speak("Sorry,I didn't get it.Please repeat")

    elif 'wikipedia' in command:
        speak("According to wikipedia")
        cmd = cmd.replace('wikipedia',"")
        result = wikipedia.summary(cmd,sentences=10)
        speak("According to wikipedia")
        speak(result)  

    elif "youtube" in command:
      speak("Opening You tube")
      webbrowser.open("youtube.com")

    elif "whatsapp" in command:
        speak("Opening Whatsapp")
        webbrowser.open("whatsapp.com")  

    elif "google" in command:
        speak("Opening Google")
        webbrowser.open("google.com")    

    elif "play" in command:
        speak("Playing Songs")
        music="D:\songs"
        song=os.listdir(music)
        for x in range(0,len(song)):
          os.startfile(os.path.join(music,song[x]))

    elif 'joke' in cmd:
        speak('Searching for a joke')
        speak('i get it')
        speak(pyjokes.get_joke())
        speak('hahahahahahah')      

    elif "show" in command:
        speak("Opening Pics")
        pic="D:\Family Pics"
        num=os.listdir(pic)
        for x in range(0,len(num)):
            os.startfile(os.path.join(pic,num[x])) 
            a=0
            while 1:   
               cmd=take_command().lower()
               if "stop"==cmd:
                   a=1
                   break
               elif "next"==cmd:
                   speak("Next")
                   break
               elif "previous"==cmd:
                   speak("Previous")
                   x=x-2   
                   break
            if a:
                os.close()
                break
   
    elif "notepad" in command:
        speak("Opening Notepad")
        app=application.Application()
        app.start("Notepad.exe")

    elif "bye"==command:
        speak("Bye,Take care")
        break    

    else:
        speak("Sorry,I didn't get it.Please repeat")  