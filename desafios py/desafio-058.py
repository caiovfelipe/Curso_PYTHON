from random import randint
n = randint(1,11)
u = int(input('Digite um número entre 1 a 10: '))
cont = 1
while u != n:
    
    cont += 1
    if u < n:
        u = int(input('Muuito baixo! Digite outro número: '))
    else:
        u = int(input('Alto demais! Digite outro número: '))
print('Uau! Meus parabéns, você acertou! O número era {}.'.format(n))
print('Você acertou após {} tentativa(s)'.format(cont))