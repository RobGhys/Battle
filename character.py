import pygame

from constants import *


"""
Describes the Player's spaceship 
Typical player has <{x, y}, alive, score> characteristics
"""
class Character:

    def __init__(self):
        self.alive = True

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
        @modifies output
    """
    def draw_character(self, iconCharacter, surface):
        character_image = pygame.image.load(iconCharacter)
        surface.blit(character_image, (self.get_x(), self.get_y()))

