import keyboard, pyautogui, PIL
from time import sleep
from datetime import datetime
from PIL import ImageGrab 
from time import time

width = 600
height = 50
left = 1300
top = 425

sleep_const = 1800
timing_const = 10
sleep_add = 350

def stop(event):
	quit()	


def check(screen):
	for row in range(height):
		for col in range(width):
			if not screen[col,row] == (255,255,255,255):
				return col
	return -1

sleep(2)

#keyboard.on_press_key("enter", stop)


past = time()
count = 1

while True:
	
	#screen = pyautogui.screenshot(region=(left,top,width,height))

	#screen.save("screenshots/"+datetime.now().strftime("%M:%S:")+str(datetime.now().microsecond)+".png")

	screen = ImageGrab.grab(bbox=(left, top, left+width, top+height))

	now = time()
	elapsed = now-past
	print("time elapsed: "+str(elapsed))

	if elapsed > timing_const*count:
		count += 1
		sleep_const += sleep_add

	x = check(screen.load())
	if not x == -1:
		sleep(x/sleep_const)
		pyautogui.press("up")
		print(x/sleep_const)
		
		print("saw thinging")
		#screen.show()	
		continue



	
	


