import subprocess
import os
import socket
from Features.WhatsApp import MsgInstagram
from Brain.Brain import ReplyBrain
from Scripts.Listen import Listen
print(">> Starting Rapheal : Wait For Some Seconds.")
from Scripts.Speak import Speak
print(">> Started The Rapheal : Wait For Few Seconds More")
from TaskExe import MainTaskExecution
from Features.GreetMe import GreetMe
from Features.Battery import Battery
from Modules.AppsLocaion import Appopener,Rainmeter
from Features.SystemControl import Brightness
from Scripts.Talk import Talk


def MainExecution():
    GreetMe()
    Speak("I'm Rapheal, I'm Ready To Assist You .")

    while True:

        Data = Listen()
        Data = str(Data).replace(".", "")

        ValueReturn = MainTaskExecution(Data)
        if ValueReturn == True:
            pass

        elif len(Data) < 3:
            pass

        elif "battery" in Data:
            Battery()

        elif "turn on the tv" in Data:  # Specific COmmand
            Speak("Ok..Turning On The Android TV")

        elif "sleep" in Data:
            Speak("bye sir have a good day")
            subprocess.call("TASKKILL /F /IM Rainmeter.exe", shell=True)
            quit()

        elif "brightness" in Data:
            Data.replace("brightness to","")
            Brightness(Data)

        elif "shutdown" in Data:
            Reply = Listen()
            Speak("sir Do you want to shutdown the system")
            if "yes" in Reply:
                Speak("Shutting Down System")
                Speak("bye sir have a good day")
                subprocess.call("TASKKILL /F /IM Rainmeter.exe", shell=True)
                os.system("sudo shutdown -h now")

        elif "restart" in Data:
            reply = Listen()
            Speak("sir Do you want to shutdown the system")
            if "yes" in reply:
                Speak("Restarting Down System")
                Speak("bye sir have a good day")
                subprocess.call("TASKKILL /F /IM Rainmeter.exe", shell=True)
            os.system("sudo shutdown -r now")

        elif "open" in Data:
            Appopener(Data)

        elif "close" in Data:
            Appopener(Data)

        elif "instagram" in Data:
            MsgInstagram()

        else:
            Reply = ReplyBrain(Data)
            Speak(Reply)

def is_connected():

    REMOTE_SERVER = "www.google.com"

    try:
        host = socket.gethostbyname(REMOTE_SERVER)
        s = socket.create_connection((host, 80), 2)
        return True
    except:
        pass
    return False

if is_connected():
    Speak("Internet connection succesfull")
    Speak("Starting Engine")
    Speak("Collecting required resources")
    Speak("initializing")
    os.startfile(Rainmeter)
    MainExecution()
else:
    print("No internet connection")
    Talk("Internet Connection Failed")
    Talk("try again later")
    quit()
is_connected()


