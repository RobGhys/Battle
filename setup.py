import os
import pygame
from global_vars import BACKGROUNDBLUE, WINDOW_HEIGHT, TILE_SIZE, NB_TILES_TO_FILL_SCREEN
from decor import *


def set_import_image(image_name):
    """
        @returns pygame image object from image name
        (uses os conversion)
    """
    img_path = os.path.join('images', image_name)
    return pygame.image.load(img_path).convert()


def set_window(title, icon_screen, screen):
    """
        Shows Title & icon
        @requires: title is String
        @requires: icon is a .png file
        @modifies: out
    """
    pygame.display.set_caption(title)
    icon = pygame.image.load(icon_screen)
    pygame.display.set_icon(icon)
    screen.fill(BACKGROUNDBLUE)  # Fills screen with light blue


def set_root_tiles():
    root_tile = []

    tile_x = 0 # Starting position x
    tile_y = WINDOW_HEIGHT - TILE_SIZE # Y position is constant
    nb_box_level = 2

    for i in range(nb_box_level):
        for tile in range(NB_TILES_TO_FILL_SCREEN):
            root_tile.append(Decor(tile_x, tile_y))
            # Increase x so that we draw further tiles
            tile_x += TILE_SIZE
        # Resets x and y position for the outer loop
        tile_x = 0
        tile_y -= TILE_SIZE

    return root_tile


def draw_characters(game_screen, hero, enemy, weapon, root_tile):
    """
    :param game_screen: a pygame screen
    :param hero: a Hero
    :param enemy: an Enemy
    :param weapon: a Weapon
    :param root_tile: a list of Decor
    :return: /
    """
    hero.draw(game_screen)
    if enemy.is_alive():
        enemy.draw(game_screen)
    for tile in root_tile:
        tile.draw_decor('tile_root.png', game_screen, tile.get_x(), tile.get_y())
    if weapon.get_fire_on_status():
        weapon.move_x()
        weapon.draw(game_screen)
