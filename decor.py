import os
import pygame


class Decor:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def draw_decor(self, icon_tile, surface, x, y):
        """
            @modifies draw Character on the screen
        """
        img_path = os.path.join('images/decor', icon_tile)
        character_image = pygame.image.load(img_path).convert_alpha()
        surface.blit(character_image, (x, y))
