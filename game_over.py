import pygame
from pygame.locals import *
from global_vars import WINDOW_WIDTH, WINDOW_HEIGHT, WHITE
from scores import get_high_score


def game_over_screen(screen, background, score):
    # Font set-up
    end_game_font = pygame.font.Font('font.ttf', 50)
    scores_font = pygame.font.Font('font.ttf', 30)

    while True:
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            # Check if exit game
            if event.type == QUIT:
                quit()
        x_y_coord = game_over_text(end_game_font, screen)
        scores_text(scores_font, score, screen, x_y_coord)
        pygame.display.update()


def game_over_text(end_game_font, screen):
    # Prepare game over message
    game_over_message = end_game_font.render('GAME OVER', True, WHITE)
    # Tuple containing x, y coordinates
    position = ((WINDOW_WIDTH // 2) - 125, (WINDOW_HEIGHT // 2) - 100)

    # Display game over message
    screen.blit(game_over_message, position)

    return position


def scores_text(scores_font, score, screen, x_y_coord):
    highest_score = get_high_score(score, 'scores.txt')
    line_spacing = 50

    # Choose between first or second highest score message
    if score >= highest_score:
        highest_score_message = scores_font.render('New Highest Score!', True, WHITE)
    else:
        highest_score_message = scores_font.render('Highest Score: ' + str(highest_score), True, WHITE)

    # Score message
    score_message = scores_font.render('Score: ' + str(score), True, WHITE)

    # Defines where to display messages (x, y)
    position_score_msg = (x_y_coord[0] + 50, x_y_coord[1] + line_spacing * 1.5 )
    position_highest_score_msg = (position_score_msg[0] - 50, position_score_msg[1] + line_spacing)

    # Display score messages
    screen.blit(score_message, position_score_msg)
    screen.blit(highest_score_message, position_highest_score_msg)