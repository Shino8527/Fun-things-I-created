import math

def mmc(nr1, nr2): #minimo múltiplo comum
    if nr1 > nr2:
        limite= nr1
    else:
        limite= nr2

    for valor in range(limite+1): #verificar se de todos os nrs até ao maior, algum é divisor dos nr1 e nr2 ao mesmo tempo
        if nr1 % valor == 0 and nr2 % valor == 0:
            return valor
    #se percorrer todos os nrs e nenhum for divisor de ambos, n têm um multiplo comum
    return None

def mdc(nr1, nr2): #máximo divisor comum
    x1= nr1
    x2= nr2
    while x1 != x2:
        if x1> x2:
            x1-= x2
        else:
            x2-= x1
    return x1

def maior_e_menor_nr_in_lista(lista):
    maxi= 0
    min= 0
    for item in range(len(lista)):
        if lista[item] >= maxi:
            maxi= lista[item]
        elif lista[item] >= min:
            min= lista[item]

    return maxi, min

def e_primo(nr): #verifica se um nr é primo
  for idx in range(2, nr-1):
    if nr % idx == 0:
      return False
  return True

def decompor(nr): #decompor um nr em fatores primos (fatorização)
  fatores=[]
  for divisor in range(2, nr-1):
    ciclo=True
    if nr==1:
      break
    while ciclo:
      if nr/divisor==round(nr/divisor) and e_primo(divisor):
        nr/=divisor
        fatores.append(divisor)
      else:
        break
  return fatores

def verif_nr(valor): #verifica se o valor dado é um nr
  try:
    obj=eval(valor)
  except:
    return False
  return True
  
def verif_int(valor): #verifica se o valor dado é um inteiro
  try:
    obj=int(valor)
  except:
    return False
  return True

def raizquadrada(nr):
   return math.sqrt(nr)

def raiz(nr, indice): #raiz dum nr de indice "indice"
   return nr**(1/indice)

def fatorial(nr):
   return math.factorial(nr)

def dias_no_mes(nr_do_mes, ano):
   dicionario={1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
   if (ano%4 == 0 or ano%400 == 0) and nr_do_mes == 2:
      nrdias= 29
   else:
      nrdias= dicionario[nr_do_mes]
   return nrdias

def soma_de_nrs(lista): #faz a soma de todos os nrs numa lista e devolve esse valor
   sum= 0 #somatório de todos os nrs na lista
   tam= len(lista)
   for item in range(tam):
      sum+= lista[item]

   return sum

def multiplicacao_de_nrs(lista): #faz o produto de todos os nrs numa lista e devolve esse valor
   product= 0 #produto de todos os nrs na lista
   tam= len(lista)
   for item in range(tam):
      product*= lista[item]

   return product

def media_lista(lista): #faz a média de todos os elementos pertencentes a uma lista
   nr_itens_apagados= 0
   tam= len(lista)
   for item in range(tam):
      item-= nr_itens_apagados
      if not verif_nr(lista[item]): #se um item na lista n for um nr, é apagado da lista
         lista.pop(item)
         nr_itens_apagados+=1

   tam-= nr_itens_apagados #novo tamanho da lista
   sum= soma_de_nrs(lista)
   
   #return da média
   return sum/ tam

def get_angle_with_points(coord1, coord2):
   x1, y1 = coord1
   x2, y2 = coord2

   declive= (y2 - y1)/ (x2 - x1)
   angle= math.atan(declive)

   return angle

def teorema_pitagoras(cateto1, cateto2, hipotenusa):
   if cateto1 == 0:
      cateto1= (hipotenusa**2 - cateto2**2)**(1/2)
      return cateto1
   elif cateto2 == 0:
      cateto2= (hipotenusa**2 - cateto1**2)**(1/2)
      return cateto2
   elif hipotenusa == 0:
      hipotenusa= (cateto1**2 + cateto2**2)**(1/2)
      return hipotenusa
   
def formula_quadratica(a, b, c): #resolver uma equação de 2º grau
   x1= (-b + math.sqrt(b**2 - 4*a*c))/2*a
   x2= (-b - math.sqrt(b**2 - 4*a*c))/2*a
   return x1, x2

def distance_between_points(p1, p2):
   x1, y1=p1[0], p1[1]
   x2, y2=p2[0], p2[1]
   distance= math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
   return distance