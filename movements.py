from pygame.locals import *


def key_hit_movement(event, hero, weapon):
    """
        @requires event != null && hero != null && event a keyboard input
        @returns dx, derivates of x
    """
    dx = 0

    # Key pressed
    if event.type == KEYDOWN:
        if event.key == K_RIGHT and not hero.get_jump_status():
            dx = 5
            # Sets the Hero and weapon to right direction
            hero.set_right(True)
            hero.set_left(False)
            if not weapon.fire_on:
                weapon.set_facing(1)
        elif event.key == K_LEFT and not hero.get_jump_status():
            # Sets the Hero and weapon to left direction
            dx = -5
            hero.set_left(True)
            hero.set_right(False)
            if not weapon.fire_on:
                weapon.set_facing(-1)
        elif event.key == K_SPACE:
            # Jumps
            hero.set_jump_status(True)
        elif event.key == K_r:
            # Fires a bullet
            weapon.set_fire_on_status(True)
            x = hero.get_x() + (hero.get_pixel_size() // 2)
            y = hero.get_y() + (hero.get_pixel_size() // 2)
            weapon.fix_position(x, y)
        else:
            # No movement -> sprite show stand still
            hero.no_movement()

    # Key released
    if event.type == KEYUP:
        if event.key == K_RIGHT or event.key == K_LEFT:
            dx = 0
            hero.set_left(False)
            hero.set_right(False)

    return dx


def movement_right(hero):
    """
    Sets the hero to the sprite moving to the right
    :return: dx
    """
    dx = 5
    hero.set_right(True)
    hero.set_left(False)
    return dx


def movement_left(hero):
    """
    Sets the hero to the sprite moving to the left
    :return: dx
    """
    dx = -5
    hero.set_right(False)
    hero.set_left(True)
    return dx
