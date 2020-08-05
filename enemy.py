import random
from character import *


"""
Describes the Enemies' characteristics 
Typical player has <{x, y}, alive> characteristics
"""
class Enemy(Character):

    enemy_size_x = 64
    enemy_size_y = 64
    dx = 3
    possible_dir = ('left', 'right')

    def __init__(self):
        self.x = random.randint(0, (WIDTH - self.enemy_size_x))
        self.y = random.randint(0, (HEIGHT // 3))
        self.direction = self.possible_dir[1]
        self.jump = False
        self.alive = True

    """
        @modifies   self.x_post = self.x + self.dx if self.direction is right,
                    else self.x_post = self.x - self.dx 
    """
    def move(self, player):
        if self.direction == self.possible_dir[1]:
            self.x += self.dx
        elif self.direction == self.possible_dir[0]:
            self.x -= self.dx

        # Check if enemy should not switch to a lower line
        self.launch_jump(player)

    """
        @modifies self.jump to True if enemy has reached game border
    """
    def check_jump_status(self):
        if self.x >= (WIDTH - self.enemy_size_x) or self.x <= 0:
            self.jump = True

    """
        @modifies   self.direction_post = right if jumping and self.direction = left,
                    or self.direction_post = left if jumping and self.direction = right
    """
    def reset_direction(self):
        if self.jump:
            if self.direction == self.possible_dir[1]:
                self.direction = self.possible_dir[0]
            else:
                self.direction = self.possible_dir[1]

    """
        @modifies self.y_post = self.y + enemy_size_y if jump is True
    """
    def launch_jump(self, player):
        self.check_jump_status()
        self.reset_direction()

        if self.jump and self.get_alive():
            # Checks if enemy is not in player base (= y position)
            if self.y < (player.get_y() - self.player_size):
                self.y += self.enemy_size_y
            else:
                # Kills enemy and hurts player
                self.set_alive(False)
                player.decrease_lives()
            self.jump = False

    """
        @returns self.alive
    """
    def get_alive(self):
        return self.alive

    """
        @modifies self.alive_post = alive
    """
    def set_alive(self, alive):
        self.alive = alive
