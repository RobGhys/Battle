import pygame
from pygame.locals import *
from global_vars import WINDOW_WIDTH, WINDOW_HEIGHT, WHITE


def game_over(screen, background, score):
    # Font set-up
    font_size = 50
    end_game_font = pygame.font.Font('font.ttf', font_size)

    while True:
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            # Check if exit game
            if event.type == QUIT:
                quit()

        # Prepare game over message
        game_over_message = end_game_font.render('GAME OVER', True, WHITE)
        x_game_over = (WINDOW_WIDTH // 2) - 125
        y_game_over = (WINDOW_HEIGHT // 2) - 100
        screen.blit(game_over_message, (x_game_over, y_game_over))

        # Prepare score message
        game_over_message = end_game_font.render('Score: ' + str(score), True, WHITE)

        x_score = x_game_over + 10
        y_score = y_game_over + 100
        screen.blit(game_over_message, (x_score, y_score))

        pygame.display.update()
