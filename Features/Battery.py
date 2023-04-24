from Scripts.Speak import Speak
import psutil

def Battery():
    battery = psutil.sensors_battery()
    battery_percentage = str(battery.percent)
    plugged = battery.power_plugged
    Speak(f"Battery is at {battery_percentage} percent.")
    if plugged:
        Speak("Status : charging....")
    if not plugged:
        if battery_percentage <= "95%":
            Speak("Status : Not charging.")

