import random as rd
lista = list()

quant = int(input('Quantas jogadas deseja fazer?: '))
for p in range(quant):
    for c in range(quant):
        lista.append(rd.randint(0, 60))
print(lista)
