# -*- coding: utf-8 -*-
import math
import pygame
from My_math import distance_between_points
pygame.init()
pygame.display.set_caption("Shaders")

class Player:
    def __init__(self, color, screen):
        self.color= color
        self.screen= screen
        self.size= [20,20]
        self.hitbox= pygame.Rect(midx,midy,self.size[0],self.size[1])
        i=90
        self.shadow= (i,i,i)
        self.radius= 10000
    
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.hitbox)
        
    def update_pos(self):
        key1= pygame.key.get_pressed()
        if key1[pygame.K_w]:
            self.hitbox.move_ip(0,-1)
        if key1[pygame.K_d]:
            self.hitbox.move_ip(1,0)
        if key1[pygame.K_s]:
            self.hitbox.move_ip(0,1)
        if key1[pygame.K_a]:
            self.hitbox.move_ip(-1,0)
            
    def lantern(self):
        #pygame.draw.circle(self.screen, self.shadow, self.hitbox.center, self.radius)
        walls= wallmaker.getwalls()
        if len(walls)!=0:
            for line in walls:
                coords=[line[0],line[1],self.hitbox.center]
                
                #calcular os angulos entre o jogador e os "cantos" da parede
                angle1= angle(coords[0], coords[2])
                angle2= angle(coords[1], coords[2])
                
                #definir o fim das linhas
                end1= define_end(angle1,self.radius)
                end2= define_end(angle2,self.radius)
                
                #desenhar as linhas
                #pygame.draw.line(self.screen,self.color,end1,coords[2])
                #pygame.draw.line(self.screen,self.color,end2,coords[2])
                
                if distance_between_points(line[0], self.hitbox.center) <= self.radius/15 \
                    and distance_between_points(line[1], self.hitbox.center) <= self.radius/15:
                    pygame.draw.polygon(self.screen, (0,0,0), (end1, line[0], line[1], end2))
                
        
            
class Wallmaker:
    def __init__(self, color, screen):
        self.color= color
        self.screen= screen
        self.drawing= False
        self.start= (0,0)
        self.end= (0,0)
        self.lines= []
        
    def checkdrawing(self):
        mouse_pos= mousepos()
        if self.drawing:
            self.end= mouse_pos
            self.lines.append([self.start,self.end])
            self.drawing= False
        
        else:
            self.start= mouse_pos
            self.drawing= True
            
    def isdrawing(self):
        if self.drawing:
            pygame.draw.line(self.screen,self.color,self.start,mousepos())
        
        #font = pygame.font.Font('freesansbold.ttf', 30)
        for coord in self.lines:
            pygame.draw.line(self.screen,self.color,coord[0],coord[1])
            
            #declive= str( angle(coord[0], coord[1]) )
            #text = font.render(declive, 1, self.color)
            #self.screen.blit(text, coord[0])
            
    def getwalls(self):
        return self.lines

def mousepos():
    return pygame.mouse.get_pos()
 
def angle(ponto, player):
    distance_x= ponto[0]-player[0]
    distance_y= ponto[1]-player[1]
    angle= math.atan2(distance_y, distance_x)
    return float(angle)

def define_end(angle,radius):
    #definir ponto até onde a linha q será da luz chega
    end_x= math.cos(angle)*radius
    end_y= math.sin(angle)*radius
    
    #posição final
    end= (end_x, end_y)
    
    return end

def check_collision_lines(walls,player,testline):
    for line in walls:
        ponto1= line[0]
        ponto2= line[1]
        
        xtl1= testline[0][0]
        ytl1= testline[0][1]
        xtl2= testline[1][0]
        ytl2= testline[1][1]
        
        #if (xpl< ponto1[0] and ponto1[0]< testline[0]) and :

def Render_Text(what, color, where, additional_text): #mostra os fps na srceen
    font = pygame.font.Font('freesansbold.ttf', 30)
    text = font.render(additional_text+what, 1, color)
    screen.blit(text, where)

#fullscreen, alt+f4 para sair
ScreenWidth= 1500
ScreenHeight= 750
midx= round(ScreenWidth/2)
midy= round(ScreenHeight/2)
screen= pygame.display.set_mode((ScreenWidth,ScreenHeight))

preto= (0,0,0)
red= (255,0,0)
blue=(0,0,255)
gray= (90, 90, 90)

player= Player(red, screen)

wallmaker=Wallmaker(blue, screen)

running=True
while running:
    
    screen.fill(gray)

    #jogador
    player.lantern()
    player.update_pos()
    player.draw()
                
    #ver se está a criar uma parede ou não E desenha todas as paredes já criadas
    wallmaker.isdrawing()
    
    for event in pygame.event.get():
       if event.type==pygame.QUIT:
           running=False
       elif event.type == pygame.KEYUP:
           pass
       elif event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
           wallmaker.checkdrawing()
       elif event.type == pygame.MOUSEBUTTONDOWN and event.button==2:
           mouse= mousepos()
           retangulo= pygame.Rect(mouse[0],mouse[1],10,10)
           pygame.draw.rect(screen, red, retangulo)
           
    pygame.display.update()
    
pygame.quit()