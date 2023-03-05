import os
import sys

def auth_user():
    # If user has already logged in => can get token from file.
    if os.file.exists(".cache"):
        return

    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print("Whoops, need a username!")
        print("usage: python main.py [username]")
        sys.exit()
