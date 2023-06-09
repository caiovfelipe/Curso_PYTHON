from random import randint
n = randint(1,11)
u = int(input('Digite um número entre 1 a 10: '))
cont = 0
while u != n:
    print('Errado!')
    u = int(input('Digite outro número entre 1 a 10: '))
    cont += 1
print('Uau! Meus parabéns, você acertou! O número era {}.'.format(n))
print('Você acertou após {} tentativa(s)'.format(cont))