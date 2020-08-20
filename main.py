from hero import *
from enemy import *
from weapon import *
from decor import *
from collision import *
from movements import key_hit_movement, move_characters
from musics import play_music
from setup import set_import_image, set_window, set_tiles, draw_characters, draw_map, set_coins, set_enemies
from intro_menu import start
from game_over import game_over


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
    enemies = set_enemies()
    weapon = Weapon() # Initializes weapon class
    tiles = set_tiles() # List of Decor
    coins = set_coins() # List of Decor

    while True:
        game_screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            dx_hero = key_hit_movement(event, hero, weapon)

        # Movement
        move_characters(hero, enemies, dx_hero)

        # Collision detection
        detect_collision(enemies, hero, weapon, coins)

        # Draws hero, enemy, tiles, weapon
        draw_map(game_screen, tiles, coins)
        draw_characters(game_screen, hero, enemies, weapon)

        pygame.display.update()

        if hero.get_lives() == 0:
            return hero.get_score()


if __name__ == '__main__':
    # Init pygame
    pygame.init()

    # Create game screen and launches music
    screen = pygame.display.set_mode(WINDOW)

    background = set_import_image('background.png')
    game_font = pygame.font.Font('font.ttf', 25)
    end_game_font = pygame.font.Font('font.ttf', 50)
    #play_music('background_sound.wav', -1)

    # Launches game
    start(screen, background)
    score = game(screen)

    # Game over
    pygame.mixer.music.pause()
    game_over(screen, background, score)
