from hero import *
from enemy import *
from weapon import *
from decor import *
from collision import *
from movements import key_hit_movement
from musics import play_music
from setup import set_import_image, set_window, set_root_tiles, draw_characters


def quit():
    """
        Quits game
    """
    pygame.quit()
    sys.exit()


def game(game_screen):
    """
        Game Loop
    """
    clock.tick(27)  # Number of frames per second
    set_window("Battle", os.path.join('images', 'standing.png'), game_screen)
    dx_hero = 0 # Derivate of x
    hero = Hero()  # Initializes player class
    enemy = Enemy() # Initializes enemy class
    weapon = Weapon() # Initializes weapon class
    root_tile = set_root_tiles() # Initializes tiles

    while True:
        game_screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            dx_hero = key_hit_movement(event, hero, weapon)

        # Movement
        hero.move_x(dx_hero)
        hero.move_y()
        enemy.move_x()

        # Collision detection
        detect_collision(enemy, hero, weapon)

        # Draws hero, enemy, tiles, weapon
        draw_characters(game_screen, hero, enemy, weapon, root_tile)

        pygame.display.update()


if __name__ == '__main__':
    # Init pygame
    pygame.init()

    # Create game screen and launches music
    screen = pygame.display.set_mode(WINDOW)

    background = set_import_image('background.jpg')
    game_font = pygame.font.Font('font.ttf', 25)
    end_game_font = pygame.font.Font('font.ttf', 50)
    #play_music('background_sound.wav', -1)

    # Launches game
    game(screen)
