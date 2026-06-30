import pygame
class Settings():
 
    def __init__(self):
        self.width=1200
        self.height=700
        
        self.bg_color=(0,0,0)
        self.bg_image = pygame.image.load("img/BG.jpg")

        self.ship_limit = 1
        
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color= (227,207,87)

        self.fleet_drop_speed = 6

        self.speed_up = 1.3

        self.score_s= 1.5

        self.int_change_set()

        self.s_active = True

        self.pau_b = False

    def int_change_set(self):
        self.ship_speed = 2
        self.bullet_speed = 2
        self.alien_speed_factor = 2.5
        self.fleet_dir = 1
        self.alien_p = 100

    def inc_speed(self):
        self.ship_speed *= self.speed_up
        self.bullet_speed *= self.speed_up
        self.alien_speed_factor *= self.speed_up
        self.alien_p = int(self.alien_p * self.score_s)
