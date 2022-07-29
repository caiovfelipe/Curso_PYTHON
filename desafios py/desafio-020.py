from random import shuffle

g1 = str(input('Nome do(a) líder do grupo 1: '))
g2 = str(input('Nome do(a) líder do grupo 2: '))
g3 = str(input('Nome do(a) líder do grupo 3: '))
g4 = str(input('Nome do(a) líder do gurpo 4: '))
lista_grupos = [g1, g2, g3, g4]
shuffle(lista_grupos)
print('A lista da apresentação dos grupos será esta: {}' .format(lista_grupos))