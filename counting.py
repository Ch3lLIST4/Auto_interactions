# pip install pynput 
from pynput.keyboard import Key, Controller
import time
import hashlib 


COOLDOWN = 5 # server cooldown
NUMBER = 1 # starting number


keyboard = Controller()

time.sleep(2)

while (True):
	for digit in str(NUMBER):
		keyboard.press(digit)
		keyboard.release(digit)

	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
	
	NUMBER = NUMBER + 1
	time.sleep(COOLDOWN + 1)
