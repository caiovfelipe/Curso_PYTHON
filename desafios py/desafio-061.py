ti = int(input('Digite o termo inicial da progressão aritmédica: '))
r = int(input('Digite a razão: '))
cont = 1
while cont <= 10:
    print('{} => '.format(ti), end='')
    ti += r
    cont += 1
print('Fim')
