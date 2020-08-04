import sys
from pygame.locals import *

from player import *
from enemy import *

#Init pygame
pygame.init()

#Create game screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load('background.png')

"""
    Shows Title & icon
    @requires: title is String
    @requires: icon is a .png file
    @modifies: out
"""
def set_window(title, iconScreen):
    pygame.display.set_caption(title)
    icon = pygame.image.load(iconScreen)
    pygame.display.set_icon(icon)
    screen.fill(BLACK)  # Fills screen with black


"""
    @requires event != null && event a keyboard input
    @returns dx, derivative of x
"""
def move_player(event):
    dx = 0 #initialization is necessary

    # Key pressed
    if event.type == KEYDOWN:
        if event.key == K_RIGHT:
            dx = 2.5
        if event.key == K_LEFT:
            dx = -2.5

    # Key released
    if event.type == KEYUP:
        if event.key == K_RIGHT or event.key == K_LEFT:
            dx = 0

    return dx


"""
    Quits game
"""
def quit():
    pygame.quit()
    sys.exit()


"""
    Game Loop
"""
def game():
    set_window("Space Invaders", 'ufo.png')
    player = Player() # Initializes player class
    enemy = Enemy() # Initializes enemy class

    while True:
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            # Check if exit game
            if event.type == QUIT:
                quit()
            dx = move_player(event) # Record key that was hit

        player.move_x(dx) # Uses dx to move player

        player.draw_player('player.png', screen)
        enemy.draw_enemy('enemy.png', screen)
        pygame.display.update()


if __name__ == '__main__':
    game()