from playsound import playsound
import os,sys

def pronounce():
    playsound('audio.mp3')
    os.remove("audio.mp3")


