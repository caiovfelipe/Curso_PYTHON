#from random import sample
from secrets import choice

nome1 = str(input('Nome do(a) primeiro(a) aluno(a): '))
nome2 = str(input('Nome do(a) segundo(a) aluno(a): '))
nome3 = str(input('Nome do(a) terceiro(a) aluno(a): '))
nome4 = str(input('Nome do(a) quarto(a) aluno(a): '))

'''nome1 = 'Caio'
nome2 = 'Renan'
nome3 = 'Sara'
nome4 = 'Vinicios'''
#nome = sample([nome1, nome2, nome3, nome4], k=1) #Usar choice também é uma opção

nome = choice([nome1, nome2, nome3, nome4])
print('O aluno escolhido foi {}.' .format(nome))