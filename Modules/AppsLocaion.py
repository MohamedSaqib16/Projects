Rainmeter = "E:\\Rainmeter\\Rainmeter.exe"

from Scripts.Listen import Listen
from AppOpener import open, close

def Appopener(Name):
    print()
    print("1. Open <any_name> TO OPEN APPLICATIONS")
    print("2. Close <any_name> TO CLOSE APPLICATIONS")
    print()
    open("help")
    print("TRY 'OPEN <any_key>'")

    inp = Name
    if "close " in inp:
        app_name = inp.replace("close ","").strip()
        close(app_name, match_closest=True, output=False) # App will be close be it matches little bit too (Without printing context (like CLOSING <app_name>))
    if "open " in inp:
        app_name = inp.replace("open ","")
        open(app_name, match_closest=True) # App will be open be it matches little bit too

