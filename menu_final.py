import pygame, sys, random

# Pygame Setup
pygame.mixer.pre_init(44100, -16, 2, 512) 
pygame.init()
clock = pygame.time.Clock()

class Game():
    def __init__(self):
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.screen_width, self.screen_height = 1280, 960
        self.TITLE_W, self.TITLE_H = self.screen_width / 2, self.screen_height / 5
        self.display = pygame.Surface((self.screen_width, self.screen_height))
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.title_size = 80

        # Menu Variables
        self.main_menu = MainMenu(self)
        self.mods_menu = ModsMenu(self)
        self.curr_menu = self.main_menu

        # Mod Variables
        #self.arnold_mod = ArnoldMod()
        #self.tristan_mod = TristanMod()
        #self.jordan_mod = JordanMod()
        #self.bryce_mod = BryceMod()
        #self.christian_mod = ChristianMod()
        self.curr_mod = "none"

    def menu_loop(self):
        while self.playing:
            self.event_loop()
            if self.START_KEY:
                self.playing = False
            self.display.fill(self.BLACK)
            self.window.blit(self.display, (0, 0))
            pygame.display.update()
            self.reset()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
    
    def text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.TITLE_W, self.game.TITLE_H
        self.run_display = True
        self.cursor_rect = pygame.Rect (0, 0, 20, 20)
        self.offset = -200
    
    def make_cursor(self):
        self.game.text("*", 40, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.screen.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Play"
        self.playx, self.playy = self.mid_w, self.mid_h + 200
        self.modx, self.mody = self.mid_w, self.mid_h + 400
        self.exitx, self.exity = self.mid_w, self.mid_h + 600
        self.cursor_rect.midtop = (self.playx + self.offset, self.playy)

    def display(self):
        self.run = True
        while self.run:
            self.game.event_loop()
            self.inputs()
            self.game.display.fill(self.game.BLACK)
            self.game.text("Pong Game", self.game.title_size, self.game.TITLE_W, self.game.TITLE_H)
            self.game.text("Play", 60, self.playx, self.playy)
            self.game.text("Mods", 60, self.modx, self.mody)
            self.game.text("Exit", 60, self.exitx, self.exity)
            self.make_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == "Play":
                self.cursor_rect.midtop = (self.modx + self.offset, self.mody)
                self.state = "Mods"
            elif self.state == "Mods":
                self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                self.state = "Exit"
            elif self.state == "Exit":
                self.cursor_rect.midtop = (self.playx + self.offset, self.playy)
                self.state = "Play"
        elif self.game.UP_KEY:
            if self.state == "Play":
                self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                self.state = "Exit"
            elif self.state == "Mods":
                self.cursor_rect.midtop = (self.playx + self.offset, self.playy)
                self.state = "Play"
            elif self.state == "Exit":
                self.cursor_rect.midtop = (self.modx + self.offset, self.mody)
                self.state = "Mod"

    def inputs(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == "Play":
                play_pong()
            elif self.state == "Mods":
                self.game.curr_menu = self.game.mods_menu
            elif self.state == "Exit":
                pygame.quit()
                sys.exit()
            self.run = False

class ModsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Arnold Chi H"
        self.arnoldx, self.arnoldy = self.mid_w, self.mid_h + 120
        self.tristanx, self.tristany = self.mid_w, self.mid_h + 240
        self.jordanx, self.jordany = self.mid_w, self.mid_h + 360
        self.brycex, self.brycey = self.mid_w, self.mid_h + 480
        self.christianx, self.christiany = self.mid_w, self.mid_h + 600
        self.cursor_rect.midtop = (self.arnoldx + self.offset, self.arnoldy)
    
    def display(self):
        self.run = True
        while self.run:
            self.game.event_loop()
            self.inputs()
            self.game.display.fill(self.game.BLACK)
            self.game.text("Mods", self.game.title_size, self.game.TITLE_W, self.game.TITLE_H)
            self.game.text("Arnold Chi H", 40, self.arnoldx, self.arnoldy)
            self.game.text("Tristan M", 40, self.tristanx, self.tristany)
            self.game.text("Jordan D", 40, self.jordanx, self.jordany)
            self.game.text("Bryce B", 40, self.brycex, self.brycey)
            self.game.text("Christian B", 40, self.christianx, self.christiany)
            self.make_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == "Arnold Chi H":
                self.cursor_rect.midtop = (self.tristanx + self.offset, self.tristany)
                self.state = "Tristan M"
            elif self.state == "Tristan M":
                self.cursor_rect.midtop = (self.jordanx + self.offset, self.jordany)
                self.state = "Jordan D"
            elif self.state == "Jordan D":
                self.cursor_rect.midtop = (self.brycex + self.offset, self.brycey)
                self.state = "Bryce B"
            elif self.state == "Bryce B":
                self.cursor_rect.midtop = (self.christianx + self.offset, self.christiany)
                self.state = "Christian B"
            elif self.state == "Christian B":
                self.cursor_rect.midtop = (self.arnoldx + self.offset, self.arnoldy)
                self.state = "Arnold Chi H"
        elif self.game.UP_KEY:
            if self.state == "Arnold Chi H":
                self.cursor_rect.midtop = (self.christianx + self.offset, self.christiany)
                self.state = "Christian B"
            elif self.state == "Christian B":
                self.cursor_rect.midtop = (self.brycex + self.offset, self.brycey)
                self.state = "Bryce B"
            elif self.state == "Bryce B":
                self.cursor_rect.midtop = (self.jordanx + self.offset, self.jordany)
                self.state = "Jordan D"
            elif self.state == "Jordan D":
                self.cursor_rect.midtop = (self.tristanx + self.offset, self.tristany)
                self.state = "Tristan M"
            elif self.state == "Tristan M":
                self.cursor_rect.midtop = (self.arnoldx + self.offset, self.arnoldy)
                self.state = "Arnold Chi H"

    def inputs(self):
        self.move_cursor()
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run = False
        elif self.game.START_KEY:
            if self.state == "Arnold Chi H":
                self.game.curr_mod = self.game.arnold_mod
            elif self.state == "Tristan M":
                self.game.curr_mod = self.game.tristan_mod
            elif self.state == "Jordan D":
                self.game.curr_mod = self.game.jordan_mod
            elif self.state == "Bryce B":
                self.game.curr_mod = self.game.bryce_mod
            elif self.state == "Christian B":
                self.game.curr_mod = self.game.christian_mod
            self.run = False
            
    
def play_pong():
    
    # General setup
    pygame.mixer.pre_init(44100, -16, 2, 512) #resetting the sound buffer
    pygame.init()
    clock = pygame.time.Clock()

    # Main Window
    screen_width = 1280
    screen_height = 960
    screen = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption('Pong')

    # Colors
    light_grey = (200,200,200)
    bg_color = pygame.Color('grey12')

    # Game Rectangles
    ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
    player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10,140)
    opponent = pygame.Rect(10, screen_height / 2 - 70, 10,140)

    # Game Variables
    player_speed = 0
    opponent_speed = 7

    # Score Text
    player_score = 0
    opponent_score = 0
    basic_font = pygame.font.Font('freesansbold.ttf', 32)

    def ball_animation():
        ball_speed_x = 7 * random.choice((1,-1)) 
        ball_speed_y = 7 * random.choice((1,-1)) 

        ball.x += ball_speed_x
        ball.y += ball_speed_y

	    # Ball Collision (Top or Bottom)
        if ball.top <= 0 or ball.bottom >= screen_height:
            pygame.mixer.Sound.play(pong_sound) #play the pong sound
            ball_speed_y *= -1
	
	    # Player Scores
        if ball.left <= 0: 
            pygame.mixer.Sound.play(score_sound) #play the score sound
            player_score += 1 
            ball_restart() 

	    # Opponent Scores
        if ball.right >= screen_width:
            pygame.mixer.Sound.play(score_sound) #play the score sound
            opponent_score += 1 
            ball_restart() 

	    # Ball Collision (Player or Opponent)
        if ball.colliderect(player) or ball.colliderect(opponent):
            pygame.mixer.Sound.play(pong_sound) #play the pong sound
            ball_speed_x *= -1

    def player_animation():
	    player.y += player_speed

	    if player.top <= 0:
		    player.top = 0
	    if player.bottom >= screen_height:
		    player.bottom = screen_height

    def opponent_ai():
	    if opponent.top < ball.y:
		    opponent.y += opponent_speed
	    if opponent.bottom > ball.y:
		    opponent.y -= opponent_speed

	    if opponent.top <= 0:
		    opponent.top = 0
	    if opponent.bottom >= screen_height:
		    opponent.bottom = screen_height

    def ball_restart():
	    
        ball_speed_x = 7 * random.choice((1,-1)) 
        ball_speed_y = 7 * random.choice((1,-1)) 
	    # move ball to the center
        ball.center = (screen_width/2, screen_height/2)

	    # start the ball in a random direction
        ball_speed_y *= random.choice((1,-1)) 
        ball_speed_x *= random.choice((1,-1)) 

    # Sound
    pong_sound = pygame.mixer.Sound("./media/pong.ogg") #in the media folder
    score_sound = pygame.mixer.Sound("./media/score.ogg") #in the media folder
 

    while True:
	    for event in pygame.event.get():
		    if event.type == pygame.QUIT:
			    pygame.quit()
			    sys.exit()

		    if event.type == pygame.KEYDOWN:
			    if event.key == pygame.K_UP:
				    player_speed -= 6
			    if event.key == pygame.K_DOWN:
				    player_speed += 6
		    if event.type == pygame.KEYUP:
			    if event.key == pygame.K_UP:
				    player_speed += 6
			    if event.key == pygame.K_DOWN:
				    player_speed -= 6

	    ball_animation()
	    player_animation()
	    opponent_ai()

	    # Visuals 
	    screen.fill(bg_color)
	    pygame.draw.rect(screen, light_grey, player)
	    pygame.draw.rect(screen, light_grey, opponent)
	    pygame.draw.ellipse(screen, light_grey, ball)
	    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0),(screen_width / 2, screen_height))

	    # Creating the surface for text
	    player_text = basic_font.render(f'{player_score}',False,light_grey)
	    screen.blit(player_text,(660,470)) 

	    opponent_text = basic_font.render(f'{opponent_score}',False,light_grey)
	    screen.blit(opponent_text,(600,470)) 

	    # Loop Timer
	    pygame.display.flip()
	    clock.tick(60)

                



g = Game()

while g.running:
    g.curr_menu.display()
    g.menu_loop()