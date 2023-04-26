from random import randint
n = (randint(0, 5))
ns = int(input('Escolha um número entre 1 e 5: '))
if ns == n:
    print('Parabéns! Você ganhou!')
else:
    print('Errou! Jogue novamente.')