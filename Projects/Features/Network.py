import socket

REMOTE_SERVER = "www.google.com"

def is_connected():
    try:
        # connect to the remote server
        host = socket.gethostbyname(REMOTE_SERVER)
        s = socket.create_connection((host, 80), 2)
        return True
    except:
        pass
    return False

if is_connected():
    print("Internet connected")
    # your code here
else:
    print("No internet connection")
