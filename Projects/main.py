from Brain.Brain import ReplyBrain
from Scripts.Listen import Listen
print(">> Starting Rapheal : Wait For Some Seconds.")
from Scripts.Speak import Speak
from Features.Clap import Tester
print(">> Started The Rapheal : Wait For Few Seconds More")
from TaskExe import MainTaskExecution
from Features.GreetMe import GreetMe
from Features.Battery import Battery

def MainExecution():
    GreetMe()
    Speak("I'm Rapheal, I'm Ready To Assist You Sir.")

    while True:

        Data = Listen()
        Data = str(Data).replace(".","")

        ValueReturn = MainTaskExecution(Data)
        if ValueReturn==True:
            pass

        elif len(Data)<3:
            pass

        elif "battery" in Data:
            Battery()

        elif "turn on the tv" in Data:# Specific COmmand
            Speak("Ok..Turning On The Android TV")

        else:
            Reply = ReplyBrain(Data)
            Speak(Reply)

def ClapDetect():

    query = Tester()
    if "True-Mic" in query:
        print("")
        MainExecution()
    else:
        pass

ClapDetect()