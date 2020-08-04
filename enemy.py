import pygame
import random

from constants import *


"""
Describes the Enemies' characteristics 
Typical player has <{x, y}, alive> characteristics
"""
class Enemy:

    ENEMY_SIZE_X = 55
    ENEMY_SIZE_Y = 65

    def __init__(self):
        self.x = random.randint(0, (WIDTH - self.ENEMY_SIZE_X))
        self.y = random.randint(0, (HEIGHT // 3))
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
        @modifies self.x to self.x + dx
    """
    def move_x(self, dx):
        self.x += dx

    """
        @modifies output
    """
    def draw_enemy(self, iconEnemy, surface):
        enemy_image = pygame.image.load(iconEnemy)
        surface.blit(enemy_image, (self.get_x(), self.get_y()))

