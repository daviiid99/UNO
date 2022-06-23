from cards import *
from save_game import *
from board import *

vec = pygame.math.Vector2

def vec_to_int(vector):
    return int(vector.x), int(vector.y)

def reset_names () :
    game_values["PLAYER"]["1"] = "NONE"
    game_values["PLAYER"]["2"] = "NONE"
    game_values["PLAYER"]["3"] = "NONE"
    silent_save_game()


class Name :
    def __init__(self) :
        pygame.init()
        self.running = True
        self.screen = WIN
        self.rect = self.screen.get_rect()
        self.mouse = vec()
        self.mouse_visible = True
        self.clock = pygame.time.Clock()
        self.one_player = pygame.Rect(100, 350, 300, 200)
        self.two_player = pygame.Rect(500, 350, 300, 200)
        self.three_player = pygame.Rect(900, 350, 300, 200)
        self.color = pygame.Color('white')
        self.font = pygame.font.Font(None, 100)
        self.input_box = pygame.Rect(300, 400, 180, 100)
        self.active = False
        self.name = 1
        self.text = '  Type your name'
        self.player_one = 0
        self.player_two = 0
        self.player_three = 0



    def check_click(self, mouse):
        if self.one_player.collidepoint(mouse):
            print("1 jugador")

        elif self.two_player.collidepoint(mouse):
            print("2 jugadores")

        elif self.three_player.collidepoint(mouse):
            print("3 jugadores")

            #if pygame.mouse.get_pressed()[0]:

    def player_control(self) :

       if self.name > 0 :

            for event in pygame.event.get() :
                # Closes the game
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_box.collidepoint(event.pos):
                        self.text = ''

                        self.active = not self.active
                    else:
                        self.active = False

                if event.type == pygame.KEYDOWN:
                
                    if event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        self.text += event.unicode

                    if event.key == pygame.K_RETURN :
                            self.text = self.text[:-1]
                            if game_values["PLAYER"]["1"] == "NONE" :
                                game_values["PLAYER"]["1"] = self.text
                                self.name -=1
                                self.player_one = 0
                                silent_save_game()
                                self.text = 'Type your name'
                                enter = False

                            elif game_values["PLAYER"]["2"] == "NONE" :
                                game_values["PLAYER"]["2"] = self.text
                                self.name -=1
                                self.player_two = 0
                                silent_save_game()
                                self.text = 'Type your name'
                                enter = False

                            else :
                                game_values["PLAYER"]["3"] = self.text
                                self.name -=1
                                self.player_three = 0
                                silent_save_game()
                                self.text = 'Type your name'
                                enter = False

                            active = False


    def update_mouse_position(self, dt):
        self.mouse = vec(pygame.mouse.get_pos())


    def draw(self):
        self.screen.fill("#ee2229")
        self.screen.blit(logo, (500, 20))

        if self.player_one == 1 :
            self.name = self.player_one

        elif self.player_one == 0 and self.player_two == 2 :
            self.name = self.player_two

        else :
            self.name = self.player_three

        player = self.font.render('Player %d' % self.name, 1, self.color)
        WIN.blit(player, (480, 300) )

        self.input_box.w = width
        text = self.font.render(self.text, True, self.color)
        
        WIN.blit(text, (self.input_box.x+5, self.input_box.y+5))
        pygame.draw.rect(self.screen, self.color, self.input_box, 2)


        pygame.display.update()


    def select_name (self) :
        reset_names()
        number = game_values["PLAYERS"]
        self.name = number

        if self.name == 3 :
            self.player_one = 1
            self.player_two = 2
            self.player_three = 3

        elif self.name == 2 :
            self.player_one = 1
            self.player_two = 2

        else :
            self.player_one = 1

        while self.name > 0:
            delta_time = self.clock.tick() / 1000
            number = game_values["PLAYERS"]
            self.player_control()        
            self.update_mouse_position(delta_time)
            self.draw()

        if self.name == 0 :
            b = Board()
            b.playing()


    
        pygame.quit()
