import pygame
from pygame.sprite import Group
from ship import Ship
import mysql.connector as mycon
class Score():
    def __init__(self, Invad_set, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.Invad_set = Invad_set
        self.stats = stats
        #Properties Of Text 
        self.t_color =(47, 255, 0)
        self.bg_color=(0,0,0)
        self.font = pygame.font.SysFont("Times New Roman", 50) #comicsansms

        self.F_score()
        self.F_high_score()
        self.level_f()
        self.prep_ship()

    def F_score(self):
        #Current Score
        self.r_score = int(round(self.stats.score, -1))
        self.scores =  "{:,}".format(self.r_score)
        self.score_image = self.font.render(self.scores, True, self.t_color, self.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        #Displaying Score in the window
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

        self.d_image = self.font.render("P:Pause",True,self.t_color, self.bg_color)
        self.d_rect = self.d_image.get_rect()
        self.d_rect.left = self.screen_rect.left +20
        self.d_rect.top = 550
        self.r_image = self.font.render("R:Resume",True,self.t_color, self.bg_color)
        self.r_rect = self.r_image.get_rect()
        self.r_rect.left = self.d_rect.left
        self.r_rect.bottom = self.d_rect.bottom + 70
        
        self.screen.blit(self.d_image, self.d_rect)
        self.screen.blit(self.r_image, self.r_rect)
        for i in range(self.stats.ships_left + 1):
            self.screen.blit(self.sh, self.ship_rect)

        
    def F_high_score(self):
        #Global High Score
        high_score  = int(round(self.stats.high_score, -1))
        high_score_s = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_s, True, self.t_color, self.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
       # self.high_score_board()
        
    def level_f(self):
        #Current Level
        self.level_image = self.font.render(str(self.stats.level),True, self.t_color, self.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ship(self):
        #Ships left
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            self.ship = Ship(self.Invad_set, self.screen)
            self.sh = pygame.image.load('img/ship.bmp') 
            self.ship_rect = self.sh.get_rect()
            self.ship_wid = self.sh.get_width()
            self.ship_rect.left = self.screen_rect.left 
            self.ship_rect.top = self.score_rect.top
            self.ship.rect_x = 10 + (ship_number * self.ship_wid)
            self.ship.rect_y = 10
            self.ships.add(self.ship)

    def high_score_board(self):
        #Score Board
        mydb = mycon.connect(host = "localhost",user = "root",passwd = "ROOTLAP",
                             database = "kevin_the_cube")
        cur = mydb.cursor()
        h_sc = cur.fetchone()
        cur.execute("select * from High_Score")
        h_sc = cur.fetchall()
        b=str(input("Enter Your Name: "))
        a=0
        print(h_sc)
        c=self.r_score
        for row in h_sc:
            if row[-1] >= c:
                a=row[0]
                print("check 1")
                continue
            elif row[-1] < c:
                a= row[0]
                print("check 1.1")
                break
        print(4)
        if a!=0:
            s = "INSERT INTO High_Score(Rank_,Name_,Score) VALUES({},'{}',{})".format(a,b,c)
            aa= "update High_Score set Rank_ =Rank_ + {} where Rank_ < {};".format(1,a)
            cur.execute(aa)
            mydb.commit()
            cur.execute(s)
            mydb.commit()
            print("check 2.1")
            
        else:
            s = "INSERT INTO High_Score(Rank_,Name_,Score) VALUES({},'{}',{})".format(a+1,b,c)
            cur.execute(s)
            mydb.commit()
            print("check 2.2")
        cur.execute("select * from High_Score")
        h_sc = cur.fetchall()
        print("check 3")
        for row in h_sc:
            print(row)
        mydb.close()
        
            
        
