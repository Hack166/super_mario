import pygame
from . import constants as C
from . import tools

pygame.init()
SCREEN = pygame.display.set_mode((C.SCREEN_H, C.SCREEN_W))

GRAPHICS = tools.load_graphics('resources/graphics')