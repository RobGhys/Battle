from global_vars import *


class Character:
    """
    Describes a Character's characteristics
    Typical character has <{x, y},right, left> characteristics
    """
    character_size = 64  # Number of pixels in the image: 64x64


    def __init__(self):
        self.x = 0
        self.y = 0

    def get_x(self):
        """
            @returns self.x
        """
        return self.x

    def get_y(self):
        """
            @returns self.y
        """
        return self.y

    def play_music(self, file):
        """
            Plays sound from file
        """
        sound_path = os.path.join('sounds', file)
        mixer.Sound(sound_path).play()

    def draw_item(self, icon_character, surface, x, y):
        """
            @modifies draw Character on the screen
        """
        img_path = os.path.join('images', icon_character)
        character_image = pygame.image.load(img_path).convert_alpha()
        surface.blit(character_image, (x, y))

    def draw_item_sub_folder(self, path, icon_character, surface, x, y):
        """
            @modifies draw Character on the screen
        """
        img_path = os.path.join(path, icon_character)
        character_image = pygame.image.load(img_path).convert_alpha()
        surface.blit(character_image, (x, y))

    def load_sprite(self, icon_list):
        """
            @requires icon_list != null
            @returns a list that will load each sprite in icon_list
        """
        sprites = []
        for i in range(len(icon_list)):
            img_path = os.path.join('images', icon_list[i])
            current_image = pygame.image.load(img_path).convert_alpha()
            sprites.append(current_image)

        return sprites

    def load_sprite_sub_folder(self, icon_list, path):
        """
            @requires icon_list != null
            @returns a list that will load each sprite in icon_list
        """
        sprites = []
        for i in range(len(icon_list)):
            img_path = os.path.join(path, icon_list[i])
            current_image = pygame.image.load(img_path).convert_alpha()
            sprites.append(current_image)

        return sprites

    def draw_sprite(self, sprite, surface):
        """
            @modifies draw Character on the screen
        """
        surface.blit(sprite, (self.get_x(), self.get_y()))

    def get_pixel_size(self):
        return self.character_size
