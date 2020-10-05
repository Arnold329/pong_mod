import pygame, sys, random, pygame.freetype, pygame.font
pygame.init()
clock = pygame.time.Clock()

#Game Window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("pong")

# Colors
light_grey = (200,200,200)
bg_color = pygame.Color('grey12')
black = (255,255,255)
white = (0,0,0)
font = pygame.freetype.SysFont('Times New Roman', 30)

#Button Class

def button(height, width, x, y, color, text):
    button = pygame.Rect(x, y, height, width)
    menu_button = pygame.draw.rect(screen, black, button)
    button_text = font.render(text, False, white)
    screen.blit(button_text, menu_button)
    pygame.display.update()
    return menu_button

button1 = button(200, 200, 150, 200, black, "hello")

while True:
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        if button1.collidepoint(mouse_x, mouse_y):
            pygame.exit()
            sys.exit()