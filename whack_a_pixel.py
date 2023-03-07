from blinkt import set_brightness, set_pixel, show, clear, set_all
import time
import random
import sys


def input_from_user():
	user_pixel = input()
	try:
		user_pixel = int(user_pixel)
	except ValueError:
		print(f"You did not enter an integer")
		return(10)
	return(user_pixel)


def main():
	set_brightness(0.1)
	life = 3
	level = 1

	while True:
		pixel = random.randint(0,7)
		set_pixel(pixel, 255, 255, 255)
		show()
		time.sleep(1/level)
		clear()
		show()
		user_pixel = input_from_user()
		if user_pixel-1 == pixel:
			set_all(255, 255, 255)
			show()
			time.sleep(0.2)
			set_all(0, 0, 0)
			#clear()
			show()
			time.sleep(0.5)
			print(f"Correct. You still have {life} lives left.")
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
			print(f"You have {life} lives left.")
		level += 1

if __name__ == "__main__":
	main()
