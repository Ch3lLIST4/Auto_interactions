# pip install pynput 
from pynput.keyboard import Key, Controller
import time
import hashlib 

keyboard = Controller()

time.sleep(2)

number = 1;

while (True):
	for digit in str(number):
		keyboard.press(digit)
		keyboard.release(digit)

	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
	
	number = number + 1
	time.sleep(1)