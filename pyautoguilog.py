from pyautogui import *
from time import sleep
from pynput import keyboard
import pyperclip as pyp

sleeptime = 1

def copypaste(streng):
     pyp.copy(str(streng))
     hotkey('command', 'v')

