from random import randint
cont = 0
while True:
    usern = int(input('Par ou ímpar [1 para ímpar, e 2 para par]: '))
    while usern not in (1, 2):
        print('Dados inválidos')
        usern = int(input('Par ou ímpar [1 para ímpar, e 2 para par]: '))
        
    compn = randint(1, 2)
    if usern == 1:
        if (usern + compn)%2 == 1:
            print('Parabénss, você venceu.')
            print('Continue jogando..')
            cont += 1
        else:
            break
    if usern == 2:
        if (usern + compn)%2 == 0:
            print('Parabénss, você venceu.')
            print('Continue jogando..')
            cont += 1
        else:
            break
    
print(f'Você perdeu com {cont} vítorias consecutivas.')
    