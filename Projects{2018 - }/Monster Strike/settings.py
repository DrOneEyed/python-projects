import pygame
class Settings():
    def __init__(self):
        #Dimensions of screen
        self.width=1200
        self.height=700
    
        self.bg_color=(0,0,0)
        #Space background
        self.bg_image = pygame.image.load("img/BG.jpg")

        self.ship_limit = 2
        
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color= (227,207,87)
    
        #Drop speed of aliens
        self.fleet_drop_speed = 20

        #Change in speed as round increases-Multiplied
        self.speed_up = 1.3
        #Change in score per kill as round increases
        self.score_s= 50

        self.int_change_set()

        self.s_active = True

        self.pau_b = False
        
    #Starting speed(Increased space_ship speed)
    def int_change_set(self):
        self.ship_speed = 6
        self.bullet_speed = 4
        self.alien_speed_factor = 2.5
        #Doubt
        self.fleet_dir = 1
        #Points per kill in level 1
        self.alien_p = 100
        
    #Change in speed as level changes(Spaceship, bullet speed stays same throughout)
    def inc_speed(self):
        self.alien_speed_factor *= self.speed_up
        #Points increase as level increase(Now adds by 50 per round not multiply by 1.5)
        self.alien_p = int(self.alien_p + self.score_s)
