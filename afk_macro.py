import random
import pyautogui
import keyboard
import time
import os

def timer(seconds):
	for i in range(1, seconds+1):
		print(seconds+1-i)
		time.sleep(1)

def press_key(key, sleep_time):
	print(f"-Pressing '{key}' for {round(sleep_time,2)} seconds")
	if key == "space":
		pyautogui.press("space")
	else:
		pyautogui.keyDown(key)
		time.sleep(sleep_time)
		pyautogui.keyUp(key)




def rand_movement():
	key_binds = ["w","a","s","d", "space"]
	prev_key = ""

	time_elapsed = 0

	for i in range(0, random.randint(1,3)):
		for j in range(0, random.randint(3,5)):
			key = key_binds[random.randint(0,len(key_binds)-1)] 
			if (prev_key == key) and (key == "space"):
				print("Avoided double space")
				pass
			else:
				click_or_key = random.uniform(0, 1)
				if click_or_key >= 0.3:
					rand_float = random.uniform(0.3, 1.2)
					press_key(key, rand_float)
					time_elapsed += rand_float
					prev_key = key
				else:
					print("-Click")
					pyautogui.click(button="left")
			
	
	return time_elapsed

def main():
	timer(3)
	time_elapsed = 0
	finished = False
	while True:
		time_elapsed += rand_movement()
		wait_time = random.randint(10, 25)
		print(f"Waiting {wait_time} seconds")
		time.sleep(wait_time)

		time_elapsed += wait_time

		print(f"Aprox time elapsed: {round(time_elapsed/60,2)} min | {round((12660-time_elapsed)/60,2)} min left")

		#3.5 hrs = 12660 sec
		if time_elapsed >= 12660:
			print("Terminating")
			finished = True
			break

		if keyboard.is_pressed("q"):
			print("Terminating")
			break

	if finished:
		os.system("rundll32.exe powrprof.dll, SetSuspendState 0, 1, 0")


main()
