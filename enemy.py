import pygame
import random

from constants import *
from character import *


"""
Describes the Enemies' characteristics 
Typical player has <{x, y}, alive> characteristics
"""
class Enemy(Character):

    ENEMY_SIZE_X = 55
    ENEMY_SIZE_Y = 65

    def __init__(self):
        self.x = random.randint(0, (WIDTH - self.ENEMY_SIZE_X))
        self.y = random.randint(0, (HEIGHT // 3))

    """
        @modifies self.x to self.x + dx
    """
    def move_x(self, dx):
        self.x += dx