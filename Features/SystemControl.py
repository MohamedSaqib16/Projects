import screen_brightness_control as sbc
from Scripts.Speak import Speak
import time

def Brightness(Brightness):
    brightness = sbc.get_brightness()
    primary = sbc.get_brightness(display=0)

    sbc.set_brightness(Brightness)
    sbc.get_brightness(Brightness)
    Speak(f"brightness set to {Brightness} percent")
    time.sleep(3)

    for monitor in sbc.list_monitors():
        print(monitor, ':', sbc.get_brightness(display=monitor), '%')

