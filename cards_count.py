import pygame
from cards import *

game_cards= [
        					red_0, red_1, red_2, red_3, red_4, red_5, red_6, red_7, red_8, red_9, red_skip, red_reverse, red_draw, wild,
        					blue_0, blue_1, blue_2, blue_3, blue_4, blue_5, blue_6, blue_7, blue_8, blue_9, blue_skip, blue_reverse, blue_draw, wild,
        					orange_0, orange_1, orange_2, orange_3, orange_4, orange_5, orange_6, orange_7, orange_8, orange_9, orange_skip, orange_reverse, orange_draw, wild,
        					green_0, green_1, green_2, green_3, green_4, green_5, green_6, green_7, green_8, green_9, green_skip, green_reverse, green_draw, wild,
        					red_1, red_2, red_3, red_4, red_5, red_6, red_7, red_8, red_9, red_skip, red_reverse, red_draw, wild_draw_4,
        					orange_1, orange_2, orange_3, orange_4, orange_5, orange_6, orange_7, orange_8, orange_9, orange_skip, orange_reverse, orange_draw, wild_draw_4,
        					green_1, green_2, green_3, green_4, green_5, green_6, green_7, green_8, green_9, green_skip, green_reverse, green_draw, wild_draw_4,
        					blue_1, blue_2, blue_3, blue_4, blue_5, blue_6, blue_7, blue_8, blue_9, blue_skip, blue_reverse, blue_draw, wild_draw_4
        					 ]

count = 0

game_cards.remove(red_1)
game_cards.remove(red_1)

for card in game_cards :
	count +=1

print("Hay %d cartas" % count)
