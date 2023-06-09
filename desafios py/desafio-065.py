resp = 'S'
cont = soma = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um valor: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
print('A média de todos os {} valores digitados é {}.'.format(cont, (soma/cont)))
print('O maior número digitado foi {} e o menor foi {}.'.format(maior, menor))
print('Operação finalizada.')