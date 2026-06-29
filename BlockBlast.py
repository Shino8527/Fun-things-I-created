import pygame
import math
import random

class Square:
    def __init__(self, screen, squaresize):
        self.screen= screen
        self.hitbox= pygame.rect.Rect(0,0, squaresize, squaresize)
        self.color= (0,0,0)
        self.has_block= False
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
                    pygame.draw.rect(self.screen, (152,251,152), bloco.hitbox)

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
    
    def check_points(self):
        lines_destroyed=0
        for column in range(len(self.matriz)): #analisar colunas
            occupied_spaces=0
            for bloco in self.matriz[column]:
                if bloco.has_block:
                    occupied_spaces+=1
            if occupied_spaces == len(self.matriz[column]): #se a coluna estiver completa
                lines_destroyed+= 1
                for bloco in self.matriz[column]: #apagar todos os blocos q estejam nessa coluna
                    bloco.color=(0,0,0)
                    bloco.has_block= False

        for column in range(len(self.matriz[0])): #analisar as filas
            occupied_spaces=0
            for row in range(len(self.matriz)):
                if self.matriz[row][column].has_block:
                    occupied_spaces+=1
            if occupied_spaces == len(self.matriz)-2: #se a fila estiver completa
                lines_destroyed+= 1
                for row in range(len(self.matriz)): #apagar todos os blocos q estejam nessa fila
                    self.matriz[row][column].color=(0,0,0)
                    self.matriz[row][column].has_block= False
        
        self.points+= 10 * lines_destroyed**2 #se destruir, por exemplo, 2 filas na mesma jogada, ganha 10*2**2, ou seja 40 pontos em vez de 20

    def place_block(self, block_type, square_pos, color):
        if self.check_if_block_fits(block_type, square_pos): #se a peça couber no espaço dado
            for square in range(len(block_type)):
                x= square_pos[0]+ block_type[square][0] #x do quadrado analisado
                y= square_pos[1]+ block_type[square][1] #y do quadrado analisado
                self.matriz[x][y].has_block= True #o espaço está ocupado
                self.matriz[x][y].color= color #visualmente, mostra q o espaço está ocupado
            self.points+= len(block_type)
            return True
        else:
            return False
    
    def highlight_space(self, block_type, square_pos):
        for square in range(len(block_type)):
            try:
                x= square_pos[0]+ block_type[square][0] #x do quadrado analisado
                y= square_pos[1]+ block_type[square][1] #y do quadrado analisado
                self.matriz[x][y].is_highlighted= True #visualmente, mostra o espaço q irá ser ocupado
            except:
                pass

    def dehighlight_everything(self):
        for row in range(len(self.matriz)):
            for bloco in self.matriz[row]:
                bloco.is_highlighted= False
        
    def check_if_block_fits(self, block_type, square_pos):
        total_squares= len(block_type)
        count= 0 #variável para contar quantos espaços estão vazios
        for square in range(total_squares):
            x= square_pos[0]+ block_type[square][0] #x do quadrado analisado
            y= square_pos[1]+ block_type[square][1] #y do quadrado analisado
            if inside_game(x,y, self.rows, self.columns) and self.matriz[x][y].has_block == False:
                #se o quadrado analisado está dentro da grelha de jogo e está vazio
                count+=1
        return count == total_squares #faz return da veracidade desta afirmação
    
    def check_all_empty_spaces(self, block_type):
        there_is_space= False
        for column in range(len(self.matriz)):
            for row in range(len(self.matriz[column])): #testa em toda as quadriculas
                if self.check_if_block_fits(block_type, (column,row)): #se a peça pode ficar nessa
                    there_is_space= True #se sim ent há espaço para colocar a peça no campo
                    break
        return there_is_space
    
    def print(self):
        for column in range(len(self.matriz[0])):
            line= "|"
            for row in range(len(self.matriz)):
                newcolumn= column
                newrow= row
                if self.matriz[newrow][newcolumn].has_block:
                    line+= "+ "
                else:
                    line+= "  "
            print(line)

        
