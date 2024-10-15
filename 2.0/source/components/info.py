import pygame
from .. import constants as C
pygame.font.init()

class Info:
    def __init__(self,state):
        self.state = state
        self.create_state_labels()
        self.create_info_labels()

    def create_state_labels(self):
        if self.state == 'main_menu':
            pass

    def create_info_labels(self):
        pass

    def create_label(self,label,size=40,width_scale=1.25,height_scale=1):
        font = pygame.font.SysFont(C.FONT,size)
        label_image = font.render(label,1,(255,255,255))
        rect = label_image.get_rect()
        label_image = pygame.transform.scale(label_image,(int(rect.width * width_scale),int(rect.height * height_scale)))
        return label_image

    def update(self):
        pass

    def draw(self,surface):
        surface.blit(self.create_label('hello',size=60),(100,400))