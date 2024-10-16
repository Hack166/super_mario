from ..components import info
import pygame
from .. import tools,setup
from .. import constants as C

class LoadScreen:
    def __init__(self):
        self.finished = False
        self.next = None
        self.info = info.Info('level')
        self.setup_background()

    def setup_background(self):
        self.background = setup.GRAPHICS['level_1']
        rect = self.background.get_rect()
        self.background = pygame.transform.scale(self.background, (int(rect.width * C.bg_scale), int(rect.height * C.bg_scale)))
        self.background_rect = self.background.get_rect()



    def update(self, surface, keys):
        self.draw(surface)

    def draw(self, surface):
        surface.blit(self.background, (0, 0))
        self.info.draw(surface)