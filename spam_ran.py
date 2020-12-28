# pip install pynput 
from pynput.keyboard import Key, Controller
import time
from string import digits, ascii_letters, punctuation
import random


delay = 1.5

try:
    keyboard = Controller()

    time.sleep(2)

    letters = ascii_letters + digits + punctuation

    length = random.randint(100,110)

    while (True):   

        ran_string = "".join(random.choice(letters) for _ in range(int(length)))
        for char in ran_string:   
            keyboard.press(char)
            keyboard.release(char)

        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(delay)
except Exception as e:
    print(e)