# pip install pynput 
from pynput.keyboard import Key, Controller
import time


COOLDOWN = 5 # server cooldown
DELAY = 2 # server delay
NUMBER = 52727 # starting number


keyboard = Controller()

time.sleep(2)

while (True):
	for digit in str(NUMBER):
		keyboard.press(digit)
		keyboard.release(digit)

	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
	
	NUMBER = NUMBER + 1
	time.sleep(COOLDOWN + DELAY)
