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
WHITE = (255,255,255)
RED = (93.3,13.3,16.1)


## Game Values
FPS = 60
MAX_CARDS = 108
INITIAL_CARDS = 7
MAX_TURN_TIME = 30
clock = pygame.time.Clock()
small_font = pygame.font.Font(None, 30)
count_font = pygame.font.Font(None, 50)
mini_font = pygame.font.Font(None, 18)


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
cards_deck = pygame.transform.scale(pygame.image.load(os.path.join('Assets/logo', "deck.png")), (320,361))
next_cursor = pygame.transform.scale(pygame.image.load(os.path.join('Assets/cursor', "next.png")), (50,50))
previous_cursor = pygame.transform.scale(pygame.image.load(os.path.join('Assets/cursor', "previous.png")), (50,50))


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
red_0 = pygame.image.load(os.path.join('Assets/deck/red', "0.png"))
red_1 = pygame.image.load(os.path.join('Assets/deck/red', "1.png"))
red_2 = pygame.image.load(os.path.join('Assets/deck/red', "2.png"))
red_3 = pygame.image.load(os.path.join('Assets/deck/red', "3.png"))
red_4 = pygame.image.load(os.path.join('Assets/deck/red', "4.png"))
red_5 = pygame.image.load(os.path.join('Assets/deck/red', "5.png"))
red_6 = pygame.image.load(os.path.join('Assets/deck/red', "6.png"))
red_7 = pygame.image.load(os.path.join('Assets/deck/red', "7.png"))
red_8 = pygame.image.load(os.path.join('Assets/deck/red', "8.png"))
red_9 = pygame.image.load(os.path.join('Assets/deck/red', "9.png"))
red_skip = pygame.image.load(os.path.join('Assets/deck/red', "skip.png"))
red_reverse = pygame.image.load(os.path.join('Assets/deck/red', "reverse.png"))
red_draw = pygame.image.load(os.path.join('Assets/deck/red', "draw_2.png"))

# BLUE
blue_0 = pygame.image.load(os.path.join('Assets/deck/blue', "0.png"))
blue_1 = pygame.image.load(os.path.join('Assets/deck/blue', "1.png"))
blue_2 = pygame.image.load(os.path.join('Assets/deck/blue', "2.png"))
blue_3 = pygame.image.load(os.path.join('Assets/deck/blue', "3.png"))
blue_4 = pygame.image.load(os.path.join('Assets/deck/blue', "4.png"))
blue_5 = pygame.image.load(os.path.join('Assets/deck/blue', "5.png"))
blue_6 = pygame.image.load(os.path.join('Assets/deck/blue', "6.png"))
blue_7 = pygame.image.load(os.path.join('Assets/deck/blue', "7.png"))
blue_8 = pygame.image.load(os.path.join('Assets/deck/blue', "8.png"))
blue_9 = pygame.image.load(os.path.join('Assets/deck/blue', "9.png"))
blue_skip = pygame.image.load(os.path.join('Assets/deck/blue', "skip.png"))
blue_reverse = pygame.image.load(os.path.join('Assets/deck/blue', "reverse.png"))
blue_draw = pygame.image.load(os.path.join('Assets/deck/blue', "draw_2.png"))

# ORANGE
orange_0 = pygame.image.load(os.path.join('Assets/deck/orange', "0.png"))
orange_1 = pygame.image.load(os.path.join('Assets/deck/orange', "1.png"))
orange_2 = pygame.image.load(os.path.join('Assets/deck/orange', "2.png"))
orange_3 = pygame.image.load(os.path.join('Assets/deck/orange', "3.png"))
orange_4 = pygame.image.load(os.path.join('Assets/deck/orange', "4.png"))
orange_5 = pygame.image.load(os.path.join('Assets/deck/orange', "5.png"))
orange_6 = pygame.image.load(os.path.join('Assets/deck/orange', "6.png"))
orange_7 = pygame.image.load(os.path.join('Assets/deck/orange', "7.png"))
orange_8 = pygame.image.load(os.path.join('Assets/deck/orange', "8.png"))
orange_9 = pygame.image.load(os.path.join('Assets/deck/orange', "9.png"))
orange_skip = pygame.image.load(os.path.join('Assets/deck/orange', "skip.png"))
orange_reverse = pygame.image.load(os.path.join('Assets/deck/orange', "reverse.png"))
orange_draw = pygame.image.load(os.path.join('Assets/deck/orange', "draw_2.png"))

# GREEN
green_0 = pygame.image.load(os.path.join('Assets/deck/green', "0.png"))
green_1 = pygame.image.load(os.path.join('Assets/deck/green', "1.png"))
green_2 = pygame.image.load(os.path.join('Assets/deck/green', "2.png"))
green_3 = pygame.image.load(os.path.join('Assets/deck/green', "3.png"))
green_4 = pygame.image.load(os.path.join('Assets/deck/green', "4.png"))
green_5 = pygame.image.load(os.path.join('Assets/deck/green', "5.png"))
green_6 = pygame.image.load(os.path.join('Assets/deck/green', "6.png"))
green_7 = pygame.image.load(os.path.join('Assets/deck/green', "7.png"))
green_8 = pygame.image.load(os.path.join('Assets/deck/green', "8.png"))
green_9 = pygame.image.load(os.path.join('Assets/deck/green', "9.png"))
green_skip = pygame.image.load(os.path.join('Assets/deck/green', "skip.png"))
green_reverse = pygame.image.load(os.path.join('Assets/deck/green', "reverse.png"))
green_draw = pygame.image.load(os.path.join('Assets/deck/green', "draw_2.png"))

# WILD
wild = pygame.image.load(os.path.join('Assets/deck/wild', "wild.png"))
wild_draw_4 = pygame.image.load(os.path.join('Assets/deck/wild', "wild_draw_4.png"))
