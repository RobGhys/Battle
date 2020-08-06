from bullet import *

import random
import math
from character import *

"""
Describes the Bullet's characteristics 
Typical player has <{x, y}, alive> characteristics
"""


class Big_Bertha(Bullet):
    dy = 20
    player_size = 64
    min_x = (WIDTH // 2) - (2 * player_size)
    max_x = (WIDTH // 2) + (2 * player_size)

    def __init__(self, player):
        # Generates random position within [min_x, max_x]
        self.x = random.randint(self.min_x, self.max_x)
        self.y = player.get_y() - self.bullet_size_y
        self.state = self.possible_states[1]

    # Override
    def throw_bullet(self, event):
        if event.type == KEYDOWN:
            if event.key == K_x:
                # Activates fire mode 'on'
                self.state = self.possible_states[0]

