import copy
#este modulo serve para ao fazer a copia da lista de listas (sopa), o python criar mesmo um objeto diferente, ou seja, copiá-lo e pô-lo noutro espaço da memória

def getsopa():
    nrcol=int(input("Quantas colunas são?  "))
    nrfil=int(input("Quantas filas são?  "))
    sopa=[]
    print("Escreva as filas sem espaços entre as letras")
    for i in range (nrfil):#pede as filas quantas vezes quantas forem as filas dadas
        c=True
        while c:
            print("Fila nr "+str(i+1))
            filas=list(input()) #pede a fila sem espaços e coloca a na forma de lista logo
            if len(filas)==nrcol:#verifica q o nr de letras dado é mesmo o nr de colunas
                sopa.append(filas)
                c=False
    print(sopa)
    return sopa


def direcao(sopa,coordfila,coordcol,tam,xd,yd):
    tentativa="" 
    #é a palavra q vai ser "feita" a partir das coords da primeira letra (coordfila,coordcol) e seguindo na direção definida pelos xd e yd
    
    for i in range (tam):
        try:
            tentativa+=sopa[coordfila+(i*xd)][coordcol+(i*yd)]
#            print(coordfila+(i*xd),coordcol+(i*yd))
            #juntar as letras na variavel tentativa por ordem, começando na letra q foi encontrada no inicio
            #xd e yd são as variáveis q indicam a direção em q se está a procurar o resto da palavra
        except IndexError:
           # print("index error",coordfila+(i*xd),coordfila+(i*xd))
            return "F" #foi para fora da "sopa"
    return tentativa

def encontroupalavra(sopa,coordfila,coordcol,tam,palavra):
    if direcao(sopa,coordfila,coordcol,tam,0,-1)==palavra: #procurar para cima da letra encontrada
        return "cima"
    elif direcao(sopa,coordfila,coordcol,tam,1,-1)==palavra: #procurar para cima e a direita da letra encontrada
        return "diagcimadir"
    elif direcao(sopa,coordfila,coordcol,tam,1,0)==palavra: #procurar para a direita da letra encontrada
        return "direita"
    elif direcao(sopa,coordfila,coordcol,tam,1,1)==palavra: #procurar para baixo e direita da letra encontrada
        return "diagbaixdir"
    elif direcao(sopa,coordfila,coordcol,tam,0,1)==palavra: #procurar para baixo da letra encontrada
        return "baixo"
    elif direcao(sopa,coordfila,coordcol,tam,-1,1)==palavra: #procurar para baixo e a esquerda da letra encontrada
        return "diagbaixesq"
    elif direcao(sopa,coordfila,coordcol,tam,-1,0)==palavra: #procurar para a esquerda da letra encontrada
        return "esquerda"
    elif direcao(sopa,coordfila,coordcol,tam,-1,-1)==palavra: #procurar para cima e a esquerda da letra encontrada
        return "diagcimaesq"
    else: #não encontrou
        return "F"
    

def procurapalavra(palavra,sopa):
    tam=len(palavra) #tamanho da palavra
    letra=palavra[0] #1º letra
    nrcol=len(sopa[0]) #nr de colunas
    nrfil=len(sopa) #nr de filas
    for x in range (nrfil):#este ciclo vai percorrer cada uma das filas
        fila=sopa[x]
        for y in range (nrcol):#este ciclo vai percorrer cada uma das letras na fila
            if fila[y]==letra:
                #se a letra em q vamos na fila for = à 1º letra, tenta ver em todas as direções se está a palavra
                tentativa=encontroupalavra(sopa,x,y,tam,palavra)
                if tentativa !='F': #se tiver encoontrado faz return da direção em q esta (definida por "tentativa"), as coords da 1º letra, e o tamanho da palavra
                    return [tentativa,x,y,tam]
                #se não encontrou recomeça o ciclo e continua a procurar
                
    #se percorrer todas as letras de todas as filas e n encontrou nada, a palavra n está na sopa de letras
    return [] 


