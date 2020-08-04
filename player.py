import pygame

from constants import *


"""
Describes the Player's spaceship 
Typical player has <{x, y}, alive, score> characteristics
"""
class Player:

    PLAYER_SIZE = 64 # Number of pixels in the image: 64x64

    def __init__(self):
        self.x = (WIDTH - self.PLAYER_SIZE) // 2
        self.y = HEIGHT - (self.PLAYER_SIZE * 2)
        self.alive = True
        self.score = 0

    """
        @returns self.x
    """
    def get_x(self):
        return self.x

    """
        @returns self.y
    """
    def get_y(self):
        return self.y

    """
        @modifies self.x to self.x + dx if self.getx() >= 0 and self.getx() <= (WIDTH - self.PLAYER_SIZE) \
        and teleports player to right-hand side or left-hand size
    """
    def move_x(self, dx):
        # Player goes from left-hand side to right-hand side
        if self.get_x() < 0:
            self.x = (WIDTH - self.PLAYER_SIZE)

        # Player goes from right-hand side to left-hand side
        elif self.get_x() > (WIDTH - self.PLAYER_SIZE):
            self.x = 0

        # Player moves by dx unit
        else:
            self.x += dx

    """
        @modifies output
    """
    def draw_player(self, iconPlayer, surface):
        player_image = pygame.image.load(iconPlayer)
        surface.blit(player_image, (self.get_x(), self.get_y()))

