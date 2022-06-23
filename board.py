from cards import *
from random import randint
from save_game import *

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
        self.rect = self.screen.get_rect()
        self.mouse = vec()
        self.mouse_visible = True
        self.player_one_name = ''
        self.player_two_name = ''
        self.player_three_name = ''
        self.deck = pygame.Rect(340, 80, 160, 290)
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

        self.available_cards = 0

        self.player_one_cards = []
        self.player_two_cards = []
        self.player_three_cards = []
        self.player_one_turn = True
        self.player_two_turn = False
        self.player_three_turn = False
        self.card_witdh = 50
        self.card_height = 400
        self.random_card = self.game_cards[0] 
        self.card_one_rect = pygame.Rect(480, 350, 255, 290)
        self.next = pygame.Rect(1220, 550, 50, 50)
        self.previous = pygame.Rect(5, 550, 50, 50)
        self.current_turn_pick = False
        self.next_seven = False
        self.previous_seven = True

        self.card_one_rect = pygame.Rect(70, 400, 241, 361)
        self.card_two_rect = pygame.Rect(200, 400, 241, 361)
        self.card_three_rect = pygame.Rect(350, 400, 241, 361)
        self.card_four_rect = pygame.Rect(500, 400, 241, 361)
        self.card_five_rect = pygame.Rect(650, 400, 241, 361)
        self.card_six_rect = pygame.Rect(800, 400, 241, 361)
        self.card_seven_rect = pygame.Rect(950, 400, 241, 361)


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
        self.random_card = self.game_cards[random_card]
        self.game_cards.remove(self.random_card)

    def first_turn_cards_assign(self) :
        if self.player_one_name != '' :
            self.first_turn_cards_picks(self.player_one_cards)

        if self.player_two_name != '' :
            self.first_turn_cards_picks(self.player_two_cards)

        if self.player_three_name != '' :
            self.first_turn_cards_picks(self.player_three_cards)


    def first_turn_cards_picks (self, player) :
        # Max number of cards at start
        count = 7 

        while count > 0 :

            # Search for a random card
            carta = randint(0, len(self.game_cards) - 1)
            carta = self.game_cards[carta]

            # Remove the card from deck
            self.game_cards.remove(carta)

            # Assign the card to player cards
            player.append(carta)

            # Decrease the remaining cards counter
            count -=1

        self.available_cards -=7

    def check_click(self, mouse):
        # Check if the user is looking for the previous cards
        if self.previous.collidepoint(mouse) :
            self.previous_seven = True
            self.next_seven = False
            print("Retrocediendo")

        # Check if the user is looking for the next cards
        elif self.next.collidepoint(mouse) :
            self.next_seven = True
            self.previous_seven = False
            print("avanzando")

        # Check if the user is using the deck
        elif self.deck.collidepoint(mouse) :
            if self.current_turn_pick == False : # Checks if the user didn't pick a card on this turn yet
                self.pick_card()
                self.current_turn_pick = True

        elif self.card_one_rect.collidepoint(mouse) :
            print("Soy la carta uno")
            if self.player_one_turn :
                if self.previous_seven :
                    # Assign the card
                    card_one = self.player_one_cards[0]

                    # Replace the card
                    self.random_card = card_one

                    # Remove the card from the player
                    self.player_one_cards.remove(card_one)

                elif self.next_seven :
                    # Assign the card
                    card_one = self.player_one_cards[7]

                    # Replace the card
                    self.random_card = card_one

                    # Remove the card from the player
                    self.player_one_cards.remove(card_one)


        elif self.card_two_rect.collidepoint(mouse) :
            print("Soy la carta dos")

            if self.player_one_turn :
                if self.previous_seven :
                    # Assign the card
                    card_two = self.player_one_cards[1]

                    # Replace the card
                    self.random_card = card_two

                    # Remove the card from the player
                    self.player_one_cards.remove(card_two)

                elif self.next_seven :
                    # Assign the card
                    card_two = self.player_one_cards[8]

                    # Replace the card
                    self.random_card = card_two

                    # Remove the card from the player
                    self.player_one_cards.remove(card_two)

        elif self.card_three_rect.collidepoint(mouse) :
            print("Soy la carta tres")

            if self.player_one_turn :
                if self.previous_seven :
                    # Assign the card
                    card_three = self.player_one_cards[2]

                    # Replace the card
                    self.random_card = card_three

                    # Remove the card from the player
                    self.player_one_cards.remove(card_three)

                elif self.next_seven :
                    # Assign the card
                    card_three = self.player_one_cards[9]

                    # Replace the card
                    self.random_card = card_three

                    # Remove the card from the player
                    self.player_one_cards.remove(card_three)

        elif self.card_four_rect.collidepoint(mouse) :
            print("Soy la carta cuatro")

            if self.player_one_turn :
                if self.previous_seven :
                    # Assign the card
                    card_four = self.player_one_cards[3]

                    # Replace the card
                    self.random_card = card_four

                    # Remove the card from the player
                    self.player_one_cards.remove(card_four)

                elif self.next_seven :
                    # Assign the card
                    card_four = self.player_one_cards[10]

                    # Replace the card
                    self.random_card = card_four

                    # Remove the card from the player
                    self.player_one_cards.remove(card_four)

        elif self.card_five_rect.collidepoint(mouse) :
            print("Soy la carta cinco")

            if self.player_one_turn :
                if self.previous_seven :
                    # Assign the card
                    card_five = self.player_one_cards[4]

                    # Replace the card
                    self.random_card = card_five

                    # Remove the card from the player
                    self.player_one_cards.remove(card_five)

                elif self.next_seven :
                    # Assign the card
                    card_five = self.player_one_cards[11]

                    # Replace the card
                    self.random_card = card_five

                    # Remove the card from the player
                    self.player_one_cards.remove(card_five)

        elif self.card_six_rect.collidepoint(mouse) :
            print("Soy la carta seis")

            if self.player_one_turn :
                if self.previous_seven :
                    # Assign the card
                    card_six = self.player_one_cards[5]

                    # Replace the card
                    self.random_card = card_six

                    # Remove the card from the player
                    self.player_one_cards.remove(card_six)

                elif self.next_seven :
                    # Assign the card
                    card_six = self.player_one_cards[12]

                    # Replace the card
                    self.random_card = card_six

                    # Remove the card from the player
                    self.player_one_cards.remove(card_six)

        elif self.card_seven_rect.collidepoint(mouse) :
            print("Soy la carta siete")

            if self.player_one_turn :
                if self.previous_seven :
                    # Assign the card
                    card_seven = self.player_one_cards[6]

                    # Replace the card
                    self.random_card = card_seven

                    # Remove the card from the player
                    self.player_one_cards.remove(card_seven)

                elif self.next_seven :
                    # Assign the card
                    card_seven = self.player_one_cards[13]

                    # Replace the card
                    self.random_card = card_seven

                    # Remove the card from the player
                    self.player_one_cards.remove(card_seven)


    def pick_card (self) :
        player = self.current_player()

        # Search for a random card in deck
        random_card = randint(0, len(self.game_cards) - 1)

        # Assign the random number to a deck card
        random_card = self.game_cards[random_card]

        # Delete the choosed card from the deck
        self.game_cards.remove(random_card)

        # Assign the card to the player
        player.append(random_card)


    def current_player (self) :

        player = self.player_one_cards

        if self.player_two_turn :
            player = self.player_two_cards

        elif self.player_three_turn :
            player = self.player_three_cards

        return player

    def player_control(self) :

        for event in pygame.event.get() :
            # Closes the game
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN :
                if event.key == pygame.K_m :
                    # Changes the mouse visibility
                    self.mouse_visible = not self.mouse_visible
                    pygame.mouse.set_visible(self.mouse_visible)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.check_click(event.pos)


    def draw_board(self) :

        self.screen.fill("#ee2229")
        
        cards = count_font.render("Available Cards : %d " % self.available_cards, 1, self.color)
        self.screen.blit(cards, (850, 20))
        
        self.screen.blit(cards_deck, (260, 50))
        card = pygame.transform.scale(self.random_card, (200, 300))
        self.screen.blit(card, (570, 75))

        if self.player_one_turn :

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
                       

        elif self.player_two_turn :

            player_two = self.font.render(self.player_two_name, 1, self.color)
            self.screen.blit(player_one, (800, 20))

            for card in self.player_two_cards :
                self.card_witdh +=50
                self.screen.blit(card, (self.card_witdh, self.card_height) )

        elif self.player_three_turn :

            player_three = self.font.render(self.player_three_name, 1, self.color)
            self.screen.blit(player_three, (50, 500))

            for card in self.player_three_cards :
                self.card_witdh +=50
                self.screen.blit(card, (self.card_witdh, self.card_height) )

        # Controller
        #pygame.draw.rect(self.screen, self.color, self.next)
        self.screen.blit(next_cursor, (self.next.x, self.next.y))
        #pygame.draw.rect(self.screen, self.color, self.previous)
        self.screen.blit(previous_cursor, (self.previous.x, self.previous.y))
        #pygame.draw.rect(self.screen, self.color, self.deck)

        # Cards
        #pygame.draw.rect(self.screen, self.color, self.card_one_rect)
        #pygame.draw.rect(self.screen, self.color, self.card_two_rect)
        #pygame.draw.rect(self.screen, self.color, self.card_three_rect)
        #pygame.draw.rect(self.screen, self.color, self.card_four_rect)
        #pygame.draw.rect(self.screen, self.color, self.card_five_rect)
        #pygame.draw.rect(self.screen, self.color, self.card_six_rect)
        #pygame.draw.rect(self.screen, self.color, self.card_seven_rect)

        pygame.display.update()


    def playing(self) :
        while self.running :
            if self.available_cards == 0 :
                self.available_card()
                self.assign_players()
                self.first_turn_cards_assign()
                self.assign_first_card()


            elif self.available_cards > 0 :
                #self.pick_card()
                self.available_card()
                self.draw_board()
                self.player_control()

        pygame.quit()
                

