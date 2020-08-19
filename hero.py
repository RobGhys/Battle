from character import *


class Hero(Character):
    """
    A Hero is the character the player will play in this game.
    Typical Hero has <{x, y}, lives, score> characteristics
    Hero is mutable
    """
    items_image_size = 32

    def __init__(self):
        # Initial position -> bottom left corner
        self.x = self.character_size
        self.y = WINDOW_HEIGHT - self.character_size - (2 * TILE_SIZE) + 5

        # Jump status
        self.is_jump = False
        self.jump_count_init = 8
        self.jump_count = self.jump_count_init

        # Used for sprites
        self.img_folder_path = 'images/hero'
        self.right = False
        self.left = False

        # Lists containing each sprites for right, left, or standing, ready to use for display
        self.sprites_right = ['R1.png', 'R2.png', 'R3.png', 'R4.png', 'R5.png', 'R6.png', 'R7.png', 'R8.png', 'R9.png']
        self.sprites_left = ['L1.png', 'L2.png', 'L3.png', 'L4.png', 'L5.png', 'L6.png', 'L7.png', 'L8.png', 'L9.png']
        self.sprites_standing = ['standing.png']

        self.walkRight = self.load_sprite_sub_folder(self.sprites_right, self.img_folder_path)
        self.walkLeft = self.load_sprite_sub_folder(self.sprites_left, self.img_folder_path)
        self.char = self.load_sprite_sub_folder(self.sprites_standing, self.img_folder_path)

        self.frame_lasting_sprite = 3  # Each sprite should last this amount of frame in game loop
        self.walk_count = 0

        # Interface and game status
        self.interface_font = pygame.font.Font('font.ttf', 20)
        self.lives = 3
        self.life_time_lapse = 0
        self.score = 0

    def get_lives(self):
        return self.lives

    def get_lifetime_lapse(self):
        return self.life_time_lapse

    def increase_life_time_lapse(self):
        self.life_time_lapse += 1

    def reset_life_time_lapse(self):
        self.life_time_lapse = 0

    def get_jump_status(self):
        return self.is_jump

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left

    def get_walk_count(self):
        return self.walk_count

    def get_timer_reset_sprite(self):
        """
            @returns the size until which walk_count can increase before being reset.
            This is dependent on how many frames there are, and how long we want each frame to last.
        """
        return len(self.sprites_right) * self.frame_lasting_sprite

    def set_right(self, right):
        self.right = right

    def set_left(self, left):
        self.left = left

    def set_jump_status(self, jumping):
        self.is_jump = jumping

    def no_movement(self):
        """Standing mode"""
        self.left = False
        self.right = False
        self.reset_walk_count()

    def reset_walk_count(self):
        self.walk_count = 0

    def increase_walk_count(self):
        self.walk_count += 1

    def decrease_lives(self):
        self.lives -= 1

    def increase_score(self, ds):
        self.score += ds

    def get_score(self):
        return self.score

    def move_x(self, dx):
        """
            @modifies self.x to self.x + dx if self.getx() >= 0 and self.getx() <= (WINDOW_WIDTH - self.character_size)
        """
        # Player goes from left-hand side to right-hand side
        if self.get_x() < 0:
            self.x = 0
        # Player goes from right-hand side to left-hand side
        elif self.get_x() > (WINDOW_WIDTH - self.character_size):
            self.x = (WINDOW_WIDTH - self.character_size - 10)
        # Player moves by dx unit
        else:
            self.x += dx

    def move_y(self):
        """If self.is_jump is True, """
        if self.is_jump:
            if self.jump_count >= -self.jump_count_init:
                direction = 1
                if self.jump_count < 0:
                    direction = -1
                self.y -= 0.5 * (self.jump_count**2) * direction
                self.jump_count -= 1
            else:
                self.is_jump = False
                self.jump_count = self.jump_count_init

    def get_sprite_left(self):
        return self.walkLeft

    def get_sprite_right(self):
        return self.walkRight

    def get_sprite_standing(self):
        return self.sprites_standing

    def draw(self, screen):
        '''Draws the Hero on the screen'''
        # Reset walk_count if it reaches 28
        # 28 -> 9 sprites per position (left or right) that we leave during 3 frames
        if self.get_walk_count() + 1 >= self.get_timer_reset_sprite():
            self.reset_walk_count()

        # Battle moving to the right
        if self.get_right():
            # Displays the right sprite if character is moving to the right.
            # We use the i-th position of the list of all sprites moving to the right, and (int)divide it by 3
            self.draw_sprite(self.walkRight[self.get_walk_count() // 3], screen)
            self.increase_walk_count()  # Increases walk_count by 1

        # Battle moving to the left
        elif self.get_left():
            self.draw_sprite(self.walkLeft[self.get_walk_count() // 3], screen)
            self.increase_walk_count()  # Increases walk_count by 1
        # Battle standing
        else:
            self.draw_item('standing.png', screen, self.x, self.y)

        '''Draws potion icons'''
        self.draw_interface(screen)

    def draw_interface(self, screen):
        '''Draws 1, 2, or 3 potions depending on number of lives remaining'''
        spacing_x = self.items_image_size - 4
        for i in range(self.lives):
            self.draw_item_sub_folder('images/decor', 'flask.png', screen, WINDOW_WIDTH - spacing_x, 0)
            spacing_x += (self.items_image_size // 2) + 4

        # Create a space between potion and coin logo
        spacing_x += self.items_image_size
        message = self.interface_font.render(str(self.score), True, WHITE)
        screen.blit(message, (WINDOW_WIDTH - spacing_x + 10, 7))

        spacing_x += self.items_image_size
        self.draw_item_sub_folder('images/decor', 'coin.png', screen, WINDOW_WIDTH - spacing_x, 0)
