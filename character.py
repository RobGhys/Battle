import pygame
import os
from pygame.locals import *
from constants import *


"""
Describes the Player's spaceship 
Typical player has <{x, y}, alive, score> characteristics
"""
class Character:

    player_size = 64  # Number of pixels in the image: 64x64

    def __init__(self):
        self.x = 0
        self.y = 0

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
        @modifies draw Character on the screen
    """
    def draw_item(self, iconCharacter, surface):
        img_path = os.path.join('images', iconCharacter)
        character_image = pygame.image.load(img_path).convert_alpha()
        surface.blit(character_image, (self.get_x(), self.get_y()))