from blinkt import set_brightness, set_pixel, show, clear, set_all
import time
import random
import sys

set_brightness(0.1)
life = 3
level = 1

while True:
	pixel = random.randint(0,7)
	set_pixel(pixel, 255, 255, 255)
	show()
	time.sleep(1/level)
	#set_pixel(pixel, 0, 0, 0)
	clear()
	show()
	user_pixel = int(input())
	#time.sleep(0.5)
	#user_pixel = pixel + 10
	if user_pixel-1 == pixel:
		set_all(255, 255, 255)
		show()
		time.sleep(0.2)
		set_all(0, 0, 0)
		#clear()
		show()
		time.sleep(0.5)
		f"Correct. You still have {life} lives left."
	else:
		for i in range(life):
			set_all(255, 0, 0)
			show()
			time.sleep(0.2)
			set_all(0, 0, 0)
			#clear()
			show()
			time.sleep(0.5)
		if life == 0:
			sys.exit(f"***Game Over***")
		life -= 1
		f"You have {life} lives left."
	level += 1
