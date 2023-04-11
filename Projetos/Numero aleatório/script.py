import random

print ('Olá! Por favor, escolha um numero entre 1 a 10')

number = int(random.randint(1, 10))


while number:
    escolha = int(input('Digite: '))
    if(escolha < 1 or escolha > 10):
        print('Por favor, apenas números entre 1 a 10')
        continue
    if escolha == number:
        print('Parabéns! Você acertou!')
        break
    else:
        print('Errado! Tente novamente')

    