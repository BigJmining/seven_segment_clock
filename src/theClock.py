#!/usr/bin/env python3
# by Jason Lohrey

import pygame
import os


pygame.init()

cwd = os.getcwd()

clock = pygame.time.Clock()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Seven Segment Clock")

BG_color = (0,0,0)
seg_color = (255,0,0)

clock_face = pygame.image.load(os.path.join(cwd,'images','clock_face')).convert_alpha()
clock_hand = pygame.image.load(os.path.join(cwd,'images','clock_hand')).convert_alpha()


run = True
while run:
    clock.tick(27)
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

pygame.quit()    