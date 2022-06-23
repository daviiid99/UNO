from cards import *
from player_name import *

vec = pygame.math.Vector2

def vec_to_int(vector):
    return int(vector.x), int(vector.y)
 

class Player :
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

    def check_click(self, mouse):
        if self.one_player.collidepoint(mouse):
            game_values["PLAYERS"] = 1
            silent_save_game()
            n = Name()
            n.select_name()

        elif self.two_player.collidepoint(mouse):
            game_values["PLAYERS"] = 2
            silent_save_game()
            n = Name()
            n.select_name()

        elif self.three_player.collidepoint(mouse):
            game_values["PLAYERS"] = 3
            silent_save_game()
            n = Name()
            n.select_name()

            #if pygame.mouse.get_pressed()[0]:
            

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



    def update_mouse_position(self, dt):
        self.mouse = vec(pygame.mouse.get_pos())


    def draw(self):
        self.screen.fill("#ee2229")
        self.screen.blit(logo, (500, 20))

        # 1 Player Rect
        #pygame.draw.rect(WIN, BLACK, self.one_player)
        WIN.blit(player_1, (self.one_player.x, self.one_player.y))

        # 2 Player Rect
        #pygame.draw.rect(WIN, BLACK, self.two_player)
        WIN.blit(player_2, (self.two_player.x, self.two_player.y))

         # 3 Player Rect
        #pygame.draw.rect(WIN, BLACK, self.three_player)
        WIN.blit(player_3, (self.three_player.x, self.three_player.y))

        pygame.display.update()


    def select_players (self) :
        while self.running:
            theme.play()
            delta_time = self.clock.tick() / 1000
            self.player_control()        
            self.update_mouse_position(delta_time)
            self.draw()
        pygame.quit()




 



