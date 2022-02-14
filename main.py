from pyautogui import *
import keyboard


def moveTo_percent(percX: int, percY: int, seconds=0.01):
    screen_size = size()

    screen_size_x = screen_size[0]

    screen_size_y = screen_size[1]
    moveTo((percX / 100) * screen_size_x, screen_size_y - (percY / 100) * screen_size_y, seconds)


def write_to_file(streng: str):
    with open("pyautoguilog.py", "a") as f:
        f.write(streng + "\n")

def clear_file():
    with open("pyautoguilog.py", "w") as f:
        f.truncate(0)


def scan_for_key_presses():
    clear_file()
    write_to_file("from pyautogui import *")
    write_to_file("from time import sleep")
    write_to_file("from pynput import keyboard")


scan_for_key_presses()