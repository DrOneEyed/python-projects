import pygame.font
class Button():
    def __init__(self, Invad_set, screen, msg):
        self.screen = screen
        #Get the rectangular area of the surface
        self.screen_rect = screen.get_rect()
        #Width
        self.width, self.height =250,50
        #Background color
        self.b_color = (0,0,0)
        #Text color
        self.t_color = (255,255,255)
        #Font
        self.font = pygame.font.SysFont(None,48)
        
        self.rect = pygame.Rect(0,0,self.width,self.height)
        #Center the button
        self.rect.center = self.screen_rect.center

        self.prep_msg(msg)
        
    #Makes sure text appears in the centre, also turns it into a rendered image
    def prep_msg(self,msg):
        self.msg_image = self.font.render(msg, True, self.t_color, self.b_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    #Draw blank button and then draw image
    def draw_b(self):
        self.screen.fill(self.b_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)        
