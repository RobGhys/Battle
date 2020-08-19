import pygame
from pygame.locals import *
from global_vars import WINDOW_WIDTH, WINDOW_HEIGHT, WHITE


def start(screen, background):
    # Font set-up
    font_size = 50
    end_game_font = pygame.font.Font('font.ttf', font_size)
    loop_menu = True

    while loop_menu:
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            # Check if exit game
            if event.type == QUIT:
                quit()
            loop_menu = key_hit(event)

        # Prepare game over message
        game_over_message = end_game_font.render('PRESS KEY', True, WHITE)
        x_game_over = (WINDOW_WIDTH // 2) - 125
        y_game_over = (WINDOW_HEIGHT // 2) - 100
        screen.blit(game_over_message, (x_game_over, y_game_over))

        pygame.display.update()


def key_hit(event):
    if event.type == KEYDOWN:
        if event.key == K_SPACE:
            return False
    else:
        return True
