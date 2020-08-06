from character import *

"""
Describes the Player's spaceship 
Typical player has <{x, y}, lives, score, score_x, score_y> characteristics
"""
class Player(Character):

    def __init__(self):
        self.x = (WIDTH - self.player_size) // 2
        self.y = HEIGHT - (self.player_size + 5)

        self.lives = 3
        self.lives_x = (WIDTH - 100)
        self.lives_y = 10

        self.score = 0
        self.score_x = 10
        self.score_y = 10


    """
        @modifies self.x to self.x + dx if self.getx() >= 0 and self.getx() <= (WIDTH - self.PLAYER_SIZE) \
        and teleports player to right-hand side or left-hand size
    """
    def move_x(self, dx):
        # Player goes from left-hand side to right-hand side
        if self.get_x() < 0:
            self.x = (WIDTH - self.player_size)

        # Player goes from right-hand side to left-hand side
        elif self.get_x() > (WIDTH - self.player_size):
            self.x = 0

        # Player moves by dx unit
        else:
            self.x += dx

    """
        @returns self.lives
    """
    def get_lives(self):
        return self.lives


    """
        @modifies self.lives_post = self.lives - 1
    """
    def decrease_lives(self):
        if self.lives > 0:
            self.lives -= 1


    """
        @modifies self.score_post to self.score + ds
    """
    def increase_score(self, ds):
        self.score += ds

    """
        @modifies out: shows score on the screen
    """
    def display_score(self, surface, font):
        score_box = font.render("Score: " + str(self.score), True, WHITE)
        surface.blit(score_box, (self.score_x,self.score_y))

    """
        @modifies out: shows lives on the screen
    """
    def display_lives(self, surface, font):
        lives_box = font.render("lives: " + str(self.lives), True, RED)
        surface.blit(lives_box, (self.lives_x, self.lives_y))