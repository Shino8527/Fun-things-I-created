# -*- coding: utf-8 -*-
import pygame
pygame.init()
pygame.display.set_caption("G-Man")

def Render_Text(what, color, where, additional_text): #mostra os fps na srceen
    font = pygame.font.Font('freesansbold.ttf', 30)
    text = font.render(additional_text+what, 1, pygame.Color(color))
    screen.blit(text, where)
    
ScreenWidth= 1500
ScreenHeight= 750
midx= round(ScreenWidth/2)
midy= round(ScreenHeight/2)
screen= pygame.display.set_mode((ScreenWidth,ScreenHeight))

#jogador
altura=50
x=midx
y=midy-altura/2
player1= pygame.Rect(x,y,20,altura)
velman=1
playervel=0
playervelmax=20
change=True
changetimer=0
clicka=True
clickd=True

#chão
floorsize=10
floor= pygame.Rect(0,ScreenHeight,ScreenWidth,floorsize)

#teto
teto= pygame.Rect(0,-floorsize,ScreenWidth,floorsize)

#plataformas
tamplat=100
plataforma= pygame.Rect(midx+50,midy,tamplat,10)

#paredes
tamparede=50
widthparede=5
paredeesq= pygame.Rect(400,ScreenHeight-tamparede,widthparede,tamparede)
parededir= pygame.Rect(400+widthparede,ScreenHeight-tamparede,widthparede,tamparede)

#gravidade
grav=10

#salto
salto=-1

#cores
preto=(0,0,0)
branco=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)

#relogio
clock= pygame.time.Clock()

running=True
while running:
    
    screen.fill(preto)
    
    #fps 
    clock.tick(200) #o nr colocado dentro dos parenteses no tick define o limite max de fps
    Render_Text(str(int(clock.get_fps())), branco, (10,10), "FPS: ")
    
    #jogador
    pygame.draw.rect(screen,red,player1)
    playervel+=grav/125
    if playervel>=playervelmax:
        playervel=playervelmax
    if playervel<-playervelmax:
        playervel=-playervelmax
    
    #Render_Text(str(playervel),branco,(200,10))
        
    #chão e teto
    pygame.draw.rect(screen,green,floor)
    pygame.draw.rect(screen,green,teto)
    
    #plataformas
    pygame.draw.rect(screen,green,plataforma)
    
    #parede
    pygame.draw.rect(screen,blue,paredeesq)
    pygame.draw.rect(screen,blue,parededir)
    
    key1= pygame.key.get_pressed()
    
    if key1[pygame.K_a] and clicka:
        player1.move_ip(-velman,0)
    if key1[pygame.K_d] and clickd:
        player1.move_ip(velman,0)
    if key1[pygame.K_e] and change:
        grav*=-1
        change=False
        if not pygame.Rect.colliderect(floor,player1) and not pygame.Rect.colliderect(teto,player1):
            if playervel<0:
                playervel+=2
            else:
                playervel-=2
    
    if not change:
        changetimer+=1
    if changetimer==100:
        change=True
        changetimer=0
    
    if pygame.Rect.colliderect(floor,player1):
        playervel=0
        if key1[pygame.K_e]:
            player1.move_ip(0,salto)
    elif pygame.Rect.colliderect(teto,player1):
        playervel=0
        if key1[pygame.K_e]:
            player1.move_ip(0,-salto)
    elif pygame.Rect.colliderect(plataforma,player1):
        playervel=0
        if key1[pygame.K_e]:
            if grav<=0:
                player1.move_ip(0,salto)
            else:
                player1.move_ip(0,-salto)
    if pygame.Rect.colliderect(paredeesq,player1):
        if player1.right>=paredeesq.left:
            clickd=False
    else:
        clickd=True
        
    if pygame.Rect.colliderect(parededir,player1):
        if player1.left<=parededir.right:
            clicka=False
    else:
        clicka=True
        
            
    
    player1.move_ip(0,playervel)
        
    for event in pygame.event.get():
       if event.type==pygame.QUIT:
           running=False
   
    pygame.display.update()

pygame.quit()