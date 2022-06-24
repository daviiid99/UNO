from cards import *
from random import randint
from save_game import *
import threading
import time


vec = pygame.math.Vector2

def vec_to_int(vector):
    return int(vector.x), int(vector.y)

class Board :

    def __init__(self) :
        pygame.init()
        self.running = True
        self.font = pygame.font.Font(None, 100)
        self.color = pygame.Color('white')
        self.screen = WIN
        self.timer_Screen = WIN
        self.rect = self.screen.get_rect()
        self.mouse = vec()
        self.mouse_visible = True
        self.player_one_name = ''
        self.player_two_name = ''
        self.player_three_name = ''
        self.deck = pygame.Rect(315, 80, 180, 290)
        self.game_cards= [
                            red_0, red_1, red_2, red_3, red_4, red_5, red_6, red_7, red_8, red_9, red_skip, red_reverse, red_draw, wild,
                            blue_0, blue_1, blue_2, blue_3, blue_4, blue_5, blue_6, blue_7, blue_8, blue_9, blue_skip, blue_reverse, blue_draw, wild,
                            orange_0, orange_1, orange_2, orange_3, orange_4, orange_5, orange_6, orange_7, orange_8, orange_9, orange_skip, orange_reverse, orange_draw, wild,
                            green_0, green_1, green_2, green_3, green_4, green_5, green_6, green_7, green_8, green_9, green_skip, green_reverse, green_draw, wild,
                            red_1, red_2, red_3, red_4, red_5, red_6, red_7, red_8, red_9, red_skip, red_reverse, red_draw, wild_draw_4,
                            orange_1, orange_2, orange_3, orange_4, orange_5, orange_6, orange_7, orange_8, orange_9, orange_skip, orange_reverse, orange_draw, wild_draw_4,
                            green_1, green_2, green_3, green_4, green_5, green_6, green_7, green_8, green_9, green_skip, green_reverse, green_draw, wild_draw_4,
                            blue_1, blue_2, blue_3, blue_4, blue_5, blue_6, blue_7, blue_8, blue_9, blue_skip, blue_reverse, blue_draw, wild_draw_4
                             ]
        self.game_cards_names= [
                            "red_0", "red_1", "red_2", "red_3", "red_4", "red_5", "red_6", "red_7", "red_8", "red_9", "red_skip", "red_reverse", "red_draw", "wild",
                            "blue_0", "blue_1", "blue_2", "blue_3", "blue_4", "blue_5", "blue_6", "blue_7", "blue_8", "blue_9", "blue_skip", "blue_reverse", "blue_draw", "wild",
                            "orange_0", "orange_1", "orange_2", "orange_3", "orange_4", "orange_5", "orange_6", "orange_7", "orange_8", "orange_9", "orange_skip", "orange_reverse", "orange_draw", "wild",
                            "green_0", "green_1", "green_2", "green_3", "green_4", "green_5", "green_6", "green_7", "green_8", "green_9", "green_skip", "green_reverse", "green_draw", "wild",
                            "red_1", "red_2", "red_3", "red_4", "red_5", "red_6", "red_7", "red_8", "red_9", "red_skip", "red_reverse", "red_draw", "wild_draw_4",
                            "orange_1", "orange_2", "orange_3", "orange_4", "orange_5", "orange_6", "orange_7", "orange_8", "orange_9", "orange_skip", "orange_reverse", "orange_draw", "wild_draw_4",
                            "green_1", "green_2", "green_3", "green_4", "green_5", "green_6", "green_7", "green_8", "green_9", "green_skip", "green_reverse", "green_draw", "wild_draw_4",
                            "blue_1", "blue_2", "blue_3", "blue_4", "blue_5", "blue_6", "blue_7", "blue_8", "blue_9", "blue_skip", "blue_reverse", "blue_draw", "wild_draw_4"]

        self.available_cards = 0

        self.player_one_cards = []
        self.player_one_card_names = []

        self.player_two_cards = []
        self.player_two_card_names = []

        self.player_three_cards = []
        self.player_three_card_names = []

        self.random_card = self.game_cards[0] 
        self.random_card_name = ''

        self.player_one_turn = True
        self.player_two_turn = False
        self.player_three_turn = False
        self.card_witdh = 50
        self.card_height = 400
        self.card_one_rect = pygame.Rect(480, 350, 255, 290)
        self.next = pygame.Rect(1220, 550, 50, 50)
        self.previous = pygame.Rect(5, 550, 50, 50)
        self.current_turn_pick = False
        self.next_seven = False
        self.previous_seven = True

        self.card_one_rect = pygame.Rect(70, 400, 150, 361)
        self.card_two_rect = pygame.Rect(220, 400, 150, 361)
        self.card_three_rect = pygame.Rect(360, 400, 155, 361)
        self.card_four_rect = pygame.Rect(505, 400, 160, 361)
        self.card_five_rect = pygame.Rect(650, 400, 165, 361)
        self.card_six_rect = pygame.Rect(800, 400, 165, 361)
        self.card_seven_rect = pygame.Rect(950, 400, 240, 361)

        self.next_turn_rect = pygame.Rect(1000, 80, 230, 320)
        self.uno_rect = pygame.Rect(800, 80, 200, 270)
        self.timer = 30

        self.player_one_uno = False
        self.player_two_uno = False
        self.player_three_uno = False

        self.player_one_points = 0
        self.player_two_points = 0
        self.player_three_points = 0

        self.choosed_wild = False
        self.choosed_red_rect = pygame.Rect(400, 170, 220, 200)
        self.choosed_blue_rect = pygame.Rect(600, 370, 220, 200)
        self.choosed_orange_rect = pygame.Rect(400, 370, 220, 200)
        self.choosed_green_rect = pygame.Rect(600, 170, 220, 200)

    def check_board_threads (self) :
        game_values["START"]["TURN"] = "NO"
        silent_save_game()


    def assign_players(self) :
        players = game_values["PLAYERS"]

        if players == 1 :
            self.player_one_name = game_values["PLAYER"]["1"]

        elif players == 2:
            self.player_one_name = game_values["PLAYER"]["1"]
            self.player_two_name = game_values["PLAYER"]["2"]

        elif players == 3:
            self.player_one_name = game_values["PLAYER"]["1"]
            self.player_two_name = game_values["PLAYER"]["2"]
            self.player_three_name = game_values["PLAYER"]["3"]

    def available_card(self) :
        count = 0

        for card in self.game_cards :
            count +=1

        self.available_cards = count

    def assign_first_card(self) :

        random_card = randint(0, len(self.game_cards))

        # Assign the card
        self.random_card = self.game_cards[random_card]

        # Assign the card name
        self.random_card_name = self.game_cards_names[random_card]

        # Remove the card from total
        self.game_cards.remove(self.random_card)
        self.game_cards_names.remove(self.random_card_name)

        if "wild" in self.random_card_name :
            self.choosed_wild = True
            self.choosed_color()



    def first_turn_cards_assign(self) :
        if self.player_one_name != '' :
            self.first_turn_cards_picks(self.player_one_cards, self.player_one_card_names)

        if self.player_two_name != '' :
            self.first_turn_cards_picks(self.player_two_cards, self.player_two_card_names)

        if self.player_three_name != '' :
            self.first_turn_cards_picks(self.player_three_cards, self.player_three_card_names)


    def first_turn_cards_picks (self, player_cards, player_cards_names) :
        # Max number of cards at start
        count = 7 

        while count > 0 :

            # Search for a random card
            carta = randint(0, len(self.game_cards) - 1)
            card_name = self.game_cards_names[carta]
            carta = self.game_cards[carta]


            # Remove the card from deck
            self.game_cards.remove(carta)
            self.game_cards_names.remove(card_name)

            # Assign the card to player cards
            player_cards.append(carta)
            player_cards_names.append(card_name)

            # Decrease the remaining cards counter
            count -=1

        self.available_cards -=7

    def draw_cards_picks (self, player_cards, player_cards_names, count) :
        # Max number of cards at start

        while count > 0 :

            # Search for a random card
            carta = randint(0, len(self.game_cards) - 1)
            card_name = self.game_cards_names[carta]
            carta = self.game_cards[carta]


            # Remove the card from deck
            self.game_cards.remove(carta)
            self.game_cards_names.remove(card_name)

            # Assign the card to player cards
            player_cards.append(carta)
            player_cards_names.append(card_name)

            # Decrease the remaining cards counter
            count -=1

        self.available_cards -=count

    def skip_turn(self) :
        if self.player_one_turn :
            if self.player_two_name != '' and self.player_three_name != '' :
                self.player_one_turn = False
                self.player_three_turn = True
                self.current_turn_pick = False
                self.next_seven = False
                self.previous_seven = True
                self.timer = 30

            elif self.player_three_name == '' :
                self.player_one_turn = True
                self.current_turn_pick = False
                self.next_seven = False
                self.previous_seven = True
                self.timer = 30

        elif self.player_two_turn :
            if self.player_three_name != '' :
                self.player_one_turn = True
                self.current_turn_pick = False
                self.next_seven = False
                self.previous_seven = True
                self.timer = 30

            elif self.player_three_name == '' :
                self.player_two_turn = True
                self.current_turn_pick = False
                self.next_seven = False
                self.previous_seven = True
                self.timer = 30

        elif self.player_three_turn :
                self.player_three_turn = True
                self.current_turn_pick = False
                self.next_seven = False
                self.previous_seven = True
                self.timer = 30

    def reverse_turn(self) :

        if self.player_one_turn :
            self.current_turn_pick = False
            self.next_seven = False
            self.previous_seven = True
            self.timer = 30

        elif self.player_two_turn :
            self.current_turn_pick = False
            self.next_seven = False
            self.previous_seven = True
            self.timer = 30

        elif self.player_three_turn :
            self.current_turn_pick = False
            self.next_seven = False
            self.previous_seven = True
            self.timer = 30


    def next_turn (self) :
        if self.player_one_turn :
            if self.player_two_name != '' :
                self.player_one_turn = False
                self.player_two_turn = True
                self.current_turn_pick = False
                self.next_seven = False
                self.previous_seven = True
                self.timer = 30

        elif self.player_two_turn :
            if self.player_three_name != '' :
                self.player_two_turn = False
                self.player_three_turn = True
                self.current_turn_pick = False
                self.next_seven = False
                self.previous_seven = True
                self.timer = 30


            else :
                self.player_two_turn = False
                self.player_one_turn = True
                self.current_turn_pick = False
                self.next_seven = False
                self.previous_seven = True
                self.timer = 30


        elif self.player_three_turn :
            self.player_three_turn = False
            self.player_one_turn = True
            self.current_turn_pick = False
            self.next_seven = False
            self.previous_seven = True
            self.timer = 30

    def draw_cards (self, count) :
        if self.player_one_turn :
            if self.player_two_name != '' :
                self.player_two_turn = True
                self.current_turn_pick = False
                self.next_seven = False
                self.previous_seven = True
                self.draw_cards_picks(self.player_two_cards, self.player_two_card_names, count)

        elif self.player_two_turn :
            if self.player_three_name != '' :
                self.player_three_turn = True
                self.current_turn_pick = False
                self.next_seven = False
                self.previous_seven = True
                self.draw_cards_picks(self.player_three_cards, self.player_three_card_names, count)

            elif self.player_three_name == '' :
                self.player_one_turn = True
                self.current_turn_pick = False
                self.next_seven = False
                self.previous_seven = True
                self.draw_cards_picks(self.player_one_cards, self.player_one_card_names, count)


        elif self.player_three_turn :
            self.player_one_turn = True
            self.current_turn_pick = False
            self.next_seven = False
            self.previous_seven = True
            self.draw_cards_picks(self.player_one_cards, self.player_one_card_names, count)



    def choosed_color(self) :
        while self.choosed_wild :

            for event in pygame.event.get() :

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.check_click_wild(event.pos)

            self.screen.blit(colors, (350, 70))

            pygame.display.update()

    def check_deck_card_compatibility (self, player_card_name) :
        isRed = False
        isGreen = False
        isBlue = False
        isOrange = False
        isWild = False
        isWildDraw = False

        isRed_Player = False
        isGreen_Player = False
        isBlue_Player = False
        isOrange_Player = False
        isWild_Player = False
        isWildDraw_Player = False

        isValid = False

        if "wild" in player_card_name :
            isValid = True

        # Check the current deck card color
        current = self.random_card_name

        if "red" in current :
            isRed = True

        elif "blue" in current :
            isBlue = True

        elif "green" in current :
            isGreen = True

        elif "orange" in current :
            isOrange = True


         # Check the player card color
        if "red" in player_card_name :
            isRed_Player = True

        elif "blue" in player_card_name :
            isBlue_Player = True

        elif "green" in player_card_name :
            isGreen_Player = True

        elif "orange" in player_card_name :
            isOrange_Player = True


         # Check color compatibility

        if isRed and isRed_Player :
            isValid = True

        elif isBlue and isBlue_Player :
            isValid = True

        elif isGreen and isGreen_Player :
            isValid = True

        elif isOrange and isOrange_Player :
            isValid = True


        # Check number type compatibility
        if "0" in current and "0" in player_card_name :
            isValid = True

        elif "1" in current and "1" in player_card_name :
            isValid = True

        elif "2" in current and "2" in player_card_name :
            isValid = True

        elif "3" in current and "3" in player_card_name :
            isValid = True

        elif "4" in current and "4" in player_card_name :
            isValid = True

        elif "5" in current and "5" in player_card_name :
            isValid = True

        elif "6" in current and "6" in player_card_name :
            isValid = True

        elif "7" in current and "7" in player_card_name :
            isValid = True

        elif "8" in current and "8" in player_card_name :
            isValid = True

        elif "9" in current and "9" in player_card_name :
            isValid = True

        # Check special cards compatibility
        if "skip" in current and "skip" in player_card_name :
            isValid = True

        elif "reverse" in current and "reverse" in player_card_name :
            isValid = True

        return isValid

    def choosed_color(self) :
        while self.choosed_wild :

            for event in pygame.event.get() :

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.check_click_wild(event.pos)

            self.screen.blit(colors, (350, 70))

            pygame.display.update()

    def check_click_wild(self,mouse) :
        # Check if user is using a wild draw card
        if self.choosed_red_rect.collidepoint(mouse) :
            self.random_card_name = "red_0"
            self.choosed_wild = False

        elif self.choosed_blue_rect.collidepoint(mouse) :
            self.random_card_name = "blue_0"
            self.choosed_wild = False

        elif self.choosed_green_rect.collidepoint(mouse) :
            self.random_card_name = "green_0"
            self.choosed_wild = False

        elif self.choosed_orange_rect.collidepoint(mouse) :
            self.random_card_name = "orange_0"
            self.choosed_wild = False

    def check_click(self, mouse):
        # Check if the user is looking for the previous cards
        if self.previous.collidepoint(mouse) :
            self.previous_seven = True
            self.next_seven = False

        # Check if the user is looking for the next cards
        elif self.next.collidepoint(mouse) :
            self.next_seven = True
            self.previous_seven = False

        # Check if the user is using the deck
        elif self.deck.collidepoint(mouse) :
            if self.current_turn_pick == False : # Checks if the user didn't pick a card on this turn yet
                self.pick_card()
                self.current_turn_pick = True

        # Check if the user colliderect with the next turn button
        elif self.next_turn_rect.collidepoint(mouse) :
            self.timer = 30
            self.next_turn()

        elif self.uno_rect.collidepoint(mouse):
            if self.player_one_turn :
                self.player_one_uno = True

            elif self.player_two_turn :
                self.player_two_uno = True

            else :
                self.player_three_uno = True



        elif self.card_one_rect.collidepoint(mouse) :
            if self.player_one_turn :
                if self.previous_seven :
                    if len(self.player_one_cards) >=1 :

                        isWild = False

                        # Assign the card
                        card_one = self.player_one_cards[0]
                        card_one_name = self.player_one_card_names[0]

                        if "wild" in card_one_name :
                            isWild = True
                            self.choosed_wild = True
                            self.choosed_color()


                        # Check if the card is compatible
                        isValid = self.check_deck_card_compatibility(card_one_name)

                        if isValid :

                            # Replace the card
                            self.random_card = card_one

                            if not isWild:
                                self.random_card_name = card_one_name

                            # Remove the card from the player
                            self.player_one_cards.remove(card_one)
                            self.player_one_card_names.remove(card_one_name)

                            # Draw card ?
                            if "draw" in card_one_name and "4" not in card_one_name :
                                self.draw_cards(2)

                            elif "draw" in card_one_name and "4" in card_one_name :
                                self.draw_cards(4)

                            # Next turn
                            if "skip" in card_one_name :
                                self.skip_turn()

                            elif "reverse" in card_one_name :
                                self.reverse_turn()

                            else :
                                self.next_turn()

                elif self.next_seven :
                    if len(self.player_one_cards) >=8 :

                        isWild = False

                        # Assign the card
                        card_one = self.player_one_cards[7]
                        card_one_name = self.player_one_card_names[7]

                        if "wild" in card_one_name :
                            isWild = True
                            self.choosed_wild = True
                            self.choosed_color()


                        # Check if the card is compatible
                        isValid = self.check_deck_card_compatibility(card_one_name)

                        if isValid :

                            # Replace the card
                            self.random_card = card_one

                            if not isWild:
                                self.random_card_name = card_one_name

                            # Remove the card from the player
                            self.player_one_cards.remove(card_one)
                            self.player_one_card_names.remove(card_one_name)

                            # Draw card ?
                            if "draw" in card_one_name and "4" not in card_one_name :
                                self.draw_cards(2)

                            elif "draw" in card_one_name and "4" in card_one_name :
                                self.draw_cards(4)

                            # Next turn
                            if "skip" in card_one_name :
                                self.skip_turn()

                            elif "reverse" in card_one_name :
                                self.reverse_turn()

                            else :
                                self.next_turn()

            elif self.player_two_turn :
                if self.previous_seven :
                    if len(self.player_two_cards) >=1 :

                        isWild  = False

                        # Assign the card
                        card_one = self.player_two_cards[0]
                        card_one_name = self.player_two_card_names[0]

                        if "wild" in card_one_name :
                            isWild= True
                            self.choosed_wild = True
                            self.choosed_color()


                        # Check if the card is compatible
                        isValid = self.check_deck_card_compatibility(card_one_name)

                        if isValid :

                            # Replace the card
                            self.random_card = card_one
                            if not isWild:
                                self.random_card_name = card_one_name

                            # Remove the card from the player
                            self.player_two_cards.remove(card_one)
                            self.player_two_card_names.remove(card_one_name)

                            # Draw card ?
                            if "draw" in card_one_name and "4" not in card_one_name :
                                self.draw_cards(2)

                            elif "draw" in card_one_name and "4" in card_one_name :
                                self.draw_cards(4)

                            # Next turn
                            if "skip" in card_one_name :
                                self.skip_turn()

                            elif "reverse" in card_one_name :
                                self.reverse_turn()

                            else :
                                self.next_turn()

                elif self.next_seven :
                    if len(self.player_two_cards) >=8 :
                        isWild = False
                        # Assign the card
                        card_one = self.player_two_cards[7]
                        card_one_name = self.player_two_card_names[7]

                        if "wild" in card_one_name :
                            isWild = True
                            self.choosed_wild = True
                            self.choosed_color()


                        # Check if the card is compatible
                        isValid = self.check_deck_card_compatibility(card_one_name)

                        if isValid :

                            # Replace the card
                            self.random_card = card_one
                            if not isWild:
                                self.random_card_name = card_one_name

                            # Remove the card from the player
                            self.player_two_cards.remove(card_one)
                            self.player_two_card_names.remove(card_one_name)

                            # Draw card ?
                            if "draw" in card_one_name and "4" not in card_one_name :
                                self.draw_cards(2)

                            elif "draw" in card_one_name and "4" in card_one_name :
                                self.draw_cards(4)

                            # Next turn
                            if "skip" in card_one_name :
                                self.skip_turn()

                            elif "reverse" in card_one_name :
                                self.reverse_turn()

                            else :
                                self.next_turn()

            elif self.player_three_turn :
                if self.previous_seven :
                    if len(self.player_three_cards) >=1 :
                        isWild = False

                        # Assign the card
                        card_one = self.player_three_cards[0]
                        card_one_name = self.player_three_card_names[0]

                        if "wild" in card_one_name :
                            isWild = True
                            self.choosed_wild = True
                            self.choosed_color()


                        # Check if the card is compatible
                        isValid = self.check_deck_card_compatibility(card_one_name)

                        if isValid :

                            # Replace the card
                            self.random_card = card_one
                            if not isWild:
                                self.random_card_name = card_one_name


                            # Remove the card from the player
                            self.player_three_cards.remove(card_one)
                            self.player_three_card_names.remove(card_one_name)

                            # Draw card ?
                            if "draw" in card_one_name and "4" not in card_one_name :
                                self.draw_cards(2)

                            elif "draw" in card_one_name and "4" in card_one_name :
                                self.draw_cards(4)


                            # Next turn
                            if "skip" in card_one_name :
                                self.skip_turn()

                            elif "reverse" in card_one_name :
                                self.reverse_turn()

                            else :
                                self.next_turn()

                elif self.next_seven :
                    if len(self.player_three_cards) >=8 :
                        # Assign the card

                        isWild = False

                        card_one = self.player_three_cards[7]
                        card_one_name = self.player_three_card_names[7]

                        if "wild" in card_one_name :
                            isWild = True
                            self.choosed_wild = True
                            self.choosed_color()


                        # Check if the card is compatible
                        isValid = self.check_deck_card_compatibility(card_one_name)

                        if isValid :

                            # Replace the card
                            self.random_card = card_one
                            if not isWild:
                                self.random_card_name = card_one_name

                            # Remove the card from the player
                            self.player_three_cards.remove(card_one)
                            self.player_three_card_names.remove(card_one_name)

                            # Draw card ?
                            if "draw" in card_one_name and "4" not in card_one_name :
                                self.draw_cards(2)

                            elif "draw" in card_one_name and "4" in card_one_name :
                                self.draw_cards(4)

                            # Next turn
                            if "skip" in card_one_name :
                                self.skip_turn()

                            elif "reverse" in card_one_name :
                                self.reverse_turn()

                            else :
                                self.next_turn()


        elif self.card_two_rect.collidepoint(mouse) :
            if self.player_one_turn :
                if self.previous_seven :
                    if len(self.player_one_cards) >=2 :

                        isWild = False

                        # Assign the card
                        card_two = self.player_one_cards[1]
                        card_two_name = self.player_one_card_names[1]

                        if "wild" in card_two_name :
                            isWild = True
                            self.choosed_wild = True
                            self.choosed_color()


                        # Check if the card is compatible
                        isValid = self.check_deck_card_compatibility(card_two_name)

                        if isValid :

                            # Replace the card
                            self.random_card = card_two

                            if not isWild:
                                self.random_card_name = card_two_name

                            # Remove the card from the player
                            self.player_one_cards.remove(card_two)
                            self.player_one_card_names.remove(card_two_name)

                            # Draw card ?
                            if "draw" in card_two_name and "4" not in card_two_name :
                                self.draw_cards(2)

                            elif "draw" in card_two_name and "4" in card_two_name :
                                self.draw_cards(4)

                            # Next turn
                            if "skip" in card_two_name :
                                self.skip_turn()

                            elif "reverse" in card_two_name :
                                self.reverse_turn()

                            else :
                                self.next_turn()

                elif self.next_seven :
                    if len(self.player_one_cards) >=9 :

                        isWild = False

                        # Assign the card
                        card_two = self.player_one_cards[8]
                        card_two_name = self.player_one_card_names[8]

                        if "wild" in card_two_name :
                            isWild = True
                            self.choosed_wild = True
                            self.choosed_color()


                        # Check if the card is compatible
                        isValid = self.check_deck_card_compatibility(card_two_name)

                        if isValid :

                            # Replace the card
                            self.random_card = card_two
                            if not isWild:
                                self.random_card_name = card_two_name

                            # Remove the card from the player
                            self.player_one_cards.remove(card_two)
                            self.player_one_card_names.remove(card_two_name)

                            # Draw card ?
                            if "draw" in card_two_name and "4" not in card_two_name :
                                self.draw_cards(2)

                            elif "draw" in card_two_name and "4" in card_two_name :
                                self.draw_cards(4)

                            # Next turn
                            if "skip" in card_two_name :
                                self.skip_turn()

                            elif "reverse" in card_two_name :
                                self.reverse_turn()

                            else :
                                self.next_turn()

            elif self.player_two_turn :
                if self.previous_seven :
                    if len(self.player_two_cards) >=2 :

                        isWild = False

                        # Assign the card
                        card_two = self.player_two_cards[1]
                        card_two_name = self.player_two_card_names[1]

                        if "wild" in card_two_name :
                            isWild = True
                            self.choosed_wild = True
                            self.choosed_color()


                        # Check if the card is compatible
                        isValid = self.check_deck_card_compatibility(card_two_name)

                        if isValid :

                            # Replace the card
                            self.random_card = card_two
                            if not isWild:
                                self.random_card_name = card_two_name

                            # Remove the card from the player
                            self.player_two_cards.remove(card_two)
                            self.player_two_card_names.remove(card_two_name)

                            # Draw card ?
                            if "draw" in card_two_name and "4" not in card_two_name :
                                self.draw_cards(2)

                            elif "draw" in card_two_name and "4" in card_two_name :
                                self.draw_cards(4)

                            # Next turn
                            if "skip" in card_two_name :
                                self.skip_turn()

                            elif "reverse" in card_two_name :
                                self.reverse_turn()

                            else :
                                self.next_turn()

                elif self.next_seven :
                    if len(self.player_two_cards) >=9 :

                        isWild = False

                        # Assign the card
                        card_two = self.player_two_cards[8]
                        card_two_name = self.player_two_card_names[8]

                        if "wild" in card_two_name :
                            isWild = True
                            self.choosed_wild = True
                            self.choosed_color()


                        # Check if the card is compatible
                        isValid = self.check_deck_card_compatibility(card_two_name)

                        if isValid :

                            # Replace the card
                            self.random_card = card_two
                            if not isWild:
                                self.random_card_name = card_two_name

                            # Remove the card from the player
                            self.player_two_cards.remove(card_two)
                            self.player_two_card_names.remove(card_two_name)

                            # Draw card ?
                            if "draw" in card_two_name and "4" not in card_two_name :
                                self.draw_cards(2)

                            elif "draw" in card_two_name and "4" in card_two_name :
                                self.draw_cards(4)

                            # Next turn
                            if "skip" in card_two_name :
                                self.skip_turn()

                            elif "reverse" in card_two_name :
                                self.reverse_turn()

                            else :
                                self.next_turn()

            elif self.player_three_turn :
                if self.previous_seven :
                    if len(self.player_three_cards) >=2 :
                        # Assign the card

                        isWild = False

                        card_two = self.player_three_cards[1]
                        card_two_name = self.player_three_card_names[1]

                        if "wild" in card_two_name :
                            isWild = True
                            self.choosed_wild = True
                            self.choosed_color()


                        # Check if the card is compatible
                        isValid = self.check_deck_card_compatibility(card_two_name)

                        if isValid :

                            # Replace the card
                            self.random_card = card_two
                            if not isWild: 
                                self.random_card_name = card_two_name

                            # Remove the card from the player
                            self.player_three_cards.remove(card_two)
                            self.player_three_card_names.remove(card_two_name)

                            # Draw card ?
                            if "draw" in card_two_name and "4" not in card_two_name :
                                self.draw_cards(2)

                            elif "draw" in card_two_name and "4" in card_two_name :
                                self.draw_cards(4)

                            # Next turn
                            if "skip" in card_two_name :
                                self.skip_turn()

                            elif "reverse" in card_two_name :
                                self.reverse_turn()

                            else :
                                self.next_turn()

                elif self.next_seven :
                    if len(self.player_three_cards) >=9 :

                        isWild = False

                        # Assign the card
                        card_two = self.player_three_cards[8]
                        card_two_name = self.player_three_card_names[8]

                        if "wild" in card_two_name :
                            isWild = True
                            self.choosed_wild = True
                            self.choosed_color()


                        # Check if the card is compatible
                        isValid = self.check_deck_card_compatibility(card_two_name)

                        if isValid :

                            # Replace the card
                            self.random_card = card_two
                            if not isWild:
                                self.random_card_name = card_two_name

                            # Remove the card from the player
                            self.player_three_cards.remove(card_two)
                            self.player_three_card_names.remove(card_two_name)

                            # Draw card ?
                            if "draw" in card_two_name and "4" not in card_two_name :
                                self.draw_cards(2)

                            elif "draw" in card_two_name and "4" in card_two_name :
                                self.draw_cards(4)

                            # Next turn
                            if "skip" in card_two_name :
                                self.skip_turn()

                            elif "reverse" in card_two_name :
                                self.reverse_turn()

                            else :
                                self.next_turn()

        elif self.card_three_rect.collidepoint(mouse) :
            if self.player_one_turn :
                if self.previous_seven :
                    if len(self.player_one_cards) >=3 :

                        isWild = False

                        # Assign the card
                        card_three = self.player_one_cards[2]
                        card_three_name = self.player_one_card_names[2]

                        if "wild" in card_three_name :
                            isWild = True
                            self.choosed_wild = True
                            self.choosed_color()


                        # Check if the card is compatible
                        isValid = self.check_deck_card_compatibility(card_three_name)

                        if isValid :

                            # Replace the card
                            self.random_card = card_three
                            if not isWild:
                                self.random_card_name = card_three_name

                            # Remove the card from the player
                            self.player_one_cards.remove(card_three)
                            self.player_one_card_names.remove(card_three_name)

                            # Draw card ?
                            if "draw" in card_three_name and "4" not in card_three_name :
                                self.draw_cards(2)

                            elif "draw" in card_three_name and "4" in card_three_name :
                                self.draw_cards(4)

                            # Next turn
                            if "skip" in card_three_name :
                                self.skip_turn()

                            elif "reverse" in card_three_name :
                                self.reverse_turn()

                            else :
                                self.next_turn()

                elif self.next_seven :
                    if len(self.player_one_cards) >=10 :

                        isWild = False

                        # Assign the card
                        card_three = self.player_one_cards[9]
                        card_three_name = self.player_one_card_names[9]

                        if "wild" in card_three_name :
                            isWild = True
                            self.choosed_wild = True
                            self.choosed_color()


                        # Check if the card is compatible
                        isValid = self.check_deck_card_compatibility(card_three_name)

                        if isValid :

                            # Replace the card
                            self.random_card = card_three
                            if not isWild:
                                self.random_card_name = card_three_name

                            # Remove the card from the player
                            self.player_one_cards.remove(card_three)
                            self.player_one_card_names.remove(card_three_name)

                            # Draw card ?
                            if "draw" in card_three_name and "4" not in card_three_name :
                                self.draw_cards(2)

                            elif "draw" in card_three_name and "4" in card_three_name :
                                self.draw_cards(4)

                            # Next turn
                            if "skip" in card_three_name :
                                self.skip_turn()

                            elif "reverse" in card_three_name :
                                self.reverse_turn()

                            else :
                                self.next_turn()

            elif self.player_two_turn :
                if self.previous_seven :
                    if len(self.player_two_cards) >=3 :

                        isWild = False

                        # Assign the card
                        card_three = self.player_two_cards[2]
                        card_three_name = self.player_two_card_names[2]

                        if "wild" in card_three_name :
                            isWild = True
                            self.choosed_wild = True
                            self.choosed_color()


                        # Check if the card is compatible
                        isValid = self.check_deck_card_compatibility(card_three_name)

                        if isValid :

                            # Replace the card
                            self.random_card = card_three
                            if not isWild:
                                self.random_card_name = card_three_name

                            # Remove the card from the player
                            self.player_two_cards.remove(card_three)
                            self.player_two_card_names.remove(card_three_name)

                            # Draw card ?
                            if "draw" in card_three_name and "4" not in card_three_name :
                                self.draw_cards(2)

                            elif "draw" in card_three_name and "4" in card_three_name :
                                self.draw_cards(4)

                            # Next turn
                            if "skip" in card_three_name :
                                self.skip_turn()

                            elif "reverse" in card_three_name :
                                self.reverse_turn()

                            else :
                                self.next_turn()

                elif self.next_seven :
                    if len(self.player_two_cards) >=10 :

                        isWild = False

                        # Assign the card
                        card_three = self.player_two_cards[9]
                        card_three_name = self.player_two_card_names[9]

                        if "wild" in card_three_name :
                            isWild = True
                            self.choosed_wild = True
                            self.choosed_color()


                        # Check if the card is compatible
                        isValid = self.check_deck_card_compatibility(card_three_name)

                        if isValid :

                            # Replace the card
                            self.random_card = card_three
                            if not isWild:
                                self.random_card_name = card_three_name

                            # Remove the card from the player
                            self.player_two_cards.remove(card_three)
                            self.player_two_card_names.remove(card_three_name)

                            # Draw card ?
                            if "draw" in card_three_name and "4" not in card_three_name :
                                self.draw_cards(2)

                            elif "draw" in card_three_name and "4" in card_three_name :
                                self.draw_cards(4)

                            # Next turn
                            if "skip" in card_three_name :
                                self.skip_turn()

                            elif "reverse" in card_three_name :
                                self.reverse_turn()

                            else :
                                self.next_turn()

            elif self.player_three_turn :
                if self.previous_seven :
                    if len(self.player_three_cards) >=3 :

                        isWild = False

                        # Assign the card
                        card_three = self.player_three_cards[2]
                        card_three_name = self.player_three_card_names[2]

                        if "wild" in card_three_name :
                            isWild = True
                            self.choosed_wild = True
                            self.choosed_color()


                        # Check if the card is compatible
                        isValid = self.check_deck_card_compatibility(card_three_name)

                        if isValid :

                            # Replace the card
                            self.random_card = card_three
                            if not isWild:
                                self.random_card_name = card_three_name

                            # Remove the card from the player
                            self.player_three_cards.remove(card_three)
                            self.player_three_card_names.remove(card_three_name)

                            # Draw card ?
                            if "draw" in card_three_name and "4" not in card_three_name :
                                self.draw_cards(2)

                            elif "draw" in card_three_name and "4" in card_three_name :
                                self.draw_cards(4)

                            # Next turn
                            if "skip" in card_three_name :
                                self.skip_turn()

                            elif "reverse" in card_three_name :
                                self.reverse_turn()

                            else :
                                self.next_turn()

                elif self.next_seven :
                    if len(self.player_three_cards) >=10 :

                        isWild = False

                        # Assign the card
                        card_three = self.player_three_cards[9]
                        card_three_name = self.player_three_card_names[9]

                        if "wild" in card_three_name :
                            isWild = True
                            self.choosed_wild = True
                            self.choosed_color()


                        # Check if the card is compatible
                        isValid = self.check_deck_card_compatibility(card_three_name)

                        if isValid :

                            # Replace the card
                            self.random_card = card_three
                            if not isWild:
                                self.random_card_name = card_three_name

                            # Remove the card from the player
                            self.player_three_cards.remove(card_three)
                            self.player_three_card_names.remove(card_three_name)

                            # Draw card ?
                            if "draw" in card_three_name and "4" not in card_three_name :
                                self.draw_cards(2)

                            elif "draw" in card_three_name and "4" in card_three_name :
                                self.draw_cards(4)

                            # Next turn
                            if "skip" in card_three_name :
                                self.skip_turn()

                            elif "reverse" in card_three_name :
                                self.reverse_turn()

                            else :
                                self.next_turn()

        elif self.card_four_rect.collidepoint(mouse) :
            if self.player_one_turn :
                if self.previous_seven :
                    if len(self.player_one_cards) >=4 :
                        # Assign the card

                        isWild = False

                        card_four = self.player_one_cards[3]
                        card_four_name =  self.player_one_card_names[3]

                        if "wild" in card_four_name :
                            isWild = True
                            self.choosed_wild = True
                            self.choosed_color()


                        # Check if the card is compatible
                        isValid = self.check_deck_card_compatibility(card_four_name)

                        if isValid :

                            # Replace the card
                            self.random_card = card_four
                            if not isWild:
                                self.random_card_name = card_four_name

                            # Remove the card from the player
                            self.player_one_cards.remove(card_four)
                            self.player_one_card_names.remove(card_four_name)

                            # Draw card ?
                            if "draw" in card_four_name and "4" not in card_four_name :
                                self.draw_cards(2)

                            elif "draw" in card_four_name and "4" in card_four_name :
                                self.draw_cards(4)

                            # Next turn
                            if "skip" in card_four_name :
                                self.skip_turn()

                            elif "reverse" in card_four_name :
                                self.reverse_turn()

                            else :
                                self.next_turn()

                elif self.next_seven :
                    if len(self.player_one_cards) >=11 :

                        isWild = False


                        # Assign the card
                        card_four = self.player_one_cards[10]
                        card_four_name = self.player_one_card_names[10]

                        if "wild" in card_four_name :
                            isWild = True
                            self.choosed_wild = True
                            self.choosed_color()


                        # Check if the card is compatible
                        isValid = self.check_deck_card_compatibility(card_four_name)

                        if isValid :

                            # Replace the card
                            self.random_card = card_four
                            if not isWild:
                                self.random_card_name = card_four_name

                            # Remove the card from the player
                            self.player_one_cards.remove(card_four)
                            self.player_one_card_names.remove(card_four_name)

                            # Draw card ?
                            if "draw" in card_four_name and "4" not in card_four_name :
                                self.draw_cards(2)

                            elif "draw" in card_four_name and "4" in card_four_name :
                                self.draw_cards(4)

                            # Next turn
                            if "skip" in card_four_name :
                                self.skip_turn()

                            elif "reverse" in card_four_name :
                                self.reverse_turn()

                            else :
                                self.next_turn()

            elif self.player_two_turn :
                if self.previous_seven :
                    if len(self.player_two_cards) >=4 :

                        isWild = False

                        # Assign the card
                        card_four = self.player_two_cards[3]
                        card_four_name = self.player_two_card_names[3]

                        if "wild" in card_four_name :
                            isWild = True
                            self.choosed_wild = True
                            self.choosed_color()


                        # Check if the card is compatible
                        isValid = self.check_deck_card_compatibility(card_four_name)

                        if isValid :

                            # Replace the card
                            self.random_card = card_four
                            if not isWild:
                                self.random_card_name = card_four_name

                            # Remove the card from the player
                            self.player_two_cards.remove(card_four)
                            self.player_two_card_names.remove(card_four_name)

                            # Draw card ?
                            if "draw" in card_four_name and "4" not in card_four_name :
                                self.draw_cards(2)

                            elif "draw" in card_four_name and "4" in card_four_name :
                                self.draw_cards(4)

                            # Next turn
                            if "skip" in card_four_name :
                                self.skip_turn()

                            elif "reverse" in card_four_name :
                                self.reverse_turn()

                            else :
                                self.next_turn()

                elif self.next_seven :
                    if len(self.player_two_cards) >=11 :

                        isWild = False

                        # Assign the card
                        card_four = self.player_two_cards[10]
                        card_four_name = self.player_two_card_names[10]

                        if "wild" in card_four_name :
                            isWild = True
                            self.choosed_wild = True
                            self.choosed_color()


                        # Check if the card is compatible
                        isValid = self.check_deck_card_compatibility(card_four_name)

                        if isValid :

                            # Replace the card
                            self.random_card = card_four
                            if not isWild:
                                self.random_card_name = card_four_name

                            # Remove the card from the player
                            self.player_two_cards.remove(card_four)
                            self.player_two_card_names.remove(card_four_name)

                            # Draw card ?
                            if "draw" in card_four_name and "4" not in card_four_name :
                                self.draw_cards(2)

                            elif "draw" in card_four_name and "4" in card_four_name :
                                self.draw_cards(4)

                            # Next turn
                            if "skip" in card_four_name :
                                self.skip_turn()

                            elif "reverse" in card_four_name :
                                self.reverse_turn()

                            else :
                                self.next_turn()

            elif self.player_three_turn :
                if self.previous_seven :
                    if len(self.player_three_cards) >=4 :

                        isWild = False

                        # Assign the card
                        card_four = self.player_three_cards[3]
                        card_four_name = self.player_three_card_names[3]

                        if "wild" in card_four_name :
                            isWild = True
                            self.choosed_wild = True
                            self.choosed_color()


                        # Check if the card is compatible
                        isValid = self.check_deck_card_compatibility(card_four_name)

                        if isValid :

                            # Replace the card
                            self.random_card = card_four
                            if not isWild:
                                self.random_card_name = card_four_name

                            # Remove the card from the player
                            self.player_three_cards.remove(card_four)
                            self.player_three_card_names.remove(card_four_name)

                            # Draw card ?
                            if "draw" in card_four_name and "4" not in card_four_name :
                                self.draw_cards(2)

                            elif "draw" in card_four_name and "4" in card_four_name :
                                self.draw_cards(4)

                            # Next turn
                            if "skip" in card_four_name :
                                self.skip_turn()

                            elif "reverse" in card_four_name :
                                self.reverse_turn()

                            else :
                                self.next_turn()

                elif self.next_seven :
                    if len(self.player_three_cards) >=11 :

                        isWild = False

                        # Assign the card
                        card_four = self.player_three_cards[10]
                        card_four_name = self.player_three_card_names[10]

                        if "wild" in card_four_name :
                            isWild = True
                            self.choosed_wild = True
                            self.choosed_color()


                        # Check if the card is compatible
                        isValid = self.check_deck_card_compatibility(card_four_name)

                        if isValid :

                            # Replace the card
                            self.random_card = card_four
                            if not isWild:
                                self.random_card_name = card_four_name

                            # Remove the card from the player
                            self.player_three_cards.remove(card_four)
                            self.player_three_card_names.remove(card_four_name)

                            # Draw card ?
                            if "draw" in card_four_name and "4" not in card_four_name :
                                self.draw_cards(2)

                            elif "draw" in card_four_name and "4" in card_four_name :
                                self.draw_cards(4)

                        # Next turn
                            if "skip" in card_four_name :
                                self.skip_turn()

                            elif "reverse" in card_four_name :
                                self.reverse_turn()

                            else :
                                self.next_turn()

        elif self.card_five_rect.collidepoint(mouse) :
            if self.player_one_turn :
                if self.previous_seven :
                    if len(self.player_one_cards) >=5 :

                        isWild = False

                        # Assign the card
                        card_five = self.player_one_cards[4]
                        card_five_name = self.player_one_card_names[4]

                        if "wild" in card_five_name :
                            isWild = True
                            self.choosed_wild = True
                            self.choosed_color()


                        # Check if the card is compatible
                        isValid = self.check_deck_card_compatibility(card_five_name)

                        if isValid :

                            # Replace the card
                            self.random_card = card_five
                            if not isWild:
                                self.random_card_name = card_five_name

                            # Remove the card from the player
                            self.player_one_cards.remove(card_five)
                            self.player_one_card_names.remove(card_five_name)

                            # Draw card ?
                            if "draw" in card_five_name and "4" not in card_five_name :
                                self.draw_cards(2)

                            elif "draw" in card_five_name and "4" in card_five_name :
                                self.draw_cards(4)

                            # Next turn
                            if "skip" in card_five_name :
                                self.skip_turn()

                            elif "reverse" in card_five_name :
                                self.reverse_turn()

                            else :
                                self.next_turn()

                elif self.next_seven :

                    if len(self.player_one_cards) >=12 :

                        isWild = False

                        # Assign the card
                        card_five = self.player_one_cards[11]
                        card_five_name = self.player_one_card_names[11]

                        if "wild" in card_five_name :
                            isWild = True
                            self.choosed_wild = True
                            self.choosed_color()


                        # Check if the card is compatible
                        isValid = self.check_deck_card_compatibility(card_five_name)

                        if isValid :

                            # Replace the card
                            self.random_card = card_five
                            if not isWild:
                                self.random_card_name = card_five_name

                            # Remove the card from the player
                            self.player_one_cards.remove(card_five)
                            self.player_one_card_names.remove(card_five_name)

                            # Draw card ?
                            if "draw" in card_five_name and "4" not in card_five_name :
                                self.draw_cards(2)

                            elif "draw" in card_five_name and "4" in card_five_name :
                                self.draw_cards(4)

                            # Next turn
                            if "skip" in card_five_name :
                                self.skip_turn()

                            elif "reverse" in card_five_name :
                                self.reverse_turn()

                            else :
                                self.next_turn()

            elif self.player_two_turn :
                if self.previous_seven :
                    if len(self.player_two_cards) >=5 :

                        isWild = False

                        # Assign the card
                        card_five = self.player_two_cards[4]
                        card_five_name = self.player_two_card_names[4]

                        if "wild" in card_five_name :
                            isWild = True
                            self.choosed_wild = True
                            self.choosed_color()


                        # Check if the card is compatible
                        isValid = self.check_deck_card_compatibility(card_five_name)

                        if isValid :

                            # Replace the card
                            self.random_card = card_five
                            if not isWild:
                                self.random_card_name = card_five_name

                            # Remove the card from the player
                            self.player_two_cards.remove(card_five)
                            self.player_two_card_names.remove(card_five_name)

                            # Draw card ?
                            if "draw" in card_five_name and "4" not in card_five_name :
                                self.draw_cards(2)

                            elif "draw" in card_five_name and "4" in card_five_name :
                                self.draw_cards(4)

                            # Next turn
                            if "skip" in card_five_name :
                                self.skip_turn()

                            elif "reverse" in card_five_name :
                                self.reverse_turn()

                            else :
                                self.next_turn()

                elif self.next_seven :
                    if len(self.player_two_cards) >=12 :

                        isWild = False

                        # Assign the card
                        card_five = self.player_two_cards[11]
                        card_five_name = self.player_two_card_names[11]

                        if "wild" in card_five_name :
                            isWild = True
                            self.choosed_wild = True
                            self.choosed_color()


                        # Check if the card is compatible
                        isValid = self.check_deck_card_compatibility(card_five_name)

                        if isValid :

                            # Replace the card
                            self.random_card = card_five
                            if not isWild:
                                self.random_card_name = card_five_name

                            # Remove the card from the player
                            self.player_two_cards.remove(card_five)
                            self.player_two_card_names.remove(card_five_name)

                            # Draw card ?
                            if "draw" in card_five_name and "4" not in card_five_name :
                                self.draw_cards(2)

                            elif "draw" in card_five_name and "4" in card_five_name :
                                self.draw_cards(4)

                            # Next turn
                            if "skip" in card_five_name :
                                self.skip_turn()

                            elif "reverse" in card_five_name :
                                self.reverse_turn()

                            else :
                                self.next_turn()

            elif self.player_three_turn :
                if self.previous_seven :

                    if len(self.player_three_cards) >=5 :

                        isWild = False

                        # Assign the card
                        card_five = self.player_three_cards[4]
                        card_five_name = self.player_three_card_names[4]

                        if "wild" in card_five_name :
                            isWild = True
                            self.choosed_wild = True
                            self.choosed_color()


                        # Check if the card is compatible
                        isValid = self.check_deck_card_compatibility(card_five_name)

                        if isValid :

                            # Replace the card
                            self.random_card = card_five
                            if not isWild:
                                self.random_card_name = card_five_name

                            # Remove the card from the player
                            self.player_three_cards.remove(card_five)
                            self.player_three_card_names.remove(card_five_name)

                            # Draw card ?
                            if "draw" in card_five_name and "4" not in card_five_name :
                                self.draw_cards(2)

                            elif "draw" in card_five_name and "4" in card_five_name :
                                self.draw_cards(4)

                            # Next turn
                            if "skip" in card_five_name :
                                self.skip_turn()

                            elif "reverse" in card_five_name :
                                self.reverse_turn()

                            else :
                                self.next_turn()

                elif self.next_seven :
                    if len(self.player_three_cards) >=12 :

                        isWild = False

                        # Assign the card
                        card_five = self.player_three_cards[11]
                        card_five_name = self.player_three_card_names[11]

                        if "wild" in card_five_name :
                            isWild = True
                            self.choosed_wild = True
                            self.choosed_color()


                        # Check if the card is compatible
                        isValid = self.check_deck_card_compatibility(card_five_name)

                        if isValid :

                            # Replace the card
                            self.random_card = card_five
                            if not isWild:
                                self.random_card_name = card_five_name

                            # Remove the card from the player
                            self.player_three_cards.remove(card_five)
                            self.player_three_card_names.remove(card_five_name)

                            # Draw card ?
                            if "draw" in card_five_name and "4" not in card_five_name :
                                self.draw_cards(2)

                            elif "draw" in card_five_name and "4" in card_five_name :
                                self.draw_cards(4)

                            # Next turn
                            if "skip" in card_five_name :
                                self.skip_turn()

                            elif "reverse" in card_five_name :
                                self.reverse_turn()

                            else :
                                self.next_turn()

        elif self.card_six_rect.collidepoint(mouse) :
            if self.player_one_turn :
                if self.previous_seven :

                    if len(self.player_one_cards) >=6 :

                        isWild = False

                        # Assign the card
                        card_six = self.player_one_cards[5]
                        card_six_name = self.player_one_card_names[5]

                        if "wild" in card_six_name :
                            isWild = True
                            self.choosed_wild = True
                            self.choosed_color()


                        # Check if the card is compatible
                        isValid = self.check_deck_card_compatibility(card_six_name)

                        if isValid :

                            # Replace the card
                            self.random_card = card_six
                            if not isWild:
                                self.random_card_name = card_six_name

                            # Remove the card from the player
                            self.player_one_cards.remove(card_six)
                            self.player_one_card_names.remove(card_six_name)

                            # Draw card ?
                            if "draw" in card_six_name and "4" not in card_six_name :
                                self.draw_cards(2)

                            elif "draw" in card_six_name and "4" in card_six_name :
                                self.draw_cards(4)

                            # Next turn
                            if "skip" in card_six_name :
                                self.skip_turn()

                            elif "reverse" in card_six_name :
                                self.reverse_turn()

                            else :
                                self.next_turn()

                elif self.next_seven :

                    if len(self.player_one_cards) >=13 :

                        isWild = False

                        # Assign the card
                        card_six = self.player_one_cards[12]
                        card_six_name = self.player_one_card_names[12]

                        if "wild" in card_six_name :
                            isWild = True
                            self.choosed_wild = True
                            self.choosed_color()


                        # Check if the card is compatible
                        isValid = self.check_deck_card_compatibility(card_six_name)

                        if isValid :

                            # Replace the card
                            self.random_card = card_six
                            if not isWild:
                                self.random_card_name = card_six_name

                            # Remove the card from the player
                            self.player_one_cards.remove(card_six)
                            self.player_one_card_names.remove(card_six_name)

                            # Draw card ?
                            if "draw" in card_six_name and "4" not in card_six_name :
                                self.draw_cards(2)

                            elif "draw" in card_six_name and "4" in card_six_name :
                                self.draw_cards(4)

                            # Next turn
                            if "skip" in card_six_name :
                                self.skip_turn()

                            elif "reverse" in card_six_name :
                                self.reverse_turn()

                            else :
                                self.next_turn()

            elif self.player_two_turn :
                if self.previous_seven :

                    if len(self.player_two_cards) >=6 :

                        isWild = False

                        # Assign the card
                        card_six = self.player_two_cards[5]
                        card_six_name = self.player_two_card_names[5]

                        if "wild" in card_six_name :
                            isWild = True
                            self.choosed_wild = True
                            self.choosed_color()


                        # Check if the card is compatible
                        isValid = self.check_deck_card_compatibility(card_six_name)

                        if isValid :

                            # Replace the card
                            self.random_card = card_six
                            if not isWild:
                                self.random_card_name = card_six_name

                            # Remove the card from the player
                            self.player_two_cards.remove(card_six)
                            self.player_two_card_names.remove(card_six_name)

                            # Draw card ?
                            if "draw" in card_six_name and "4" not in card_six_name :
                                self.draw_cards(2)

                            elif "draw" in card_six_name and "4" in card_six_name :
                                self.draw_cards(4)

                            # Next turn
                            if "skip" in card_six_name :
                                self.skip_turn()

                            elif "reverse" in card_six_name :
                                self.reverse_turn()

                            else :
                                self.next_turn()

                elif self.next_seven :

                    if len(self.player_two_cards) >=13 :

                        isWild = False

                        # Assign the card
                        card_six = self.player_two_cards[12]
                        card_six_name = self.player_two_card_names[12]

                        if "wild" in card_six_name :
                            isWild = True
                            self.choosed_wild = True
                            self.choosed_color()

                        # Check if the card is compatible
                        isValid = self.check_deck_card_compatibility(card_six_name)

                        if isValid :

                            # Replace the card
                            self.random_card = card_six
                            if not isWild:
                                self.random_card_name = card_six_name

                            # Remove the card from the player
                            self.player_two_cards.remove(card_six)
                            self.player_two_card_names.remove(card_six_name)

                            # Draw card ?
                            if "draw" in card_six_name and "4" not in card_six_name :
                                self.draw_cards(2)

                            elif "draw" in card_six_name and "4" in card_six_name :
                                self.draw_cards(4)

                            # Next turn
                            if "skip" in card_six_name :
                                self.skip_turn()

                            elif "reverse" in card_six_name :
                                self.reverse_turn()

                            else :
                                self.next_turn()

            elif self.player_three_turn :
                if self.previous_seven :

                    if len(self.player_three_cards) >=6 :

                        isWild = False

                        # Assign the card
                        card_six = self.player_three_cards[5]
                        card_six_name = self.player_three_card_names[5]

                        if "wild" in card_six_name :
                            isWild = True
                            self.choosed_wild = True
                            self.choosed_color()

                        # Check if the card is compatible
                        isValid = self.check_deck_card_compatibility(card_six_name)

                        if isValid :

                            # Replace the card
                            self.random_card = card_six
                            if not isWild:
                                self.random_card_name = card_six_name

                            # Remove the card from the player
                            self.player_three_cards.remove(card_six)
                            self.player_three_card_names.remove(card_six_name)

                            # Draw card ?
                            if "draw" in card_six_name and "4" not in card_six_name :
                                self.draw_cards(2)

                            elif "draw" in card_six_name and "4" in card_six_name :
                                self.draw_cards(4)

                            # Next turn
                            if "skip" in card_six_name :
                                self.skip_turn()

                            elif "reverse" in card_six_name :
                                self.reverse_turn()

                            else :
                                self.next_turn()

                elif self.next_seven :
                    if len(self.player_three_cards) >=13 :

                        isWild = False

                        # Assign the card
                        card_six = self.player_three_cards[12]
                        card_six_name = self.player_three_card_names[12]

                        if "wild" in card_six_name :
                            isWild = True
                            self.choosed_wild = True
                            self.choosed_color()

                        # Check if the card is compatible
                        isValid = self.check_deck_card_compatibility(card_six_name)

                        if isValid :

                            # Replace the card
                            self.random_card = card_six
                            if not isWild:
                                self.random_card_name = card_six_name

                            # Remove the card from the player
                            self.player_three_cards.remove(card_six)
                            self.player_three_card_names.remove(card_six_name)

                            # Draw card ?
                            if "draw" in card_six_name and "4" not in card_six_name :
                                self.draw_cards(2)

                            elif "draw" in card_six_name and "4" in card_six_name :
                                self.draw_cards(4)

                            # Next turn
                            if "skip" in card_six_name :
                                self.skip_turn()

                            elif "reverse" in card_six_name :
                                self.reverse_turn()

                            else :
                                self.next_turn()

        elif self.card_seven_rect.collidepoint(mouse) :
            if self.player_one_turn :
                if self.previous_seven :
                    if len(self.player_one_cards) >=7 :

                        isWild = False

                        # Assign the card
                        card_seven = self.player_one_cards[6]
                        card_seven_name = self.player_one_card_names[6]

                        if "wild" in card_seven_name :
                            isWild = True
                            self.choosed_wild = True
                            self.choosed_color()

                        # Check if the card is compatible
                        isValid = self.check_deck_card_compatibility(card_seven_name)

                        if isValid :

                            # Replace the card
                            self.random_card = card_seven
                            if not isWild:
                                self.random_card_name = card_seven_name

                            # Remove the card from the player
                            self.player_one_cards.remove(card_seven)
                            self.player_one_card_names.remove(card_seven_name)

                            # Draw card ?
                            if "draw" in card_seven_name and "4" not in card_seven_name :
                                self.draw_cards(2)

                            elif "draw" in card_seven_name and "4" in card_seven_name :
                                self.draw_cards(4)

                            # Next turn
                            if "skip" in card_seven_name :
                                self.skip_turn()

                            elif "reverse" in card_seven_name :
                                self.reverse_turn()

                            else :
                                self.next_turn()

                elif self.next_seven :
                    if len(self.player_one_cards) >=14 :

                        isWild = False

                        # Assign the card
                        card_seven = self.player_one_cards[13]
                        card_seven_name = self.player_one_card_names[13]

                        if "wild" in card_seven_name :
                            isWild = True
                            self.choosed_wild = True
                            self.choosed_color()

                        # Check if the card is compatible
                        isValid = self.check_deck_card_compatibility(card_seven_name)

                        if isValid :

                            # Replace the card
                            self.random_card = card_seven
                            if not isWild:
                                self.random_card_name = card_seven_name

                            # Remove the card from the player
                            self.player_one_cards.remove(card_seven)
                            self.player_one_card_names.remove(card_seven_name)

                            # Draw card ?
                            if "draw" in card_seven_name and "4" not in card_seven_name :
                                self.draw_cards(2)

                            elif "draw" in card_seven_name and "4" in card_seven_name :
                                self.draw_cards(4)

                            # Next turn
                            if "skip" in card_seven_name :
                                self.skip_turn()

                            elif "reverse" in card_seven_name :
                                self.reverse_turn()

                            else :
                                self.next_turn()

            elif self.player_two_turn :
                if self.previous_seven :
                    if len(self.player_two_cards) >=7 :

                        isWild = False

                        # Assign the card
                        card_seven = self.player_two_cards[6]
                        card_seven_name = self.player_two_card_names[6]

                        if "wild" in card_seven_name :
                            isWild = True
                            self.choosed_wild = True
                            self.choosed_color()

                        # Check if the card is compatible
                        isValid = self.check_deck_card_compatibility(card_seven_name)

                        if isValid :

                            # Replace the card
                            self.random_card = card_seven
                            if not isWild:
                                self.random_card_name = card_seven_name

                            # Remove the card from the player
                            self.player_two_cards.remove(card_seven)
                            self.player_two_card_names.remove(card_seven_name)

                            # Draw card ?
                            if "draw" in card_seven_name and "4" not in card_seven_name :
                                self.draw_cards(2)

                            elif "draw" in card_seven_name and "4" in card_seven_name :
                                self.draw_cards(4)

                            # Next turn
                            if "skip" in card_seven_name :
                                self.skip_turn()

                            elif "reverse" in card_seven_name :
                                self.reverse_turn()

                            else :
                                self.next_turn()

                elif self.next_seven :
                    if len(self.player_two_cards) >=14 :

                        isWild = False

                        # Assign the card
                        card_seven = self.player_two_cards[13]
                        card_seven_name = self.player_two_card_names[13]

                        if "wild" in card_seven_name :
                            isWild = True
                            self.choosed_wild = True
                            self.choosed_color()

                        # Check if the card is compatible
                        isValid = self.check_deck_card_compatibility(card_seven_name)

                        if isValid :

                            # Replace the card
                            self.random_card = card_seven
                            if not isWild:
                                self.random_card_name = card_seven_name

                            # Remove the card from the player
                            self.player_two_cards.remove(card_seven)
                            self.player_two_card_names.remove(card_seven_name)

                            # Draw card ?
                            if "draw" in card_seven_name and "4" not in card_seven_name :
                                self.draw_cards(2)

                            elif "draw" in card_seven_name and "4" in card_seven_name :
                                self.draw_cards(4)

                            # Next turn
                            if "skip" in card_seven_name :
                                self.skip_turn()

                            elif "reverse" in card_seven_name :
                                self.reverse_turn()

                            else :
                                self.next_turn()

            elif self.player_three_turn :
                if self.previous_seven :
                    if len(self.player_three_cards) >=7 :

                        isWild = False

                        # Assign the card
                        card_seven = self.player_three_cards[6]
                        card_seven_name = self.player_three_card_names[6]

                        if "wild" in card_seven_name :
                            isWild = True
                            self.choosed_wild = True
                            self.choosed_color()

                        # Check if the card is compatible
                        isValid = self.check_deck_card_compatibility(card_seven_name)

                        if isValid :

                            # Replace the card
                            self.random_card = card_seven
                            if not isWild:
                                self.random_card_name = card_seven_name

                            # Remove the card from the player
                            self.player_three_cards.remove(card_seven)
                            self.player_three_card_names.remove(card_seven_name)

                            # Draw card ?
                            if "draw" in card_seven_name and "4" not in card_seven_name :
                                self.draw_cards(2)

                            elif "draw" in card_seven_name and "4" in card_seven_name :
                                self.draw_cards(4)

                            # Next turn
                            if "skip" in card_seven_name :
                                self.skip_turn()

                            elif "reverse" in card_seven_name :
                                self.reverse_turn()

                            else :
                                self.next_turn()

                elif self.next_seven :
                    if len(self.player_three_cards) >=14 :

                        isWild = False

                        # Assign the card
                        card_seven = self.player_three_cards[13]
                        card_seven_name = self.player_three_card_names[13]

                        if "wild" in card_seven_name :
                            isWild = True
                            self.choosed_wild = True
                            self.choosed_color()

                        # Check if the card is compatible
                        isValid = self.check_deck_card_compatibility(card_seven_name)

                        if isValid :

                            # Replace the card
                            self.random_card = card_seven
                            if not isWild:
                                self.random_card_name = card_seven_name

                            # Remove the card from the player
                            self.player_three_cards.remove(card_seven)
                            self.player_three_card_names.remove(card_seven_name)

                            # Draw card ?
                            if "draw" in card_seven_name and "4" not in card_seven_name :
                                self.draw_cards(2)

                            elif "draw" in card_seven_name and "4" in card_seven_name :
                                self.draw_cards(4)

                            # Next turn
                            if "skip" in card_seven_name :
                                self.skip_turn()

                            elif "reverse" in card_seven_name :
                                self.reverse_turn()

                            else :
                                self.next_turn()


    def pick_card (self) :
        player_cards = self.current_player()

        # Search for a random card in deck
        random_card = randint(0, len(self.game_cards) - 1)

        # Assign the random number to a deck card
        random_card_name = self.game_cards_names[random_card]
        random_card = self.game_cards[random_card]
        

        # Delete the choosed card from the deck
        self.game_cards.remove(random_card)
        self.game_cards_names.remove(random_card_name)

        # Assign the card to the player
        player_cards[0].append(random_card)
        player_cards[1].append(random_card_name)

        self.available_card()


    def current_player (self) :

        player = self.player_one_cards
        player_cards = self.player_one_card_names

        if self.player_two_turn :
            player = self.player_two_cards
            player_cards = self.player_two_card_names

        elif self.player_three_turn :
            player = self.player_three_cards
            player_cards = self.player_three_card_names

        return player, player_cards

    def player_control(self) :

        while game_values["START"]["TURN"] == "NO" :

            for event in pygame.event.get() :
                # Closes the game
                if event.type == pygame.QUIT:
                    game_values["START"]["TURN"] = "YES"
                    silent_save_game()
                    self.running = False

                elif event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_m :
                        # Changes the mouse visibility
                        self.mouse_visible = not self.mouse_visible
                        pygame.mouse.set_visible(self.mouse_visible)

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.check_click(event.pos)

    def backward (self) :

        while game_values["START"]["TURN"] == "NO" :

            if self.player_one_turn :

                while self.choosed_wild :
                    self.screen.blit(colors, (350, 70))

                if self.timer > 0  :
                    time = count_font.render("Time : %d " % self.timer, 1, self.color)
                    self.timer_Screen.blit(time, (475, 20))
                    self.timer -=1
                    clock.tick(1)
                
                if self.timer == 0:
                    self.timer = 30
                    self.next_turn()

                if self.player_one_uno :
                    uno = self.font.render("UNO!", 1, self.color)
                    self.timer_Screen.blit(uno, (500, 400))
                    clock.tick(2)
                    self.player_one_uno = False
                    

            elif self.player_two_turn :

                while self.choosed_wild :
                    self.screen.blit(colors, (350, 70))

                if self.timer > 0  :
                    time = count_font.render("Time : %d " % self.timer, 1, self.color)
                    self.timer_Screen.blit(time, (475, 20))
                    self.timer -=1
                    clock.tick(2)
                
                if self.timer == 0:
                    self.timer = 30
                    self.next_turn()

                if self.player_two_uno :
                    uno = self.font.render("UNO!", 1, self.color)
                    self.timer_Screen.blit(uno, (500, 400))
                    clock.tick(1)
                    self.player_two_uno = False


            elif self.player_three_turn :

                while self.choosed_wild :
                    self.screen.blit(colors, (350, 70))


                if self.timer > 0  :
                    time = count_font.render("Time : %d " % self.timer, 1, self.color)
                    self.timer_Screen.blit(time, (475, 20))
                    self.timer -=1
                    clock.tick(1)
                
                if self.timer == 0:
                    self.timer = 30
                    self.next_turn()

                if self.player_three_uno :
                    uno = self.font.render("UNO!", 1, self.color)
                    self.timer_Screen.blit(uno, (500, 400))
                    clock.tick(2)
                    self.player_three_uno = False


    def draw_board(self) :

        while game_values["START"]["TURN"] == "NO" :

            self.screen.fill("#ee2229")
            
            cards = count_font.render("Available Cards : %d " % self.available_cards, 1, self.color)
            self.screen.blit(cards, (850, 20))
            
            self.screen.blit(cards_deck, (300, 75))
            card = pygame.transform.scale(self.random_card, (200, 300))
            self.screen.blit(card, (570, 75))
            self.screen.blit(uno_player, (800, 80))
            self.screen.blit(next_turn, (1020, 80))

            if self.player_one_turn :

                time = count_font.render("Time : %d " % self.timer, 1, self.color)
                self.timer_Screen.blit(time, (475, 20))

                player_one = self.font.render(self.player_one_name, 1, self.color)
                cards = count_font.render("Your Cards : %d " % len(self.player_one_cards), 1, self.color)
                self.screen.blit(cards, (850, 60))
                self.screen.blit(player_one, (50, 20))

            
                if self.next_seven :

                    width = 20
                    count = 0
                  
                    for card in self.player_one_cards :
                        if count >= 7 and count < 14 :
                            self.screen.blit(card, (50 + width , 400))
                            width +=150
                        count +=1

                elif self.previous_seven :

                    width = 20
                    count = 0

                    for card in self.player_one_cards :
                        if count < 7 :
                            self.screen.blit(card, (50 + width , 400))
                        count +=1
                        width +=150

                if self.player_one_uno :
                    uno = self.font.render("UNO!", 1, self.color)
                    self.timer_Screen.blit(uno, (500, 400))

                while self.choosed_wild :
                    self.screen.blit(colors, (350, 70))

                           

            elif self.player_two_turn :

                time = count_font.render("Time : %d " % self.timer, 1, self.color)
                self.timer_Screen.blit(time, (475, 20))

                player_two = self.font.render(self.player_two_name, 1, self.color)
                cards = count_font.render("Your Cards : %d " % len(self.player_two_cards), 1, self.color)
                self.screen.blit(cards, (850, 60))
                self.screen.blit(player_two, (50, 20))

            
                if self.next_seven :

                    width = 20
                    count = 0
                  
                    for card in self.player_two_cards :
                        if count >= 7 and count < 14 :
                            self.screen.blit(card, (50 + width , 400))
                            width +=150
                        count +=1


                elif self.previous_seven :

                    width = 20
                    count = 0

                    for card in self.player_two_cards :
                        if count < 7 :
                            self.screen.blit(card, (50 + width , 400))
                        count +=1
                        width +=150

                if self.player_two_uno :
                    uno = self.font.render("UNO!", 1, self.color)
                    self.timer_Screen.blit(uno, (500, 400))

                while self.choosed_wild :
                    self.screen.blit(colors, (350, 70))

            elif self.player_three_turn :

                time = count_font.render("Time : %d " % self.timer, 1, self.color)
                self.timer_Screen.blit(time, (475, 20))

                player_three = self.font.render(self.player_three_name, 1, self.color)
                cards = count_font.render("Your Cards : %d " % len(self.player_three_cards), 1, self.color)
                self.screen.blit(cards, (850, 60))
                self.screen.blit(player_three, (50, 20))

            
                if self.next_seven :

                    width = 20
                    count = 0
                  
                    for card in self.player_three_cards :
                        if count >= 7 and count < 14 :
                            self.screen.blit(card, (50 + width , 400))
                            width +=150
                        count +=1


                elif self.previous_seven :

                    width = 20
                    count = 0

                    for card in self.player_three_cards :
                        if count < 7 :
                            self.screen.blit(card, (50 + width , 400))
                        count +=1
                        width +=150

                if self.player_three_uno :
                    uno = self.font.render("UNO!", 1, self.color)
                    self.timer_Screen.blit(uno, (500, 400))

                while self.choosed_wild :
                    self.screen.blit(colors, (350, 70))

            # Controller
            #pygame.draw.rect(self.screen, self.color, self.next)
            self.screen.blit(next_cursor, (self.next.x, self.next.y))
            #pygame.draw.rect(self.screen, self.color, self.previous)
            self.screen.blit(previous_cursor, (self.previous.x, self.previous.y))
            #pygame.draw.rect(self.screen, self.color, self.deck)

            # Cards
            #pygame.draw.rect(self.screen, BLACK, self.card_one_rect)
            #pygame.draw.rect(self.screen, WHITE, self.card_two_rect)
            #pygame.draw.rect(self.screen, RED, self.card_three_rect)
            #pygame.draw.rect(self.screen, BLACK, self.card_four_rect)
            #pygame.draw.rect(self.screen, WHITE, self.card_five_rect)
            #pygame.draw.rect(self.screen, RED, self.card_six_rect)
            #pygame.draw.rect(self.screen, BLACK, self.card_seven_rect)

            # Next Turn
            #pygame.draw.rect(self.screen, self.color, self.next_turn_rect)

            pygame.display.flip()

    """

    def winner_screen (self, player_name) :
        player = self.font.render(player_name, 1, self.color)
        self.timer_Screen.blit(uno, (500, 400))
        clock.tick(5)


        pygame.display.update()
    """

    """
    def winner (self) :
        if self.player_one_name != '' :
            if self.player_one_cards == 0 :
                self.winner_screen(self.player_one_name)
                game_values["START"]["TURN"] = "YES"
                silent_save_game()

        elif self.player_two_name != '' :
            if self.player_two_cards  == 0 :
                self.winner_screen(self.player_two_name)
                game_values["START"]["TURN"] = "YES"
                silent_save_game()


        elif self.player_three_name != '' :
            if self.player_three_cards == 0 :
                self.winner_screen(self.player_three_name)
                game_values["START"]["TURN"] = "YES"
                silent_save_game()

    """


    def playing(self) :

        self.check_board_threads()

        if self.available_cards == 0 :
            self.available_card()
            self.assign_players()
            self.first_turn_cards_assign()
            self.assign_first_card()


        while self.running :


            t1 = threading.Thread(target = self.available_card, name="t1")
            t2 = threading.Thread(target = self.draw_board , name="t2")
            t3 = threading.Thread(target = self.player_control , name="t2")
            t4 = threading.Thread(target = self.backward , name="t2")
                
            t1.start()
            t2.start()
            t3.start()
            t4.start()

            start = self.player_control()
                

            while game_values["START"]["TURN"] == "NO":
                t1.join()
                t2.join()
                t3.join()
                t4.join()
            
        pygame.quit()
                

