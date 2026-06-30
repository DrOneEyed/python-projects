import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_func as gf
from game_stats import GameStats
from button import Button
from score import Score
def run_game():
    #Initialize pygame
    pygame.init()
    pygame.mixer.init()
    #Loading a music file
    pygame.mixer.music.load('Music/SAO.mp3')
    #Volume
    pygame.mixer.music.set_volume(0.5)
    #-1 repeats music infinite times
    pygame.mixer.music.play(-1)
    #Settings() is a programmer defined class
    Invad_set = Settings()
    #Setting up the screen
    screen = pygame.display.set_mode((Invad_set.width, Invad_set.height), pygame.RESIZABLE) #pygame.FULLSCREEN

    #Top window name
    pygame.display.set_caption("Monster Strike")

    play_b = Button(Invad_set,screen,"Click to start")
    pause_b = Button(Invad_set,screen,"CONTINUE")
    stats = GameStats(Invad_set)
    sb= Score(Invad_set, screen, stats)
    ship = Ship(Invad_set, screen)
    bullets = Group()
    aliens= Group()
    

    gf.create_fleet(Invad_set, screen, ship, aliens)
    while True:
        gf.check_events(Invad_set, screen,stats,sb,play_b ,ship,aliens,bullets,pause_b)
        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_bullets(Invad_set, screen,stats,sb,ship,aliens, bullets)
            gf.update_aliens(Invad_set,stats,sb,screen,ship,aliens,bullets)
        gf.update_screen(Invad_set, screen, stats, sb, ship, aliens, bullets, play_b)

run_game()  
