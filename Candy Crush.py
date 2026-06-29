import math
import pygame

class Square:
    def __init__(self, screen, squaresize):
        self.screen= screen
        self.hitbox= pygame.rect.Rect(0,0, squaresize, squaresize)
        self.color= (0,0,0)
        self.candy= None
        self.is_highlighted= False

class Matriz:
    def __init__(self, screen, height, lenght, squaresize):
        self.screen= screen
        self.height= height
        self.lenght= lenght
        self.squaresize= squaresize
        self.matriz= []
        self.rows= math.floor(lenght/squaresize)
        self.columns= math.floor(height/squaresize)
        self.points=0
        for row in range(self.rows):
            line= []
            for column in range(self.columns):
                line.append(Square(self.screen, self.squaresize))
            self.matriz.append(line)

    def define_matriz(self):
        for row in range(len(self.matriz)):
            for column in range(len(self.matriz[row])):
                bloco= self.matriz[row][column]
                bloco.hitbox.top= self.squaresize*column
                bloco.hitbox.left= self.squaresize*row
                
    def draw_matriz(self):
        for row in range(len(self.matriz)):
            for bloco in self.matriz[row]:
                if not bloco.is_highlighted:
                    pygame.draw.rect(self.screen, bloco.color, bloco.hitbox)
                else:
                    pygame.draw.rect(self.screen, (0,251,0), bloco.hitbox)

    def get_square(self):
        mouse_pos1= mouse_pos()
        x, y= mouse_pos1[0] , mouse_pos1[1]
        
        coluna= math.floor(x/self.squaresize)
        if x%self.squaresize > 0:
            coluna+=1
        
        fila= math.floor(y/self.squaresize)
        if  y%self.squaresize > 0:
            fila+=1
        return [coluna-1,fila-1]
    
    def highlight_space(self, square_pos):
        try:
            x= square_pos[0] #x do quadrado analisado
            y= square_pos[1] #y do quadrado analisado
            self.matriz[x][y].is_highlighted= True #visualmente, mostra o espaço q irá ser ocupado
        except:
            pass

    def dehighlight_everything(self):
        for row in range(len(self.matriz)):
            for bloco in self.matriz[row]:
                bloco.is_highlighted= False

    def check_points(self):
        blocks_destroyed=0
        for column in range(len(self.matriz)): #analisar colunas
            pass

        for row in range(len(self.matriz[0])): #analisar as filas
            pass
        
        self.points+= 10 * blocks_destroyed**2 #se destruir, por exemplo, 4 blocos na mesma jogada, ganha 10*4**2, ou seja 160 pontos

def mouse_pos():
    return pygame.mouse.get_pos()

def game_ended(points):
    relativesize= round(ScreenWidth/30)
    background= pygame.rect.Rect(0, 0, ScreenWidth, ScreenWidth)
    hitbox= pygame.rect.Rect(midx- relativesize*7, midy-relativesize, relativesize*18, relativesize*2)
    font = pygame.font.Font('freesansbold.ttf', relativesize)
    text = font.render(("Game Lost :( You got "+ points + " points"), 1, (255,255,255))
    pygame.draw.rect(screen, preto, background)
    pygame.draw.rect(screen, preto, hitbox)
    screen.blit(text, hitbox)

def inside_game(coluna, fila, colunamax, filamax):
    if coluna > 1 and coluna < colunamax and fila > -1 and fila < filamax:
        return True
    else: 
        return False
pygame.init()

squaresize= 50
ScreenWidth= 500
ScreenHeight= ScreenWidth-squaresize*2
midx= round(ScreenWidth/2)
midy= round(ScreenHeight/2)
screen= pygame.display.set_mode((ScreenWidth,ScreenHeight))

preto=(0,0,0)

matriz= Matriz(screen, ScreenHeight, ScreenWidth, squaresize)
matriz.define_matriz()

mouse_down= False
game_lost= False
selectdelay= 0
square_selected= None

running=True
while running:

    for event in pygame.event.get():
       if event.type==pygame.QUIT:
           running=False
       elif event.type == pygame.KEYUP:
           pass
       elif event.type == pygame.MOUSEBUTTONUP:
           mouse_down= False
       elif event.type == pygame.MOUSEBUTTONDOWN and event.button==1: #carregou com o botão esquerdo
           mouse_down= True
           eventbutton= 1
    
    screen.fill(preto)
    pygame.display.set_caption("Candy Crush    Pontuação: " + str(matriz.points))

    matriz.draw_matriz() #desenha a matriz
    matriz.check_points() #atualizar os pontos se houver 3, 4 ou 5 em linha

    print(square_selected)
    try:
        print(square_selected.is_highlighted)
    except:
        pass
    if square_selected != None: #se está a segurar um bloco, este deve seguir o rato e a sua posição
        #x,y= mouse_pos()
        pass
    else:
        matriz.dehighlight_everything()
    
    #delay de selecionar os blocos
    if selectdelay > 0:
        selectdelay-=1
    
    if mouse_down: #se um botão do rato está a ser pressionado
        if eventbutton == 1 and selectdelay == 0: #se for o esquerdo
            selectdelay+=200
            mouse= mouse_pos() #posição do rato
            mouse_rect= pygame.Rect(mouse[0], mouse[1], 1, 1)
            for row in range(len(matriz.matriz)):
                for square in matriz.matriz[row]:
                    if square.hitbox.colliderect(mouse_rect): #se o rato está a colidir com o quadrado
                        if square_selected != None: #se já houver outro quadrado selecionado
                            matriz.dehighlight_everything()
                            square_selected= None
                            #matriz.perform_swap()
                            pass
                        else: #se n havia nenhum quadrado selecionado, destacar este
                            matriz.highlight_space(matriz.get_square())
                            square_selected= square
    
    if game_lost:
        print("Game lost")
        pygame.time.delay(6000)
        game_ended(str(matriz.points))