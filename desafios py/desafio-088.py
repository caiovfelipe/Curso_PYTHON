import random as rd
lista = list()
cont=0
temp = list()
quant = int(input('Quantas jogadas deseja fazer?: '))
for p in range(quant):
    for c in range(6):
        temp.append((rd.randint(0, 60)))
    lista.append(temp[:])
    temp.clear()
for i, l in enumerate(lista):
    print(f'Jogo {i+1}: {l}')