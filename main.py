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
import os.path
from pathlib import Path

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
from player import *

# --------------------------------------

# --------- Global variables ------------

version = "1.7"

# ------------------------------

def check_main_thread () :
        game_values["START"]["MAIN"]  = "NO"
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

    version = small_font.render("v1.7", 1, WHITE)
    WIN.blit(version, (20, 20) )

    if updated :
        updates = mini_font.render("UNO is up-to-date!", 1, WHITE)
        WIN.blit(updates, (1150, 20) )

    else  :
        updates = mini_font.render("A new update is available!", 1, WHITE)
        WIN.blit(updates, (1080, 20) )

    copyright = small_font.render("©1971-2022 MATTEL, INC", 1, WHITE)
    WIN.blit(copyright, (20, 600) )

    copyright = mini_font.render("UNO brand, logo and assets", 1, WHITE)
    WIN.blit(copyright, (1060, 580) )

    copyright = mini_font.render("are registered by MATTEL", 1, WHITE)
    WIN.blit(copyright, (1060, 600) )

    copyright = mini_font.render("in the United States", 1, WHITE)
    WIN.blit(copyright, (1060, 620) )


    clock.tick(1)

    pygame.display.update()

def latest_version_installed() :
    message = False

    # Read the version string from an external text document
    if platform.system() == "Linux" :
        os.system("rm -f version.txt")
    else :
        os.system("del /f version.txt")

    try:
        wget.download("https://raw.githubusercontent.com/daviiid99/UNO/master/version.txt") 

    except:
        message = False

    try :

        version_str = Path('version.txt').read_text()
        version_str = version_str.replace('\n', '')

        # Check if the latest version is installed
        if version_str == version :
            message = True

    except :
        message = False

    return message

updated = latest_version_installed()

class Main :
    def __init__(self) :
        pygame.init()
        self.running = True
        self.screen = WIN
        self.rect = self.screen.get_rect()
        self.mouse = vec()
        self.mouse_visible = True
        self.clock = pygame.time.Clock()

    def check_click(self, mouse):
        if self.rect.collidepoint(mouse):
            p = Player()
            game_values["START"]["MAIN"]  = "YES"
            silent_save_game()
            p.select_players()


    def welcome (self) :

        check_main_thread ()

        t2 = threading.Thread(target = self.press_to_start , name="t2")
        t1 = threading.Thread(target = create_title_screen, name="t1")
        t1.start()
        t2.start()

        start =  self.press_to_start()

        while game_values["START"]["MAIN"]  == "NO":
            theme.play()
            t2.join()
            t1.join()

    def press_to_start (self) :
        while game_values["START"]["MAIN"]  == "NO":

            theme.play()

            for event in pygame.event.get() :

                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.check_click(event.pos)


    def start_game (self) :
        while self.running:
            delta_time = self.clock.tick() / 1000
            self.welcome()


start = Main()
start.start_game()