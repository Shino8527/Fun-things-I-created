def sort_by_size(lista, reverseTrue): #ordenar a lista pelo tamanho de cada elemento
    lista.sort(reverse= reverseTrue, key=len)
    return lista

def simple_sort(lista, reverseTrue): #ordenar a lista por ordem do alfabeto ou de nrs
    lista.sort(reverse= reverseTrue)
    return lista

def straight_list(lista): 
    #transforma uma lista de listas em apenas uma lista com todos os elementos por ordem
    newlist= []
    for minilist in range(len(lista)):
        for item in range(len(lista[minilist])):
            newlist.append(lista[minilist][item])

    return newlist

def transform_list_into_matrix(lista, size_of_side): #ATENÇÃO!!! O len(lista) tem de ser divisivel pelo size_of_side
    #transforma uma lista de itens numa matriz com o tamanho dado como argumento
    newBigList= []
    newSmallList= []
    for item in range(len(lista)+1): #vai passar por todos os itens da lista dada
        try:
            if len(newSmallList) == size_of_side: #quando a lista pequena tiver o tamanho q tem de ter
                #é adicionada à lista grande
                newBigList.append(newSmallList)
                #e volta a ser apagada para continuar
                newSmallList= []
                newSmallList.append(lista[item])
            else: # se não adiciona o item à lista pequena
                newSmallList.append(lista[item])
        except IndexError:
            pass
    return newBigList

def remove_item(lista, item_to_remove): #remove um item da lista
    popped_items= 0
    for item in range (len(lista)):
        item-= popped_items #impede q ocorra o IndexError
        if lista[item] == item_to_remove:
            lista.pop(item)
            popped_items+= 1

    return lista

def replace_item(lista, item_to_replace, what_to_replace_with): #substitui um item numa lista por outro, ambos são argumentos
    for item in range (len(lista)):
        if lista[item]== item_to_replace:
            lista[item]= what_to_replace_with

    return lista

def count_item(lista, item): #conta quantas vezes é q um item aparece numa lista
    return lista.count(item)