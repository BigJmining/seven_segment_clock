#!/usr/bin/env python3
# by Jason Lohrey

import pygame
import os
import datetime


pygame.init()

cwd = os.getcwd()

clock = pygame.time.Clock()

SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 450

window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Seven Segment Clock")


clock_face = pygame.image.load(os.path.join(cwd,'images','clock_face.png')).convert_alpha()
clock_hand_vert = pygame.image.load(os.path.join(cwd,'images','clock_hand.png')).convert_alpha()
clock_hand_horz = pygame.transform.rotate(clock_hand_vert,90)
clock_hand_dot = pygame.image.load(os.path.join(cwd,'images','clock_dot.png')).convert_alpha()

OFFSET = 285
GAP = 60
FPS = 60

class CLOCK:
    def __init__(self):
        self.name = 'clock'
        

    def pass_the_time(self):
        
        time_now = (datetime.datetime.now().strftime("%H%M"))
       
        digit_1 = time_now[0]
        digit_2 = time_now[1]
        digit_3 = time_now[2]
        digit_4 = time_now[3]
        # digit_5 = time_now[3]
        # digit_6 = time_now[3]
        digits = [digit_1, digit_2, digit_3, digit_4]#, digit_5, digit_6]
       
        clock_digits = {
                '1': [0,0,0,0,0,1,1,0],
                '2': [0,1,1,1,1,1,0,0], 
                '3': [0,0,1,1,1,1,1,0],
                '4': [1,0,0,1,0,1,1,0],
                '5': [1,0,1,1,1,0,1,0],
                '6': [1,1,1,1,1,0,1,0],
                '7': [0,0,1,0,0,1,1,0],
                '8': [1,1,1,1,1,1,1,0],
                '9': [1,0,1,1,1,1,1,0],
                '0': [1,1,1,0,1,1,1,0]}

        digits_to_display = [clock_digits[digits[x]] for x in range(len(digits))]
            
        return digits_to_display    


    def draw(self,window):
        window.blit(clock_face,(0,0))

        digits = self.pass_the_time()
        # print(digits)
        
        if digits[0][0]:
            window.blit(clock_hand_vert,(50,50))                # left top
        if digits[0][1]:
            window.blit(clock_hand_vert,(50,250))               # left btm
        if digits[0][2]:
            window.blit(clock_hand_horz,(110,15))               # top
        if digits[0][3]:
            window.blit(clock_hand_horz,(110,200))               # middle
        if digits[0][4]:
            window.blit(clock_hand_horz,(110,385))              # btm
        if digits[0][5]:
            window.blit(clock_hand_vert,(270,50))               # right top
        if digits[0][6]:
            window.blit(clock_hand_vert,(270,250))              # right btm
        if digits[0][7]:
            window.blit(clock_hand_dot,(322,390))               # dot

        if digits[1][0]:
            window.blit(clock_hand_vert,(50+OFFSET,50))         # left top
        if digits[1][1]:
            window.blit(clock_hand_vert,(50+OFFSET,250))        # left btm
        if digits[1][2]:
            window.blit(clock_hand_horz,(110+OFFSET,15))        # top
        if digits[1][3]:
            window.blit(clock_hand_horz,(110+OFFSET,200))        # middle
        if digits[1][4]:
            window.blit(clock_hand_horz,(110+OFFSET,385))       # btm
        if digits[1][5]:
            window.blit(clock_hand_vert,(270+OFFSET,50))        # right top
        if digits[1][6]:
            window.blit(clock_hand_vert,(270+OFFSET,250))       # right btm
        if digits[1][7]:
            window.blit(clock_hand_dot,(322+OFFSET,390))        # dot

        pygame.draw.circle(window,(111,111,111),(SCREEN_WIDTH //2 -12,125),20)
        pygame.draw.circle(window,(111,111,111),(SCREEN_WIDTH //2 -12,275),20)

        if digits[2][0]:
            window.blit(clock_hand_vert,(50+GAP+(OFFSET*2),50))     # left top
        if digits[2][1]:
            window.blit(clock_hand_vert,(50+GAP+(OFFSET*2),250))    # left btm
        if digits[2][2]:
            window.blit(clock_hand_horz,(110+GAP+(OFFSET*2),15))    # top
        if digits[2][3]:
            window.blit(clock_hand_horz,(110+GAP+(OFFSET*2),200))    # middle
        if digits[2][4]:
            window.blit(clock_hand_horz,(110+GAP+(OFFSET*2),385))   # btm
        if digits[2][5]:
            window.blit(clock_hand_vert,(270+GAP+(OFFSET*2),50))    # right top
        if digits[2][6]:
            window.blit(clock_hand_vert,(270+GAP+(OFFSET*2),250))   # right btm
        if digits[2][7] :
            window.blit(clock_hand_dot,(322+GAP+(OFFSET*2),390))    # dot    

        if digits[3][0]:
            window.blit(clock_hand_vert,(50+GAP+(OFFSET*3),50))     # left top
        if digits[3][1]:
            window.blit(clock_hand_vert,(50+GAP+(OFFSET*3),250))    # left btm
        if digits[3][2]:
            window.blit(clock_hand_horz,(110+GAP+(OFFSET*3),15))    # top
        if digits[3][3]:
            window.blit(clock_hand_horz,(110+GAP+(OFFSET*3),200))    # middle
        if digits[3][4]:
            window.blit(clock_hand_horz,(110+GAP+(OFFSET*3),385))   # btm
        if digits[3][5]:
            window.blit(clock_hand_vert,(270+GAP+(OFFSET*3),50))    # right top
        if digits[3][6]:
            window.blit(clock_hand_vert,(270+GAP+(OFFSET*3),250))   # right btm
        if digits[3][7]:
            window.blit(clock_hand_dot,(322+GAP+(OFFSET*3),390))    # dot

        
        pygame.display.update()    

def redrawscreen():
    C.draw(window)


C = CLOCK()

run = True
while run:
    clock.tick(FPS)
    
    # event detection
    keys = pygame.key.get_pressed()

    if keys[pygame.K_q]:
        run = False

    for event in pygame.event.get():
        if event == pygame.QUIT:
            run = False

    # collision detection

    # redraw screen
    redrawscreen()

pygame.quit()    