class Block:
    def __init__(self, screen):
        self.screen= screen
        self.color= (random.randrange(0, 255),random.randrange(0, 255),random.randrange(0, 255))
        self.possibletypes=[ # tipos de blocos possíveis
            ((0,0), (0,0)), # .
            ((0,0), (0,1)), # :
            ((0,0), (1,0)), # ..
            ((0,0), (1,1)), #*.
            ((0,1), (1,0)), #.*
            ((0,0), (1,0), (1,1)), # *:
            ((0,0), (0,1), (1,1)), # :.
            ((0,0), (1,0), (0,1)), # :*
            ((1,0), (0,1), (1,1)), # .:
            ((0,0), (1,0), (1,1), (2,1)), # *:. #
            ((0,0), (0,1), (1,1), (1,2)), # ≒
            ((0,1), (1,0), (2,0), (1,1)), # .:* #
            ((0,2), (0,1), (1,1), (1,0)), # ≓
            ((0,0), (1,0), (0,1), (1,1)), # ::
            ((0,0), (1,0), (0,1), (1,1), (0,2), (2,0), (1,2), (2,1), (2,2)), #quadrado 3x3, 
            ((0,0), (0,1), (0,2)), #3 |
            ((0,0), (1,0), (2,0)), #  ...
            ((0,0), (0,1), (0,2), (0,3)), #4 |
            ((0,0), (1,0), (2,0), (3,0)), # ....
            ((0,0), (1,0), (1,1), (1,2)), # *|
            ((0,2), (1,2), (1,1), (1,0)), # .|
            ((1,0), (0,0), (0,1), (0,2)), # |*
            ((0,0), (0,1), (0,2), (1,2)), # |.
            ((0,0), (1,0), (2,0), (2,1), (2,2)), # **|
            ((0,2), (1,2), (2,2), (2,1), (2,0)), # ..|
            ((0,0), (1,0), (2,0), (0,1), (0,2)), # |**
            ((0,0), (0,1), (0,2), (1,2), (2,2)), # |..
            ((0,0), (0,1), (1,1), (2,1)), # :..
            ((0,0), (0,1), (1,0), (2,0)), # :**
            ((0,0), (2,0), (1,0), (2,1)), # **:
            ((0,1), (1,1), (2,1), (2,0)), # ..:
            ((0,1), (1,1), (2,1), (1,0)), # .:.
            ((0,0), (1,0), (2,0), (1,1)), # *:*
            ((0,0), (0,1), (0,2), (1,1)), # |-
            ((1,0), (1,1), (1,2), (0,1)), # -|
        ]
        self.type= random.choice(self.possibletypes)
        self.hitbox= pygame.Rect(0,0, 100, 100)
    
    def draw(self, x, y, size):
        #tamanho da hitbox dos blocos deve ser desde o inicio do bloco (esquerda e topo) até ao ponto mais distante desse (direita e base)
        self.hitbox.topleft = (x, y)
        #pygame.draw.rect(self.screen, (255, 255, 255), self.hitbox) #desenhar a hitbox
        minx=0 #x mais à esquerda do bloco
        miny=0 #y mais à esquerda do bloco
        maxx=0 #x mais à direita do bloco
        maxy=0 #y mais à direita do bloco
        for square in range(len(self.type)):
            #posição relativa dos quadrados (squares) até à posição inicial
            xrelativo= self.type[square][0] 
            yrelativo= self.type[square][1]
            rect= pygame.Rect(self.hitbox.x + xrelativo*size, self.hitbox.y + yrelativo*size, size-1, size-1) 
            #-1 no tamanho para criar bordas à volta de cada quadrado
            pygame.draw.rect(self.screen, self.color, rect)
            if xrelativo>maxx: #se o "x" deste square é o q está mais à direita, este vai substituir o anterior
                maxx= xrelativo
            elif xrelativo<minx: #se o "x" deste square é o q está mais à esquerda, este vai substituir o anterior
                minx= xrelativo
            if yrelativo>maxy: #se o "y" deste square é o q está mais à direita, este vai substituir o anterior
                maxy= yrelativo
            elif yrelativo<miny: #se o "y" deste square é o q está mais à esquerda, este vai substituir o anterior
                miny= yrelativo
        self.hitbox.width= size*(abs(minx - maxx)+1)
        self.hitbox.height= size*(abs(miny - maxy)+1)
        #+1 nestas contas pq a soma destes tamanhos ^^^^ vai dar 0 se for algo apenas horizontal ou vertical, por exemplo
        #nem a height nem a width n pode ser 0, pq se forem 0, o bloco não vai ter hitbox


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
divider_rect= pygame.Rect(2*squaresize-10, 0, 10, ScreenHeight)