def mostrarpalavranasopa(procurar,sopa):
    sopatemp=list(sopa)
    tentativa=procurar[0]
    x=procurar[1]
    y=procurar[2]
    tam=procurar[3]
   # print("x="+str(x))
  #  print("y="+str(y))
    #define em q direção é q está a palavra, atribuindo valores ao xd e yd
    if tentativa=="cima":
        xd=0
        yd=-1
    elif tentativa=="diagcimadir":
        xd=1
        yd=-1
    elif tentativa=="direita":
        xd=1
        yd=0
    elif tentativa=="diagbaixdir":
        xd=1
        yd=1
    elif tentativa=="baixo":
        xd=0
        yd=1
    elif tentativa=="diagbaixesq":
        xd=-1
        yd=1
    elif tentativa=="esquerda":
        xd=-1
        yd=0
    elif tentativa=="diagcimaesq":
        xd=-1
        yd=-1
    for escr in range (tam):#coloca as letras da palavra encontrada em maiusculas, para serem fáceis de identificar
        sopatemp[x+escr*xd][y+escr*yd]=sopatemp[x+escr*xd][y+escr*yd].upper()
    return sopatemp #faz return da sopa de letras com as letras em maiusculas da palavra


def printlist(sopa): #faz print de todas as filas da sopa, por ordem
    for filas in range (len(sopa)):
        palavra=""
        fila=sopa[filas]
        for escrever in range (len(fila)):
            palavra+=fila[escrever]+" "
        print(palavra)


def variaspalavras(sopadev): #ciclo para procurar mais q uma palavra na mesma sopa de letras
    c=True #ciclo
    print("Não preencha o 'Palavra procurada' para terminar")
    mostrasopa=[]
    while c:
        palavra=input("Palavra procurada ")
        if palavra != "":
            procurar=procurapalavra(palavra,sopadev)
            if len(procurar)>0:#se houver return da lista com valores de ter encontrado alguma coisa
                #altera a sopa para mostrar as letras da palavra em maiusculas
                mostrasopa=mostrarpalavranasopa(procurar,copy.deepcopy(sopadev))
                #faz print da sopa
                printlist(mostrasopa)
                
            else:#se n tiver encontradom nada
                print("Não encontrada")
            #coloca a sopa de novo com tudo em minusculas
            mostrasopa=sopadev
        else:#quando a palavra procurada="", o ciclo acaba
            c=False
#pag 83     
sopa=[['o', 'l', 'e', 'b', 'a', 'c', 's', 'e', 'd', 'a', 'd', 'i', 'c', 'o', 'm'], ['m', 'a', 'u', 's', 'o', 'l', 'e', 'u', 'i', 'e', 'd', 'o', 'p', 'i', 'd'], ['a', 't', 'o', 'a', 'o', 'p', 'a', 'r', 'a', 'b', 'c', 'r', 's', 'e', 'l'], ['i', 's', 's', 'a', 'a', 'r', 'a', 'b', 'e', 'a', 'e', 'i', 'p', 'c', 'l'], ['s', 'i', 'a', 'g', 'p', 't', 'r', 's', 'r', 't', 'o', 'e', 'e', 'i', 'a'], ['r', 't', 'a', 'o', 's', 'o', 't', 'a', 's', 'e', 'n', 't', 'l', 'c', 'm'], ['o', 'i', 'r', 'e', 'l', 'i', 'c', 'd', 'h', 'd', 'v', 'o', 'e', 'e', 'p'], ['x', 'l', 'c', 'h', 'a', 'u', 'a', 'o', 'e', 'c', 'c', 'r', 'n', 'r', 'e'], ['i', 'e', 'a', 'r', 'r', 'o', 'ç', 'r', 'p', 'a', 'i', 'b', 'e', 'o', 'i'], ['m', 'l', 'i', 'a', 'r', 'a', 'p', 'o', 'l', 'a', 'g', 'h', 'u', 'n', 'r'], ['u', 'o', 't', 'r', 'e', 'b', 'o', 'l', 'h', 'a', 'r', 'm', 'c', 'e', 'o']]
variaspalavras(sopa)
