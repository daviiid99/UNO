import os
import pygame
import json
import sys
import ctypes


## Game board
pygame.init()
width, height = 640, 480
fpsClock = pygame.time.Clock()
WIN = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
if sys.platform == "win32":
    HWND = pygame.display.get_wm_info()['window']
    SW_MAXIMIZE = 3
    ctypes.windll.user32.ShowWindow(HWND, SW_MAXIMIZE)

BLACK = (0,0,0)
RED = (93.3,13.3,16.1)


## Game Values
FPS = 60
MAX_CARDS = 108
INITIAL_CARDS = 7
MAX_TURN_TIME = 30
clock = pygame.time.Clock()

## App Info
icon = pygame.image.load('Assets/logo/logo.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("UNO")

# Theme
theme = pygame.mixer.Sound("Assets/sounds/theme.mp3")

# Player values
my_save_slot = open("game_values.json")
game_values = json.load(my_save_slot)

# Game Assets

# Title Screen
logo = pygame.image.load(os.path.join('Assets/logo', "logo.png"))

# Left card
left = pygame.image.load(os.path.join('Assets/main_screen', "left.png"))
left_2 = pygame.image.load(os.path.join('Assets/main_screen', "left_2.png"))
left_3 = pygame.image.load(os.path.join('Assets/main_screen', "left_3.png"))
left_4 = pygame.image.load(os.path.join('Assets/main_screen', "left_4.png"))

# Center card
center = pygame.image.load(os.path.join('Assets/main_screen', "center.png"))
center_2 = pygame.image.load(os.path.join('Assets/main_screen', "center_2.png"))
center_3 = pygame.image.load(os.path.join('Assets/main_screen', "center_3.png"))
center_4 = pygame.image.load(os.path.join('Assets/main_screen', "center_4.png"))

# Right card
right = pygame.image.load(os.path.join('Assets/main_screen', "right.png"))
right_2 = pygame.image.load(os.path.join('Assets/main_screen', "right_2.png"))
right_3 = pygame.image.load(os.path.join('Assets/main_screen', "right_3.png"))
right_4 = pygame.image.load(os.path.join('Assets/main_screen', "right_4.png"))

# Player Screen

# 1 Player
player_1 = pygame.image.load(os.path.join('Assets/players_screen', "1_player.png"))

# 2 Players
player_2 = pygame.image.load(os.path.join('Assets/players_screen', "2_player.png"))

# 3 Players
player_3 = pygame.image.load(os.path.join('Assets/players_screen', "3_player.png"))


# RED


# BLUE


# ORANGE


# GREEN


# WILD