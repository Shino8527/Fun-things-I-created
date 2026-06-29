# -*- coding: utf-8 -*-
import pygame
pygame.init()
pygame.display.set_caption("Arcanoid")

class Ball:
    def __init__(self, radius, color, screen):
        self.color= color
        self.screen= screen
        self.radius= radius
        self.diam= self.radius*2
        self.hitbox= pygame.Rect(midx-self.radius,midy-self.radius,self.diam,self.diam)
        self.vel= -1
        self.aumx= self.vel
        self.aumy= self.vel
        
    def move(self):
        self.hitbox.x += self.aumx
        self.hitbox.y += self.aumy
        self.hitbox.move_ip(self.aumx, self.aumy)
        
    def draw(self):
        #pygame.draw.rect(self.screen, (0,255,0), self.hitbox)
        pygame.draw.circle(self.screen, self.color, self.hitbox.center, self.radius)
        
    def check_collisions(self):
        if self.hitbox.centery - self.radius <= 0:#cima
            self.aumy *= -1
            
        #lado direito ou esquerdo
        if self.hitbox.centerx + self.radius >= ScreenWidth or self.hitbox.centerx - self.radius <= 0:
            self.aumx *= -1
        
        if self.hitbox.centery + self.radius >= ScreenHeight:#baixo
            self.reset()
            
        if pygame.Rect.colliderect(self.hitbox,player.hitbox):
            self.aumy *= -1
        
    def reset(self):
        self.hitbox.centerx=midx
        self.hitbox.centery=midy
        self.hitbox= pygame.Rect(self.hitbox.top, self.hitbox.left, self.diam, self.diam)
        self.aumx= self.vel
        self.aumy= self.vel
      
class Player:
    def __init__(self, size, color, screen):
        self.size= size
        self.color= color
        self.screen= screen
        self.hitbox= pygame.Rect(ScreenHeight-self.size[0], midx, self.size[0], self.size[1])
        
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.hitbox)
        
    def update_pos(self):
        self.hitbox.centerx= mousepos()[0]
        
def mousepos():
    return pygame.mouse.get_pos()

class Block:
    def __init__(self, size, color, screen, pos):
        self.size= size
        self.color= color
        self.screen= screen
        self.pos= pos
        self.hitbox= pygame.Rect(pos[1]-size[1], pos[0]-size[0], size[0], size[1])
    
    def colliding_with_ball(self, ball):
        if pygame.Rect.colliderect(self.hitbox , ball.hitbox):
            return True

ScreenWidth= 1500
ScreenHeight= 800
midx= round(ScreenWidth/2)
midy= round(ScreenHeight/2)
screen= pygame.display.set_mode((ScreenWidth,ScreenHeight))

preto=(0,0,0)
red= (255,0,0)

#ball
ball= Ball(20,red,screen)

#player
player= Player((150,20), red, screen)
player_is_controlled= 1

clock= pygame.time.Clock()

running=True
while running:
    
    screen.fill(preto)
    
    clock.tick(300)
    
    #player
    player.draw()
    if player_is_controlled > 0:
        player.update_pos()
    
    #ball
    ball.move()
    ball.check_collisions()
    ball.draw()
    
    for event in pygame.event.get():
       if event.type==pygame.QUIT:
           running=False
       elif event.type == pygame.KEYUP:
           pass
       elif event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
           player_is_controlled*= -1
    
    pygame.display.update()
    
pygame.quit()