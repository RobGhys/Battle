"All imports"
import sys
import math
import pygame
import os

from pygame import mixer
from pygame.locals import *

"All Global functions used throughout the program"

# Screen size
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
WINDOW = (WINDOW_WIDTH, WINDOW_HEIGHT)

# Number of  tiles to fill screen
TILE_SIZE = 32
NB_TILES_TO_FILL_SCREEN = WINDOW_WIDTH // TILE_SIZE

# Character size
CHARACTER_SIZE = 64  # Number of pixels in the image: 64x64

#                          R    G    B
WHITE                  = (255, 255, 255)
BLACK                  = (  0,   0,   0)
RED                    = (255,   0,   0)
GREEN                  = (  0, 255,   0)
BLUE                   = (  0,   0, 255)
DARKGREEN              = (  0, 155,   0)
DARKGRAY               = ( 40,  40,  40)
SKY_BLUE               = (108, 140, 255)
BACKGROUND_COLOR       = (79, 77, 62)
BULLETCOLOR            = (244, 220,  38)

# Clock
clock = pygame.time.Clock()
