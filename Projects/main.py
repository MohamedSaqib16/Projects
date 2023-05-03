import subprocess
import os
import socket
from Features.Webrowser import YoutubeSearch, google_search
from Features.Instagram import MsgInstagram,Instagram
from Brain.Brain import ReplyBrain
from Scripts.Listen import Listen
print(">> Starting Rapheal : Wait For Some Seconds.")
from TaskExe import MainTaskExecution
from Features.GreetMe import GreetMe
from Features.Battery import Battery
print(">> Started The Rapheal : Wait For Few Seconds More")
from Modules.AppsLocaion import Appopener,Rainmeter
from Features.SystemControl import Screenshot
from Scripts.Talk import Talk
from Scripts.Speak import Speak


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

        elif "sleep" in Data:
            Speak("bye sir have a good day")
            subprocess.call("TASKKILL /F /IM Rainmeter.exe", shell=True)
            quit()

        elif "screenshot" in Data:
            Screenshot()


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

        elif "youtube search" in Data:
            query = Data.replace("youtube search ", "")
            Speak(f"searching for {query}")
            YoutubeSearch(query)

        elif "google search" in Data:
            query = Data.replace("google search ", "")
            Speak(f"searching for {query}")
            google_search(query)

        elif "instagram messages" in Data:
            Speak("checking Instagram Messages")
            Speak("please wait....")
            MsgInstagram()

        elif "instagram" in Data:
            Speak("launching instagram")
            Instagram()


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

MainExecution()


if is_connected():
    Speak("Internet connection sucessful")
    Speak("Starting Engine")
    Speak("Collecting required resources")
    Speak("initializing")
    os.startfile(Rainmeter)

else:
    print("No internet connection")
    Talk("Internet Connection Failed")
    Talk("try again later")
    quit()


