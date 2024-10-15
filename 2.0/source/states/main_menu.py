import pygame
from .. import tools, setup
from .. import constants as C
from ..components import info

class MainMenu:
    def __init__(self):
        self.setup_background()
        self.setup_player()
        self.setup_cursor()
        self.info = info.Info('main_menu')

    def setup_background(self):
        self.background = setup.GRAPHICS['level_1']
        self.background_rect = self.background.get_rect()
        self.background = pygame.transform.scale(self.background, (int(self.background_rect.width * C.bg_scale),
                                                                   int(self.background_rect.height * C.bg_scale)))
        self.viewport = setup.SCREEN.get_rect()
        self.caption = tools.get_image(setup.GRAPHICS['title_screen'], 1, 60, 177, 88, (255, 0, 220),C.bg_scale )
    def setup_player(self):
        self.player_image = tools.get_image(setup.GRAPHICS['mario_bros'],178,32,12,16,(0,0,0),C.bg_scale)

    def setup_cursor(self):
        self.cursor = pygame.sprite.Sprite()
        self.cursor = tools.get_image(setup.GRAPHICS['item_objects'],24,160,8,8,(0,0,0),C.bg_scale)
    def update(self,surface):
        surface.blit(self.background,self.viewport)
        surface.blit(self.caption, (170, 100))
        surface.blit(self.player_image, (110, 495))
        surface.blit(self.cursor, (220, 360))

        self.info.update()
        self.info.draw(surface)