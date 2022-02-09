import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
import pyaudio

#assign engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#create functions as you go
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour < 12:
        speak("Good Morning Sir!")

    elif hour >=12 and hour <18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")
    asname = ("Mark 1")
    speak("How can i help you")
    speak(asname)




def username():
    speak("What should I call you sir!")
    usname = takeCommand()
    speak("Welcome")
    speak(usname)
    columns = shutil.get_terminal_size().columns
    print("      ######################################".center(columns))
    print("Welcome Mr.", usname.center(columns))
    print("      ######################################".center(columns))
    speak("How Can i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)


        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            print(e)
            speak("unable to recognize")
            return "None"

    return query



if __name__ == '__main__':
    clear = lambda: os.system('cls')

#clear any tasks before
clear()
greet()
username()


while True:
    query = takeCommand().lower()
    if query ==0:
        continue

    if 'wikipedia' in query:
        speak("searching Wikipedia")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query, sentences = 3)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        speak("Here you go\n")
        webbrowser.open_new_tab("youtube.com")

    elif 'bye' in query:
        speak("Goodbye")
        exit()

    elif 'open spotify' in query:
        speak("Opening Spotify")
        os.startfile('C:\\Users\\shaik\\AppData\\Roaming\\Spotify\\Spotify.exe')

    else:
        speak("Not available")

