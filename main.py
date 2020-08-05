import sys

from player import *
from enemy import *
from bullet import *


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
def characters_movement(player, enemy, bullet, dx):
    player.move_x(dx)  # Uses dx to move player
    enemy.move(player)
    bullet.move(player)


"""
    @modifies enemy.alive_post to False, player.score_post to player.score + ds, and bullet.state_post to 'off
    if there is a collision between bullet and enemy
"""
def collision_event(bullet, enemy, player):
    if bullet.is_colliding(enemy):
        enemy.set_alive(False)  # Kills the enemy
        player.increase_score()  # Increase score
        bullet.set_state('off')  # Removes bullet

"""
    Quits game
"""
def quit():
    pygame.quit()
    sys.exit()

"""
    Draws characters
"""
def draw(player, enemy, bullet):
    # Draw player, enemy, bullet, score, and lives
    player.draw_item('player2.png', screen)

    if enemy.get_alive():
        enemy.draw_item('alien2.png', screen)

    if bullet.get_state() == 'on':
        bullet.draw_item('bullet.png', screen)

    player.display_score(screen, game_font)
    player.display_lives(screen, game_font)

"""
    Game Loop
"""
def game():
    # Init objects
    set_window("Space Invaders", os.path.join('images', 'ufo.png'))
    player = Player() # Initializes player class
    enemy = Enemy() # Initializes enemy class
    bullet = Bullet(player) # Initializes bullet class

    # Populates Array of enemies
    nb_enemies = random.randint(1, 10)
    all_enemies = []
    for i in range(nb_enemies):
        all_enemies.append(Enemy())

    while True:
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            # Check if exit game
            if event.type == QUIT:
                quit()
            # Player action
            dx = move_player(event) # Record key that was hit
            bullet.throw_bullet(event)

        # Characters movement
        characters_movement(player, enemy, bullet, dx)
        # Collision check
        collision_event(bullet, enemy, player)
        # Draw characters
        draw(player, enemy, bullet)

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