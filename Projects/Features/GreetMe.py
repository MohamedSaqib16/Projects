import datetime
import os
import time
import AppOpener
import pyautogui

from Modules.AppsLocaion import Rainmeter
from Scripts.Speak import Speak

def GreetMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        Speak("Good Morning!")

    elif hour>=12 and hour<18:
        Speak("Good Afternoon!")

    else:
        Speak("Good Evening!")



