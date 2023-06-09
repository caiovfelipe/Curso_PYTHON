ti = int(input('Digite o termo inicial da progreção aritmédica: '))
r = int(input('Digite a razão da PA: '))
contm = 10
cont = 1
total = 0
mr = 10
while mr != 0:
    total += mr
    while cont <= total:
        print('{} => '.format(ti), end='')
        ti += r
        cont += 1
    print('Fim')
    mr = int(input('Quantos termos você quer mostrar a mais? '))
print('PA terminada com {} termos contabilizados.'.format(cont))