import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self, Invad_set, screen):
        super(Alien,self).__init__()
        self.screen = screen
        self.Invad_set = Invad_set
        self.image = pygame.image.load('img/cube.bmp')
        self.rect = self.image.get_rect()
        self.rectx = self.rect.width
        self.recty = self.rect.height
        self.x = float(self.rect.x)
    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def check_edges(self,Invad_set):
        if Invad_set.s_active == True:
            screen_rect = self.screen.get_rect()
            if self.rect.right >= screen_rect.right:
                return True
            elif self.rect.left <= 0:
                return True
        else:
            pass
        
    def update(self):
        self.x += (self.Invad_set.alien_speed_factor * self.Invad_set.fleet_dir)
        self.rect.x = self.x
        
