from pyfirmata import Arduino,util
from pyfirmata import OUTPUT
from Scripts.Speak import Speak
from Scripts.Listen import Listen

query = Listen()

board = Arduino('COM4')
board.digital[10].mode = OUTPUT
board.digital[11].mode = OUTPUT
board.digital[12].mode = OUTPUT
board.digital[13].mode = OUTPUT

board.digital[12].write(1)
board.digital[11].write(1)
board.digital[10].write(1)
board.digital[13].write(1)

def HomeAutomation():

    if "on the light" in query or "on light" in query or "light on" in query:
        Speak("as your wish sir, switching on lights")
        board.digital[10].write(0)

    elif "off the light" in query or "of the light" in query or "light off" in query:
        Speak("as your wish sir, switching off lights")
        board.digital[10].write(1)

    elif "on tv" in query or "on the tv" in query or "tv on" in query:
        Speak("as your wish sir, switching on  the tv")
        board.digital[12].write(0)

    elif "go" in query:
        Speak("as your wish sir, switching on  the tv")
        board.digital[13].write(0)

    elif "of go" in query:
        Speak("as your wish sir, switching off the tv" in query)
        board.digital[13].write(1)

    elif "of tv" in query:
        Speak("as your wish sir, switching off the tv" in query)
        board.digital[12].write(1)

    elif "of ac" in query:
        Speak("activating the lights")
        board.digital[11].write(1)