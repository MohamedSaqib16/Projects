import screen_brightness_control as sbc
from Scripts.Speak import Speak
from Scripts.Listen import Listen
import time
import pyautogui
from PIL import Image
import os


def Brightness(Brightness):
    brightness = sbc.get_brightness()
    primary = sbc.get_brightness(display=0)

    sbc.set_brightness(Brightness)
    sbc.get_brightness(Brightness)
    Speak(f"brightness set to {Brightness} percent")
    time.sleep(3)

    for monitor in sbc.list_monitors():
        print(monitor, ':', sbc.get_brightness(display=monitor), '%')

def Screenshot():
    file_path = "I:/Projects/Logs/Screenshots/"
    file_name = "screenshot.png"

    screenshot = pyautogui.screenshot()
    screenshot.save(file_path + file_name)

    Speak("Screenshot saved successfully! Do you want to open it?")
    open_file = Listen()

    if "yes" in open_file:
        os.startfile(file_path + file_name)
    else:
        Speak("Screenshot saved to " + file_path + file_name)

def basic(query):
    if "select all" in query:
        pyautogui.hotkey('ctrl', 'a')

    elif "close this window" in query:
        pyautogui.hotkey('alt', 'f4')

    elif "open a new windows" or "new window" in query:
        pyautogui.hotkey('ctrl', 'n')

    elif "open a new incognito window" or "private tab" in query:
        pyautogui.hotkey('ctrl', 'shift', 'n')

    elif "open tab one" or "first tab" in query:
        pyautogui.hotkey('ctrl', '1')

    elif "open tab two" or "second tab" in query:
        pyautogui.hotkey('ctrl', '2')

    elif "open new tab" or "new tab" in query:
        pyautogui.hotkey('ctrl', 'T')

    elif "copy" in query:
        pyautogui.hotkey('ctrl', 'c')
        Speak('text copied to clipboard')

    elif "paste" in query:
        pyautogui.hotkey('ctrl', 'v')

    elif "refresh" in query:
        pyautogui.hotkey('f5')

    elif "undo" in query:
        pyautogui.hotkey('ctrl', 'z')

    elif "redo" in query:
        pyautogui.hotkey('ctrl', )

    elif "change to next window" in query or "next window" in query:
        pyautogui.hotkey('alt', 'tab')

    elif "find" in query:
        pyautogui.hotkey('ctrl', 'f')

    elif "back space" in query:
        pyautogui.hotkey('backspace')

    elif "previous window" in query:
        pyautogui.hotkey('L alt', 'shift ', 'tab')

    elif "save" in query:
        pyautogui.hotkey('ctrl', 's')

    elif "back" in query:
        pyautogui.hotkey('browserback')

    elif "go up" in query:
        pyautogui.hotkey('pageup')

    elif "go to start " in query:
        pyautogui.hotkey('home')


