import os

DEBUG = int(os.environ.get("DEBUG", 0))

def debug_print(msg):
    if DEBUG:
        print(msg)
