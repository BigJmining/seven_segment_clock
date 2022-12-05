#!/usr/bin/env python3
# by Jason Lohrey

import pygame
import os
import datetime


pygame.init()

cwd = os.getcwd()

clock = pygame.time.Clock()

SCREEN_WIDTH = 375
SCREEN_HEIGHT = 450

window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Seven Segment Clock")

BG_color = (0,0,0)
seg_color = (255,0,0)

clock_face = pygame.image.load(os.path.join(cwd,'images','clock_face.png')).convert_alpha()
clock_hand_vert = pygame.image.load(os.path.join(cwd,'images','clock_hand.png')).convert_alpha()
clock_hand_horz = pygame.transform.rotate(clock_hand_vert,90)
clock_hand_dot = pygame.image.load(os.path.join(cwd,'images','clock_dot.png')).convert_alpha()


class CLOCK:
    def __init__(self):
        self.name = 'clock'
        self.segments_count = 7
        self.seg_1 = False
        self.seg_2 = False
        self.seg_3 = False
        self.seg_4 = False
        self.seg_5 = False
        self.seg_6 = False
        self.seg_7 = False
        self.seg_dot = False

    def pass_the_time(self):
        
        time_now = (datetime.datetime.now().strftime("%S"))
        
        # digits = time_now.split()
        # print(digits, time_now)
        # hour1 = digits[0][-1]
        hour1 = time_now[-1]
        if hour1 == "1":
            self.seg_1 = 0
            self.seg_2 = 0
            self.seg_3 = 0
            self.seg_4 = 0
            self.seg_5 = 0
            self.seg_6 = 1
            self.seg_7 = 1
            self.seg_dot = 0
        elif hour1 == "2":
            self.seg_1 = 0
            self.seg_2 = 1
            self.seg_3 = 1
            self.seg_4 = 1
            self.seg_5 = 1
            self.seg_6 = 1
            self.seg_7 = 0
            self.seg_dot = 0
        elif hour1 == "3":
            self.seg_1 = 0
            self.seg_2 = 0
            self.seg_3 = 1
            self.seg_4 = 1
            self.seg_5 = 1
            self.seg_6 = 1
            self.seg_7 = 1
            self.seg_dot = 0
        elif hour1 == "4":
            self.seg_1 = 1
            self.seg_2 = 0
            self.seg_3 = 0
            self.seg_4 = 1
            self.seg_5 = 0
            self.seg_6 = 1
            self.seg_7 = 1
            self.seg_dot = 0
        elif hour1 == "5":
            self.seg_1 = 1
            self.seg_2 = 0
            self.seg_3 = 1
            self.seg_4 = 1
            self.seg_5 = 1
            self.seg_6 = 0
            self.seg_7 = 1
            self.seg_dot = 0
        elif hour1 == "6":
            self.seg_1 = 1
            self.seg_2 = 1
            self.seg_3 = 1
            self.seg_4 = 1
            self.seg_5 = 1
            self.seg_6 = 0
            self.seg_7 = 1
            self.seg_dot = 0
        elif hour1 == "7":
            self.seg_1 = 0
            self.seg_2 = 0
            self.seg_3 = 1
            self.seg_4 = 0
            self.seg_5 = 0
            self.seg_6 = 1
            self.seg_7 = 1
            self.seg_dot = 0
        elif hour1 == "8":
            self.seg_1 = 1
            self.seg_2 = 1
            self.seg_3 = 1
            self.seg_4 = 1
            self.seg_5 = 1
            self.seg_6 = 1
            self.seg_7 = 1
            self.seg_dot = 0
        elif hour1 == "9":
            self.seg_1 = 1
            self.seg_2 = 0
            self.seg_3 = 1
            self.seg_4 = 1
            self.seg_5 = 1
            self.seg_6 = 1
            self.seg_7 = 1
            self.seg_dot = 0
        elif hour1 == "0":
            self.seg_1 = 1
            self.seg_2 = 1
            self.seg_3 = 1
            self.seg_4 = 0
            self.seg_5 = 1
            self.seg_6 = 1
            self.seg_7 = 1
            self.seg_dot = 1
        return


    def draw(self,window):
        window.blit(clock_face,(0,0))
        self.pass_the_time()
        
        if (self.seg_1):
            window.blit(clock_hand_vert,(50,50))    # left top
        if (self.seg_2):
            window.blit(clock_hand_vert,(50,250))   # left btm
        if (self.seg_3):
            window.blit(clock_hand_horz,(110,15))   # top
        if (self.seg_4):
            window.blit(clock_hand_horz,(110,200))   # middle
        if (self.seg_5):
            window.blit(clock_hand_horz,(110,385))   # btm
        if (self.seg_6):
            window.blit(clock_hand_vert,(270,50))   # right top
        if (self.seg_7):
            window.blit(clock_hand_vert,(270,250))   # right btm
        if (self.seg_dot):
            window.blit(clock_hand_dot,(322,390))   # dot
       
        pygame.display.update()    

def redrawscreen():
    C.draw(window)


C = CLOCK()

run = True
while run:
    clock.tick(27)
    
    # event detection
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_g]:
        print('GO key pressed')
    if keys[pygame.K_s]:
        print('STOP key pressed')

    if keys[pygame.K_q]:
        run = False

    for event in pygame.event.get():
        if event == pygame.QUIT:
            run = False

    # collision detection

    # redraw screen
    redrawscreen()

pygame.quit()    