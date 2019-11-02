import keyboard, pyautogui, PIL
from time import sleep
from datetime import datetime
from PIL import ImageGrab 
from time import times
import this and that

# dimentions and position of the screenshot 
width = 600
height = 50
left = 1300
top = 425


# speicific timing for the increase of speed
sleep_const = 1800		# sleep x-cordinate/sleep_cost seconds before jump

timing_const = 10		# every timing_const seconds, we increase
sleep_add = 350			#     sleep_const by sleep_add
count = 1				# count store the current timing_const block


# screen: the array of pixels from the screenshot
# returns the first col (x pos) that isnt white
# if all white, return -1 
def check(screen):
	for row in range(height):
		for col in range(width):
			if not screen[col,row] == (255,255,255,255):
				return col
	return -1


# give time to open the dino game
sleep(3)

# timing puposes
past = time()


while True:

	# get the screenshot
	screen = ImageGrab.grab(bbox=(left, top, left+width, top+height))

	# update sleep_const if it's a new block of time
	# specified by timing_const
	now = time()
	elapsed = now-past
	if elapsed > timing_const*count:
		count += 1
		sleep_const += sleep_add

	# look for the first black pixel
	x = check(screen.load())
	if not x == -1:
		# if there is one, wait then press up on keyboard
		sleep(x/sleep_const)
		pyautogui.press("up")
		continue


#screen.show()	
#screen = pyautogui.screenshot(region=(left,top,width,height))
#keyboard.on_press_key("enter", stop)
#screen.save("screenshots/"+datetime.now().strftime("%M:%S:")+str(.now().microsecond)+".png")


