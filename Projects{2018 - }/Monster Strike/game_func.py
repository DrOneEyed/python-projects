import sys
import pygame
from bullet import Bullet
from alien import Alien
import time
from button import Button
from settings import __init__

def check_keydown_events(event,Invad_set,screen ,stats, sb,play_b, ship,aliens, bullets,pause_b):
    aaa=Invad_set.bullet_speed
    bbb=Invad_set.alien_speed_factor
    if event.key == pygame.K_RIGHT:
        #If right key is pressed ship moves right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        #If left key is pressed ship moves left
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #If spacebar is pressed ship shoots out a bullet
        new_bullet = Bullet(Invad_set,screen, ship)
        bullets.add(new_bullet)
        #Sound effect
        effect = pygame.mixer.Sound('Music/GunSound.wav')
        effect.play()
    elif event.key == pygame.K_ESCAPE:
        #Game is deactivated and closed after esc
        Invad_set.s_active = False
        #Pygame ends after game is closed
        pygame.quit() #sys.exit()
    elif event.key == pygame.K_p:
        Invad_set.bullet_speed=0
        Invad_set.alien_speed_factor=0      
    elif event.key==pygame.K_r:
        pygame.K_RIGHT = True
        pygame.K_LEFT = True
        pygame.K_SPACE = True
        check_events(Invad_set,screen ,stats, sb,play_b, ship,aliens, bullets,pause_b)
        #pause_e(event,Invad_set,screen ,stats, sb,play_b, ship,aliens, bullets,pause_b)
'''def pause_e(event,Invad_set,screen ,stats, sb,play_b, ship,aliens, bullets,pause_b):
    Invad_set.pau_b = True
    if Invad_set.pau_b == True:
        pygame.mouse.set_visible(True)
        pause_b.draw_b()
    pygame.display.flip()'''
        
def check_keyup_events(event,Invad_set,screen ,stats, sb,play_b, ship,aliens, bullets,pause_b):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_p:
        pygame.K_RIGHT = False
        pygame.K_LEFT = False
        pygame.K_SPACE = False
    elif event.key==pygame.K_r:
        pygame.K_RIGHT = True
        pygame.K_LEFT = True
        pygame.K_SPACE = True
        check_events(Invad_set,screen ,stats, sb,play_b, ship,aliens, bullets,pause_b)

        
def check_events(Invad_set,screen ,stats, sb,play_b, ship,aliens, bullets,pause_b):
    if Invad_set.s_active == True:
        '''if event.type == pygame.QUIT:
            sys.exit()'''
        for event in pygame.event.get():
        
            if event.type == pygame.KEYDOWN:
                check_keydown_events(event,Invad_set,screen ,stats, sb,play_b, ship,aliens, bullets,pause_b)
            elif event.type == pygame.KEYUP:
                check_keyup_events(event,Invad_set,screen ,stats, sb,play_b, ship,aliens, bullets,pause_b)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y = pygame.mouse.get_pos()
                check_play_b(Invad_set,screen,stats,sb, play_b,ship, aliens, bullets, mouse_x, mouse_y)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y = pygame.mouse.get_pos()
        '''elif event.key == pygame.K_UP:
                ship.moving_up = True
        elif event.key == pygame.K_DOWN:
                ship.moving_down = True'''
    else:
        pass

def check_play_b(Invad_set,screen,stats,sb, play_b,ship, aliens, bullets, mouse_x, mouse_y):
    b_clicked = play_b.rect.collidepoint(mouse_x, mouse_y)
    if b_clicked and stats.game_active == False:
        Invad_set.int_change_set()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True
        sb.F_score()
        sb.F_high_score()
        sb.level_f()
        sb.prep_ship()

        
        aliens.empty()
        bullets.empty()

        create_fleet(Invad_set, screen, ship, aliens)
        ship.center
    elif b_clicked and stats.game_active == True:
        pass

def check_pause_b(Invad_set,screen,stats,sb, play_b,ship, aliens, bullets, mouse_x, mouse_y):
    b_clicked = play_b.rect.collidepoint(mouse_x, mouse_y)
    if b_clicked and stats.game_active == False:
        pygame.mouse.set_visible(False)
        Invad_set.pau_b == False
        
    elif b_clicked and stats.game_active == True:
        pass
        
