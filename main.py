from pyautogui import *
import pyautogui as p
from pynput import keyboard
from time import sleep
from threading import Thread
import datetime
import pyperclip as pyp
import sys
import os

def moveTo_percent(percX: int, percY: int, seconds=0.01):
    screen_size = size()

    screen_size_x = screen_size[0]

    screen_size_y = screen_size[1]
    moveTo((percX / 100) * screen_size_x, screen_size_y - (percY / 100) * screen_size_y, seconds)


def write_to_file(streng: str):
    with open("pyautoguilog.py", "a") as f:
        f.write(streng + "\n")
        print(streng)

def clear_file():
    with open("pyautoguilog.py", "w") as f:
        f.truncate(0)


def initialize_file():
    clear_file()
    write_to_file("from pyautogui import *")
    write_to_file("from time import sleep")
    write_to_file("from pynput import keyboard")
    write_to_file("")
    write_to_file("sleeptime = 1")






'''
known bugs
only works after the second try
'''
i = datetime.datetime.now()
diff = 0

count = 0
Enable_Keyboard_Hotkeys = False
p.PAUSE = 0.0001
p.DARWIN_CATCH_UP_TIME = 0.0001

recorder = ""
last_char = ""
second_to_last_char = ""


def millitimer():
    global i
    global diff
    i = datetime.datetime.now()
    while True:
        q = datetime.datetime.now()
        diff1 = str(q - i)
        diff2 = diff1[-9:]
        diff3 = diff2[:-3]
        diff = diff3.replace(".", "")


def start_keyboard():
    with keyboard.Listener(on_press=on_press) as listener: listener.join()


def add_new_hotkey(streng: str, pressed_btn: str = None, action=None):
    clear()
    copypaste(streng)


def copypaste(streng):
    pyp.copy(str(streng))
    p.hotkey('command', 'v')


def kill_program():
    os.system("kill " + str(os.getpid()))


def clear():
    p.hotkey('left')
    p.hotkey('left')
    p.hotkey('delete')
    p.hotkey('delete')


def get_three_digit_milliseconds():
    global i, diff
    # get first 3 digit milliseconds
    Element_Array = [str(diff)]
    res = [ele.lstrip('0') for ele in Element_Array]
    diff = res[0]
    i = datetime.datetime.now()


def on_press(key): #mainstuffoccurshere
    global recorder, last_char, second_to_last_char, diff, count, Enable_Keyboard_Hotkeys
    if key == keyboard.Key.esc:
        sleep(1)
        pid = os.getpid()
        print("killing process", pid)
        os.system("kill " + str(pid))
    try:
        # string manipulation
        recorder += str(format(key.char))
        last_char = recorder[-1]
        if len(recorder) > 1:
            second_to_last_char = recorder[-2]
        if len(recorder) % 2 == 0:
            temp_char = recorder[-1]
            recorder = ""
            recorder += temp_char
        get_three_digit_milliseconds()
        # test_print()

        if Enable_Keyboard_Hotkeys:
            if last_char == "c":
                write_to_file("hotkey('command', 'c')")
            if last_char == "v":
                write_to_file("hotkey('command', 'v')")
            if last_char == "w":
                pos = position()
                write_to_file(f"moveTo({pos[0]}, {pos[1]}, 1)")
            if last_char == "d":
                write_to_file("mouseDown()")
            if last_char == "u":
                write_to_file("mouseUp()")
            if last_char == "1":
                write_to_file("hotkey('ctrl', 'left', interval = 0.25)")
            if last_char == "2":
                write_to_file("hotkey('ctrl', 'right', interval = 0.25)")
            if last_char == "x":
                write_to_file("click(interval=sleeptime)")
            if last_char == "s":
                write_to_file("sleep(sleeptime)")
            if last_char == "m":
                pos = position()
                write_to_file(f"moveTo({pos[0]}, {pos[1]}, 1)")
                write_to_file("click()")
    except Exception as e:

        if key == keyboard.Key.alt:
            Enable_Keyboard_Hotkeys = True
            print('enabled')


        elif key == keyboard.Key.shift_r:
            Enable_Keyboard_Hotkeys = False
            print('disabled')






def test_print():
    global recorder, last_char, second_to_last_char
    print(recorder, "\t" + second_to_last_char, "\t" + last_char)
    if second_to_last_char == last_char:
        print('tripped')

def start_main(): #starts everything
    Thread(target=millitimer).start()
    start_keyboard()


if __name__ == "__main__":
    clear_file()
    initialize_file()
    Thread(target=start_main).start()