mouse_down= False
game_lost= False
selectdelay= 0
holding_block= False

list_of_blocos= []
for i in range(3):
    bloco= Block(screen)
    list_of_blocos.append(bloco)

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
    pygame.display.set_caption("Block Blast    Pontuação: " + str(matriz.points))

    matriz.draw_matriz() #desenha a matriz e faz return do nr de flags já colocadas
    pygame.draw.rect(screen, "White", divider_rect)
    matriz.check_points() #atualizar os pontos se houver alguma fila ou coluna completa
        
    if holding_block: #se está a segurar um bloco, este deve seguir o rato e a sua posição
        matriz.dehighlight_everything()
        x,y= mouse_pos()
        bloco_held= list_of_blocos[index]
        #seguir a posição do rato
        bloco_held.hitbox.x= x
        bloco_held.hitbox.y= y
        #"pintar" a posição onde a peça irá ficar se for "largada"
        matriz.highlight_space(bloco_held.type, matriz.get_square())
    else:
        matriz.dehighlight_everything()
        tam= len(list_of_blocos)
        if tam > 0: #verificar se o jogo devia terminar
            ponto=0
            for i in range(tam):
                if not matriz.check_all_empty_spaces(list_of_blocos[i].type): #se o bloco n couber em nenhum espaço do campo de jogo
                    ponto+=1
            if ponto == tam: #se nenhuma das peças q estão na "zona de espera" couberem no campo
                game_lost= True #o jogo termina

    #desenhar blocos ou criar novos se os 3 já tiverem sido usadas
    if tam > 0:
        for i in range(tam):
            bloco= list_of_blocos[i]
            if holding_block and i == index: #se está a segurar um bloco e é este "list_of_blocos[i]"
                bloco.draw(bloco.hitbox.x, bloco.hitbox.y, 20) #esse bloco segue o rato
            else: #se não, desenha o na "zona de espera"
                bloco.draw(20, 60 + i*(ScreenHeight/4), 20)
    else: #se a zona de espera n tem blocos, criar 3 novos
        for i in range(3):
            bloco= Block(screen)
            list_of_blocos.append(bloco)

    #delay de selecionar os blocos
    if selectdelay > 0:
        selectdelay-=1
    
    if mouse_down: #se um botão do rato está a ser pressionado
        if eventbutton == 1 and selectdelay == 0: #se for o esquerdo
            selectdelay+=200
            mouse= mouse_pos() #posição do rato
            mouse_rect= pygame.Rect(mouse[0], mouse[1], 1, 1)
            for bloco in list_of_blocos: #testa para todos os blocos q podem ser selecionados
                if bloco.hitbox.colliderect(mouse_rect): #se o rato está a colidir com ele, e se sim
                    if holding_block: #Vê se já estava a segurar no bloco, e se sim
                        holding_block= False
                        index=10000
                        colocar_bloco= matriz.place_block(bloco.type, matriz.get_square(), bloco.color) #tenta colocar o bloco no sitio onde o rato está
                        #se não conseguir, o bloco deve voltar à sua posição original na "zona de espera"
                        if colocar_bloco: #conseguiu pôr o bloco
                            list_of_blocos.remove(bloco) #apaga o bloco colocado da lista de blocos na "zona de espera"
                    else: #começa a segurar no bloco
                        holding_block= True
                        index= list_of_blocos.index(bloco) #descobre o index do bloco selecionado na lista
                        #o bloco começa a seguir o rato até ser "largado" noutro sitio

    if game_lost:
        pygame.time.delay(6000)
        game_ended(str(matriz.points))
    
    pygame.display.update()
pygame.quit()