from character import *
from hero import *


def detect_collision(enemy, hero, weapon):
    '''
        If the enemy is colliding with weapon, kill enemy and increase player score by 500
        If the enemy is colliding with player, remove 1 life from player
    '''
    # Sets up collision detection
    collision_weapon = Collision(enemy, weapon).get_colliding()
    collision_hero = Collision(enemy, hero).get_colliding()

    # Checks collision between enemy and weapon
    if collision_weapon and enemy.is_alive():
        enemy.kill_enemy()
        hero.increase_score(500)

    # Checks collision between enemy and hero
    if collision_hero:
        # If hero has 3 lives and is hit, remove 1 life directly
        if hero.get_lives() == 3:
            hero.decrease_lives()
        # If hero has 2 or 1 lives, we give him some time buffer
        # to move away from the enemy and not lose all his lives directly
        else:
            hero.increase_life_time_lapse()
            # Change the time buffer to give the hero more or less time to run away
            time_buffer = 25
            if hero.get_lifetime_lapse() >= time_buffer:
                hero.reset_life_time_lapse()
                hero.decrease_lives()


class Collision(object):

    items_image_size = 32

    def __init__(self, character_1, character_2):
        self.colliding = False
        self.x_1 = character_1.get_x()
        self.x_2 = character_2.get_x()
        self.y_1 = character_1.get_y()
        self.y_2 = character_2.get_y()

    def get_colliding(self):
        square_dist_x = (self.x_1 - self.x_2) ** 2
        square_dist_y = (self.y_1 - self.y_2) ** 2
        distance = math.sqrt(square_dist_x + square_dist_y)

        if distance <= self.items_image_size:
            return True
        else:
            return False

