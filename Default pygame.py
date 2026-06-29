# -*- coding: utf-8 -*-
import pygame
pygame.init()
pygame.display.set_caption("Titulo")

#fullscreen, alt+f4 para sair
ScreenWidth= 1500
ScreenHeight= 800
midx= round(ScreenWidth/2)
midy= round(ScreenHeight/2)
screen= pygame.display.set_mode((ScreenWidth,ScreenHeight))

preto=(0,0,0)

running=True
while running:
    screen.fill(preto)
    
    for event in pygame.event.get():
       if event.type==pygame.QUIT:
           running=False
    
    pygame.display.update()
    
pygame.quit()