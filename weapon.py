import pygame
from hero import *
from global_vars import BULLETCOLOR
from global_vars import WINDOW_WIDTH


class Weapon(Character):
    def __init__(self):
        self.x = -1
        self.y = -1
        self.fire_on = False
        self.facing = 1
        self.vel = 5 * self.facing
        self.dist_since_fire = 0

    def fix_position(self, x, y):
        self.x = x
        self.y = y

    def draw_item(self, icon_character, surface, x, y):
        """
            @modifies draw Character on the screen
        """
        img_path = os.path.join('images/decor', icon_character)
        character_image = pygame.image.load(img_path).convert_alpha()
        surface.blit(character_image, (x, y))

    def draw(self, screen):
        self.draw_item('flame.png', screen, self.x, self.y)

    def set_facing(self, facing):
        self.facing = facing

    def get_fire_on_status(self):
        return self.fire_on

    def set_fire_on_status(self, state):
        self.fire_on = state

    def get_vel(self):
        return self.vel

    def move_x(self):
        '''The bullet will travel 1/5 of map's width, then stop.'''
        if self.dist_since_fire < (WINDOW_WIDTH // 5):
            self.x += self.vel * self.facing
            self.dist_since_fire += self.vel
        else:
            # Reset status to stand still
            self.fire_on = False
            self.dist_since_fire = 0