def update_screen(Invad_set, screen,stats,sb, ship,aliens, bullets,play_b):
    screen.blit(Invad_set.bg_image,[0,0])
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    sb.show_score()

    if stats.game_active != True:
        play_b.draw_b()
    pygame.display.flip()
    
    
def update_bullets(Invad_set, screen,stats,sb,ship,aliens, bullets):
    
    bullets.update()
    for bullet in bullets.copy():
            if bullet.rect.bottom ==0:
                bullets.remove(bullet)
    check_bul_all_coll(Invad_set, screen , stats,sb,ship,aliens,bullets)

def check_bul_all_coll(Invad_set, screen , stats, sb,ship,aliens,bullets):
    coll= pygame.sprite.groupcollide(bullets,aliens,True,True)

    for aliens in coll.values():
        stats.score += Invad_set.alien_p * len(aliens)
        sb.F_score()
    check_high_s(stats,sb)
    if len(aliens) == 0:

        effect = pygame.mixer.Sound('Music/LevelUp.wav')
        effect.play()
        bullets.empty()
        Invad_set.inc_speed()

        stats.level +=1
        sb.level_f()
        time.sleep(2)
        create_fleet(Invad_set, screen, ship, aliens)
        
def create_fleet(Invad_set, screen,ship, aliens):
    alien = Alien(Invad_set, screen)
    number_aliens_x = get_number_alien_x(Invad_set, alien.rect.width)
    number_rows = get_number_rows(Invad_set, ship.rect.height, alien.rect.height)
    

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(Invad_set, screen, aliens, alien_number, row_number)
       
def get_number_alien_x(Invad_set, alien_width):
    available_space_x = Invad_set.width - (2*alien_width)
    number_aliens_x= int(available_space_x / (1*alien_width))
    return number_aliens_x

def create_alien(Invad_set, screen, aliens, alien_number, row_number):
    alien = Alien(Invad_set, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + (1 * alien_width * alien_number)
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + (1 * alien.rect.height * row_number)
    aliens.add(alien)

def get_number_rows(Invad_set, ship_height, alien_height):
    available_space_y = (Invad_set.height - (1* alien_height) - ship_height)
    number_rows = int(available_space_y  / (2* alien_height))
    return number_rows

def check_fleet_edges(Invad_set, aliens):
    for alien in aliens.sprites():
        if alien.check_edges(Invad_set):
            change_fleet_dirc(Invad_set, aliens)
            break
        
def change_fleet_dirc(Invad_set, aliens):
    for alien in aliens.sprites():
        alien.rect.y += Invad_set.fleet_drop_speed
    Invad_set.fleet_dir *= -1
    
def ship_hit(Invad_set,stats,sb,screen,ship,aliens,bullets):
    
    if stats.ships_left >0:
        effect = pygame.mixer.Sound('Music/LostLife.wav')
        effect.play()
        stats.ships_left -= 1
        sb.prep_ship()
        aliens.empty()
        bullets.empty()
        create_fleet(Invad_set, screen,ship,aliens)
        ship.center
        time.sleep(2)
    else:
        effect = pygame.mixer.Sound('Music/GameOver.wav')
        effect.play()
        sb.high_score_board()
        time.sleep(10)
        
        stats.game_active = False
        pygame.mouse.set_visible(True)
        
    
def check_aliens_bottom(Invad_set,stats,sb,screen, ship,aliens,bullets):
    if Invad_set.s_active == True:
        screen_rect = screen.get_rect()
        for alien in aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                ship_hit(Invad_set,stats,sb,screen,ship,aliens,bullets)
                break
    else:
        pass
    
def update_aliens(Invad_set,stats,sb,screen,ship,aliens,bullets):
    check_fleet_edges(Invad_set, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(Invad_set,stats,sb,screen,ship,aliens,bullets)
    check_aliens_bottom(Invad_set,stats,sb,screen,ship,aliens,bullets)

def check_high_s(stats,sb):
    if stats.score> stats.high_score:
        stats.high_score = stats.score
        sb.F_high_score()
        
