from character import *
from hero import *


def detect_collision(enemies, hero, weapon, coins, tiles):
    '''
        If the enemy is colliding with weapon, kill enemy and increase player score by 500
        If the enemy is colliding with player, remove 1 life from player
    '''
    # Sets up collision detection
    collision_weapon = []
    for enemy in enemies:
        # Associate True or False to each enemy depending on their collision status
        collision_weapon.append(Collision(enemy, weapon).get_colliding())

    collision_coins = []
    for coin in coins:
        # Associate True or False to each coin depending on their collision status
        collision_coins.append(Collision(hero, coin).get_colliding())

    collision_hero = False
    for enemy in enemies:
        # True if there is 1 enemy colliding with hero
        if Collision(enemy, hero).get_colliding():
            collision_hero = True
            break

    # Checks collisions
    activate_collision_enemies(enemies, collision_weapon, hero)
    activate_collision_coins(coins, collision_coins, hero)
    activate_collision_hero(collision_hero, hero)
    is_grounded(tiles, enemies)


def activate_collision_enemies(enemies, collision_weapon, hero):
    '''Tells if there is a collision between enemy and weapon'''
    for i, enemy in enumerate(enemies):
        if collision_weapon[i] and enemy.is_alive():
            enemy.kill_enemy()
            enemies.remove(enemy)
            hero.increase_score(100)


def activate_collision_coins(coins, collision_coins, hero):
    '''Tells if there is a collision between hero and coin'''
    for i, coin in enumerate(coins):
        if collision_coins[i]:
            coins.remove(coin)
            hero.increase_score(20)


def activate_collision_hero(collision_hero, hero):
    '''Tells if there is a collision between enemy and hero'''
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


def is_grounded(tiles, enemies):
    for enemy in enemies:
        for i, tile in enumerate(tiles):
            if Collision(enemy, tile).on_top_of():
                if tile.get_x() < enemy.get_min_x():
                    enemy.set_min_x(tile.get_x())
                if tile.get_x() > enemy.get_max_x():
                    enemy.set_max_x(tile.get_x())


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

    def on_top_of(self):
        delta_x = abs(self.x_1 - self.x_2)
        delta_y = abs(self.y_1 - self.y_2) - CHARACTER_SIZE + 10
        #
        # print('dx: ' + str(delta_x))
        # print('x enemy: ' + str(self.x_1))
        # print('x tile: ' + str(self.x_2))
        # print('---')
        # print('dy: ' + str(delta_x))

        #print('y enemy: ' + str(self.y_1))
        #print('y tile: ' + str(self.y_2))
        # print('---')
        if delta_x < (self.items_image_size - 1) and delta_y <= (self.items_image_size - 1):
            # print('y enemy: ' + str(self.y_1))
            # print('y tile: ' + str(self.y_2))
            # print('dy: ' + str(delta_y))
            return True
        else:
            #print('nop ' + str(delta_x) + ' , ' + str(delta_y))
            return False