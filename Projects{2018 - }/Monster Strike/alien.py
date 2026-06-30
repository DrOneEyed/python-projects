import pygame
#Sprite is a pygame module with basic game object classes
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self, Invad_set, screen):
        super(Alien,self).__init__()
        self.screen = screen
        self.Invad_set = Invad_set
        self.image = pygame.image.load('img/alien.bmp')
        self.rect = self.image.get_rect()
        self.rectx = self.rect.width
        self.recty = self.rect.height
        #Counts The No. of aliens
        self.x = float(self.rect.x)
    def blitme(self):
        #MOves the group of aliens
        self.screen.blit(self.image,self.rect)

    def check_edges(self,Invad_set):
        #Makes Sure that the gropu of aliens does not out of the window
        if Invad_set.s_active == True:
            screen_rect = self.screen.get_rect()
            if self.rect.right>= screen_rect.right:
                return True
            elif self.rect.left <= 0:
                return True
        else:
            pass
    def update(self):
        #Increases The Speed of the fleet after each level
        self.x += (self.Invad_set.alien_speed_factor * self.Invad_set.fleet_dir)
        self.rect.x = self.x
        
