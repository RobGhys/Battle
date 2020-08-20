from character import *


class Enemy(Character):

    items_image_size = 32

    def __init__(self, x, y):
        # Initial position -> bottom right corner
        self.start_x = x
        self.x = self.start_x
        self.min_x = self.x
        self.max_x = self.x
        self.y = y
        self.dx = 2
        self.direction = -1
        self.alive = True
        self.grounded = True
        self.reached_edge = False

        # Used for sprites
        self.img_folder_path = 'images/enemy'
        self.right = False
        self.left = False

        # Lists containing each sprites for right, left, or standing, ready to use for display
        self.sprites_right = ['R1E.png', 'R2E.png', 'R3E.png', 'R4E.png',
                              'R5E.png', 'R6E.png', 'R7E.png', 'R8E.png',
                              'R9E.png', 'R10E.png', 'R11E.png']
        self.sprites_left = ['L1E.png', 'L2E.png', 'L3E.png', 'L4E.png',
                             'L5E.png', 'L6E.png', 'L7E.png', 'L8E.png',
                             'L9E.png', 'L10E.png', 'L11E.png']

        self.walkRight = self.load_sprite_sub_folder(self.sprites_right, self.img_folder_path)
        self.walkLeft = self.load_sprite_sub_folder(self.sprites_left, self.img_folder_path)

        self.frame_lasting_sprite = 3  # Each sprite should last this amount of frame in game loop
        self.walk_count = 0

    def is_alive(self):
        return self.alive

    def kill_enemy(self):
        self.alive = False

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left

    def get_grounded(self):
        return self.grounded

    def get_max_x(self):
        return self.max_x

    def get_min_x(self):
        return self.min_x

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

    def set_max_x(self, x):
        self.max_x = x

    def set_min_x(self, x):
        self.min_x = x

    def set_grounded(self, grounded):
        self.grounded = grounded

    def reset_walk_count(self):
        self.walk_count = 0

    def increase_walk_count(self):
        self.walk_count += 1

    def reverse_direction(self):
        self.direction *= -1

    def move_x(self):
        # Enemy goes from right-hand side to left-hand side
        if self.get_x() > self.max_x:
            print('1')
            print('x: ' + str(self.x) + ' , ' + str(self.max_x))
            self.set_left(True)
            self.set_right(False)
            self.direction = -1
            self.x = self.max_x - 1
        # Enemy goes from left-hand side to right-hand side
        elif self.get_x() < self.min_x:
            print('2')
            self.set_left(False)
            self.set_right(True)
            self.direction = 1
            self.x = self.min_x
        else:
            self.x += self.dx * self.direction

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
        else:
            self.draw_sprite(self.walkLeft[self.get_walk_count() // 3], screen)
            self.increase_walk_count()  # Increases walk_count by 1
