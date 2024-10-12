import pygame
from .. import tools, setup
from .. import constants as C

class MainMenu:
    def __init__(self):
        self.setup_background()
        self.setup_player()
        self.setup_cursor()

    def setup_background(self):
        self.background = setup.GRAPHICS['level_1']
        self.background_rect = self.background.get_rect()
        self.background = pygame.transform.scale(self.background, (int(self.background_rect.width * C.bg_scale),
                                                                   int(self.background_rect.height * C.bg_scale)))
        self.viewport = setup.SCREEN.get_rect()
        self.caption = tools.get_image(setup.GRAPHICS['title_screen'], 1, 60, 177, 88, (255, 0, 220),C.bg_scale )
    def setup_player(self):
        pass

    def setup_cursor(self):
        pass

    def update(self,surface):
        surface.blit(self.background,self.viewport)
           surface.blit(self.caption, (170, 100))