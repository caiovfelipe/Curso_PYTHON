from random import randint

def sorteio(numeros):
    for c in range(5):
        numeros.append(randint(1, 100))
    print(f'Os números sorteados foram: {numeros}')

def somapar(numeros):
    soma = 0
    for valor in numeros:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma de todos os valores pares é igual a {soma}.')


numeros = list()
sorteio(numeros)
somapar(numeros)
