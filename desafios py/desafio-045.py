import random as rm
print('Olá, bem vindo ao jogo Jokenpô!')
print('---' * 25)
itens = ('Pedra', 'Papel', 'Tesoura')
print('Aperte 0 para escolher tesoura, 1 para escolher pedra, e 2 para escolher papel.')
user = int(input('Escolha: '))
computer = rm.randint(0, 2)
print('Jogador jogou {} e o Computador jogou {}'.format(itens[computer], itens[user]))
#User wins
if user == 0 and computer == 2 or user == 1 and computer == 0 or user == 2 and computer == 1:
    print('Parabéns! Você venceu o jogo!')
#Tie
elif user == computer:
    print('Vocês empataram. Jogue novamente!.')
#Computer wins
else:
    print('Infelizmente, o computador venceu. Joge novamente!')

