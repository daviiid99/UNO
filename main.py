# UNO
# Open-game card game created by Mattel
# All creddits to the creators

# First block of code
# Includes the imports and dependencies that this project use

#-------------------------------------------------------------------------------
import os
from random import randint
import random
import json
import threading

os.system("pip3 install wget")
os.system("pip3 install pygame")
os.system("pip install pygame")
os.system("pip3.10 install pygame")

import pygame
import time
from datetime import date
from datetime import datetime
import os.path
import platform
import zipfile
from zipfile import ZipFile
import wget 
from time import perf_counter
from datetime import timedelta

pygame.font.init() # Import font
pygame.mixer.init() # Import sounds

# ------- Imports ----------------------

from cards import *
from save_game import *

# --------------------------------------


def check_main_thread () :
	game_values["START"]["MAIN"]  = "NO"
	silent_save_game()

def welcome () :

	check_main_thread ()

	t2 = threading.Thread(target = press_a_to_start , name="t2")
	t1 = threading.Thread(target = create_title_screen, name="t1")
	t1.start()
	t2.start()

	start = press_a_to_start()

	while game_values["START"]["MAIN"]  == "NO":
		theme.play()
		t2.join()
		t1.join()

def press_a_to_start () :
	while game_values["START"]["MAIN"]  == "NO":

		theme.play()

		for event in pygame.event.get() :

			if event.type == pygame.QUIT:
				run = False
				pygame.quit()

			if event.type == pygame.KEYDOWN :
				if event.key == pygame.K_a:
					game_values["START"]["MAIN"]  = "YES"
					silent_save_game()


def create_title_screen () :

	while game_values["START"]["MAIN"]  == "NO":

		create_title_screen_animation (left, center, right)
		create_title_screen_animation (left_2, center_2, right_2)
		create_title_screen_animation (left_3, center_3, right_3)
		create_title_screen_animation (left_4, center_4, right_4)

def create_title_screen_animation (LEFT_CARD, CENTER_CARD, RIGHT_CARD) :
	

	WIN.fill("#ee2229")
	WIN.blit(logo, (500, 20))

	WIN.blit(LEFT_CARD, (230, 340))
	WIN.blit(RIGHT_CARD, (680, 340))
	WIN.blit(CENTER_CARD, (450, 280))

	clock.tick(1)

	pygame.display.update()



#-------------------------------------------------------------------------------

if __name__ == "__main__":

	welcome()