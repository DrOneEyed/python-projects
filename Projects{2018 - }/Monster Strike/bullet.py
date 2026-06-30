import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,Invad_set,screen,ship):
        #Provides functionality to parent class
        super(Bullet, self).__init__()
        self.screen = screen
        #Bullet Comes from the top of the ship
        self.rect = pygame.Rect(0,0,Invad_set.bullet_width, Invad_set.bullet_height)
        #Bullet comes from centre of the ship
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = Invad_set.bullet_color
        self.speed = Invad_set.bullet_speed
    def update(self):
        #Sends bullet in a straight line
        self.y -=self.speed
        self.rect.y = self.y
    def draw_bullet(self):
        #Draws bullet on the screen
        pygame.draw.rect(self.screen, self.color, self.rect)
