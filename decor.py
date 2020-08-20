import os
import pygame


class Decor:

    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_image(self):
        return self.image

    def draw_decor(self, surface):
        """
            @modifies draw Character on the screen
        """
        img_path = os.path.join('images/decor', self.image)
        character_image = pygame.image.load(img_path).convert_alpha()
        surface.blit(character_image, (self.x, self.y))
