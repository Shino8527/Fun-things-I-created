import pygame

class Button:
    def __init__(self, screen,  left, top, width, height, color, text, textsize):
        self.screen= screen
        self.hitbox= pygame.rect.Rect(left, top, width, height)
        self.color= color
        self.color_of_text= (255-self.color[0], 255-self.color[1], 255-self.color[2])
        self.text= text
        self.textsize= textsize
    
    def mousepos(self):
        return pygame.mouse.get_pos()
    
    def Render_Text(self, what, color, where, additional_text, textsize): #mostra o texto no botão
        font = pygame.font.Font('freesansbold.ttf', textsize)
        text = font.render(additional_text+what, 1, pygame.Color(color))
        self.screen.blit(text, where)

    def check_if_clicked(self):
        pos_rato= self.mousepos()
        rato= pygame.rect.Rect(pos_rato[0], pos_rato[1], 1, 1)
        if pygame.Rect.colliderect(rato, self.hitbox):
            return True
    
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.hitbox)
        self.Render_Text(self.text, self.color_of_text, self.hitbox, "", self.textsize)

def Render_Text(screen, what, color, where, additional_text, textsize): #mostra o texto no botão
        font = pygame.font.Font('freesansbold.ttf', textsize)
        text = font.render(additional_text+what, 1, pygame.Color(color))
        screen.blit(text, where)

def mouse_pos():
    return pygame.mouse.get_pos()