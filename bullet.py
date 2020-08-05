import random
from character import *


"""
Describes the Bullet's characteristics 
Typical player has <{x, y}, alive> characteristics
"""
class Bullet(Character):

    bullet_size_x = 32
    bullet_size_y = 32
    dy = 5
    possible_states = ('on', 'off')

    def __init__(self, player):
        self.x = player.get_x()
        self.y = player.get_y() - self.bullet_size_y
        self.state = self.possible_states[1]


    """
        @returns self.state
    """
    def get_state(self):
        return self.state


    """
        @modifies self.state to 'on' if space bar was pressed
    """
    def throw_bullet(self, event):
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                # Activates fire mode 'on'
                self.state = self.possible_states[0]


    """
        @modifies self.y_post to self.y - self.dy if self.y >=0 and self.state is 'on'
        else resets self.x and self.y to initial values, and sets states to 'off'   
    """
    def move(self, player):
        if self.y >= 0 and self.state == 'on':
            self.y -= self.dy
        else:
            # Resets x, y, and state
            self.x = player.get_x()
            self.y = player.get_y() - self.bullet_size_y
            self.state = self.possible_states[1]



