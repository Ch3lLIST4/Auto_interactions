# pip install pynput 
from pynput.keyboard import Key, Controller
import time
import hashlib 

keyboard = Controller()

time.sleep(2)

starting_number = 1;
salt = "Salt123Impo5s1bleT0Cr4ck"

while (True):   

    md5_hash = hashlib.sha3_512((str(starting_number) + salt)
    .encode()).hexdigest()
    for char in md5_hash:   
        keyboard.press(char)
        keyboard.release(char)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    starting_number = starting_number + 1
    time.sleep(1.5)
