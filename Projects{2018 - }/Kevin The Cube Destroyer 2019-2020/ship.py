import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    
    def __init__(self,Invad_set,screen):

        super(Ship,self).__init__()
        self.screen = screen
        self.Invad_set = Invad_set
        self.image = pygame.image.load('img/final.bmp').convert()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.moving_right =False
        self.moving_left = False
        '''self.moving_up = False
        self.moving_down = False'''
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.Invad_set.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.Invad_set.ship_speed
        '''elif self.moving_up == True:
            self.rect.centery -=1
        elif self.moving_down == True:
            self.rect.centery +=1'''
        self.rect.centerx = self.center
        
    def blitme(self):
            self.screen.blit(self.image, self.rect)
