cont = soma = 0
n = int(input('Digite uma série de números: '))
print('Digite 999 quando desejar parar.')
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite mais números: '))
print('Você digitou {} números.'.format(cont))
print('A soma entre eles foi de {}.'.format(soma))
print('Operação finalizada.')