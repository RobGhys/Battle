import sys

from player import *
from enemy import *
from bullet import *
from big_bertha import *

"""
    @requires event != null && event a keyboard input
    @returns dx, derivative of x
"""
def move_player(event):
    dx = 0 #initialization is necessary

    # Key pressed
    if event.type == KEYDOWN:
        if event.key == K_RIGHT:
            dx = 5
        if event.key == K_LEFT:
            dx = -5

    # Key released
    if event.type == KEYUP:
        if event.key == K_RIGHT or event.key == K_LEFT:
            dx = 0

    return dx

"""
    Moves all characters
"""
def characters_movement(player, all_enemies, bullet, all_ammo, dx):
    player.move_x(dx)  # Uses dx to move player
    for enemy in all_enemies:
        enemy.move(player)
    for bertha in all_ammo:
        bertha.move(player)
    bullet.move(player)


"""
    @modifies enemy.alive_post to False, player.score_post to player.score + ds, and bullet.state_post to 'off
    if there is a collision between bullet and enemy
"""
def collision_bullet(bullet, all_enemies, player):
    for enemy in all_enemies:
        if bullet.is_colliding(enemy):
            enemy.set_alive(False)  # Kills the enemy
            all_enemies.remove(enemy)
            player.increase_score(25)  # Increase score
            bullet.set_state('off')  # Removes bullet

"""
    @modifies enemy.alive_post to False, player.score_post to player.score + ds, and bertha.state_post to 'off
    if there is a collision between big bertha and enemy
"""
def collision_bertha(all_ammo, all_enemies, player):
    for enemy in all_enemies:
        for bertha in all_ammo:
            if bertha.is_colliding(enemy):
                enemy.set_alive(False)  # Kills the enemy
                all_enemies.remove(enemy)
                player.increase_score(10)  # Increase score
                bertha.set_state('off')  # Removes bullet
                break


"""
    @returns all_enemies
"""
def populates_with_enemies():
    nb_enemies = random.randint(3, 10)
    all_enemies = []
    for i in range(nb_enemies):
        all_enemies.append(Enemy())
    return all_enemies


"""
    @returns all_ammo
"""
def launch_big_bertha(player):
    nb_ammo = 5
    all_ammo = []
    for i in range(nb_ammo):
        all_ammo.append(Big_Bertha(player))
    return all_ammo

"""
    @returns pygame image object from image name
    (uses os conversion)
"""
def set_import_image(imageName):
    img_path = os.path.join('images', imageName)
    return pygame.image.load(img_path).convert()


"""
    Shows Title & icon
    @requires: title is String
    @requires: icon is a .png file
    @modifies: out
"""
def set_window(title, iconScreen):
    pygame.display.set_caption(title)
    icon = pygame.image.load(iconScreen)
    pygame.display.set_icon(icon)
    screen.fill(BLACK)  # Fills screen with black


"""
    Draws characters, score board and lives board on screen
"""
def draw(player, all_enemies, all_ammo, bullet):
    # Draw player, enemy, bullet, score, and lives
    player.draw_item('player2.png', screen)

    for enemy in all_enemies:
        if enemy.get_alive():
            enemy.draw_item('alien2.png', screen)

    if bullet.get_state() == 'on':
        bullet.draw_item('bullet.png', screen)

    for bertha in all_ammo:
        if bertha.get_state() == 'on':
            bertha.draw_item('bullet2.png', screen)

    player.display_score(screen, game_font)
    player.display_lives(screen, game_font)


"""
    Quits game
"""
def quit():
    pygame.quit()
    sys.exit()


"""
    Game Loop
"""
def game():
    set_window("Space Invaders", os.path.join('images', 'ufo.png'))
    player = Player() # Initializes player class
    bullet = Bullet(player) # Initializes bullet class
    dx = 0

    # Populates List of enemies and Big_Bertha
    all_enemies = populates_with_enemies()
    all_ammo = launch_big_bertha(player)

    while True:
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            # Check if exit game
            if event.type == QUIT:
                quit()
            # Player actions
            dx = move_player(event)
            bullet.throw_bullet(event)

            all_ammo[0].throw_bullet(event)
            if all_ammo[0].get_state() == 'on':
                for bertha in all_ammo:
                    bertha.set_state('on')


        # Repopulates enemy
        if len(all_enemies) == 0:
            all_enemies = populates_with_enemies()

        # Characters movement
        characters_movement(player, all_enemies, bullet, all_ammo, dx)
        # Collision check
        collision_bullet(bullet, all_enemies, player)
        collision_bertha(all_ammo, all_enemies, player)
        # Draw characters
        draw(player, all_enemies, all_ammo, bullet)

        # Update display
        pygame.display.update()


if __name__ == '__main__':
    # Init pygame
    pygame.init()

    # Create game screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    background = set_import_image('background.png')
    game_font = pygame.font.Font('font.ttf', 25)

    # Launches game
    game()