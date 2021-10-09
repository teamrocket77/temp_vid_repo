import cv2
import os
from mutagen.mp3 import MP3
import string
import re



def firstdirfinder():
    with os.scandir(os.getcwd()) as it:
        for item in it:
            if not(str(item).endswith('py\'>') or str(item).endswith('jpg\'>')):
                print(item)
