import sys
import os
from pygame.locals import *

from player import *
from enemy import *
from bullet import *


"""
    @returns pygame image object from image name
    (uses os conversion)
"""
def set_import_image(imageName):
    img_path = os.path.join('images', imageName)
    return pygame.image.load(img_path).convert()


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
    set_window("Space Invaders", os.path.join('images', 'ufo.png'))
    player = Player() # Initializes player class
    enemy = Enemy() # Initializes enemy class
    bullet = Bullet(player)

    while True:
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            # Check if exit game
            if event.type == QUIT:
                quit()
            # Player action
            dx = move_player(event) # Record key that was hit
            bullet.throw_bullet(event)

        # Characters movement
        player.move_x(dx) # Uses dx to move player
        enemy.move(player)
        bullet.move()


        # Draw player, enemy, bullet, and score
        player.draw_item('player2.png', screen)
        if enemy.get_alive():
            enemy.draw_item('alien2.png', screen)
        if bullet.get_state() == 'on':
            bullet.draw_item('bullet.png', screen)
        player.display_score(screen, game_font)


        # Update display
        pygame.display.update()


if __name__ == '__main__':
    # Init pygame
    pygame.init()

    # Create game screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    background = set_import_image('background.png')
    game_font = pygame.font.Font('font.ttf', 25)

    # Launches game
    game()