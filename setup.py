import os
import pygame
from global_vars import BACKGROUND__COLOR, WINDOW_HEIGHT, TILE_SIZE, NB_TILES_TO_FILL_SCREEN
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
    screen.fill(BACKGROUND__COLOR)  # Fills screen with light blue


def set_tiles():
    x_start = 0
    nb_tiles_to_fill_screen = NB_TILES_TO_FILL_SCREEN

    root_tile = []  # Init a list so that we can append Decor objects in it
    # Black boxes in the bottom
    root_tile = create_decor_list(root_tile, 'tile_root_bottom.png',
                                  x_start, WINDOW_HEIGHT - TILE_SIZE,
                                  nb_tiles_to_fill_screen)
    # Metal boxes on top of black boxes in the bottom
    root_tile = create_decor_list(root_tile, 'tile_root_top.png',
                                  x_start, WINDOW_HEIGHT - 2 * TILE_SIZE,
                                  nb_tiles_to_fill_screen)
    # Metal boxes, first row on the left
    root_tile = create_decor_list(root_tile, 'tile_root_top.png',
                                  (TILE_SIZE * 2), WINDOW_HEIGHT - 5 * TILE_SIZE, 4)
    # Metal boxes, first row on the right
    root_tile = create_decor_list(root_tile, 'tile_root_top.png',
                                  (TILE_SIZE * 14), WINDOW_HEIGHT - 5 * TILE_SIZE, 4)
    # Metal boxes, second row in the middle
    root_tile = create_decor_list(root_tile, 'tile_root_top.png',
                                  (TILE_SIZE * 5), WINDOW_HEIGHT - 7 * TILE_SIZE, 10)
    return root_tile


def set_coins():
    coins = []  # Init a list so that we can append Decor objects in it

    coins = create_decor_list(coins, 'coin.png',
                              TILE_SIZE * 4, WINDOW_HEIGHT - 3 * TILE_SIZE, 4)
    coins = create_decor_list(coins, 'coin.png',
                              TILE_SIZE * 14, WINDOW_HEIGHT - 3 * TILE_SIZE, 4)

    return coins


def create_decor_list(tmp_decor_list, image, tile_x, tile_y, nb_decor_items):
    """
    :requires: x and y starting positions, list of tiles, how many tiles
    :return: a list of tiles
    """

    for tile in range(nb_decor_items):
        tmp_decor_list.append(Decor(tile_x, tile_y, image))
        # Increase x so that we draw further tiles
        tile_x += TILE_SIZE

    return tmp_decor_list


def draw_characters(game_screen, hero, enemies, weapon):
    """
    :param game_screen: a pygame screen
    :param hero: a Hero
    :param enemies: an Enemy
    :param weapon: a Weapon
    :return: /
    """
    # Draws hero
    hero.draw(game_screen)

    # Draws enemies if they are still alive
    for enemy in enemies:
        if enemy.is_alive():
            enemy.draw(game_screen)

    # Draws weapon if it is activated
    if weapon.get_fire_on_status():
        weapon.move_x()
        weapon.draw(game_screen)


def draw_map(game_screen, tiles, coins):
    """
    :param game_screen: a pygame screen
    :param root_tile: a list of Decor
    :return: 
    """""
    for tile in tiles:
        tile.draw_decor(game_screen)
    for coin in coins:
        coin.draw_decor(game_screen)
