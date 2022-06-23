import os
import json
from cards import *

def silent_save_game () :
	saving = True
	my_save_slot = json.dumps(game_values)
	with open('game_values.json', 'w') as save:
		save.write(my_save_slot)
