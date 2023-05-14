from secrets import choice
nome1 = str(input('Nome do(a) primeiro(a) aluno(a): '))
nome2 = str(input('Nome do(a) segundo(a) aluno(a): '))
nome3 = str(input('Nome do(a) terceiro(a) aluno(a): '))
nome4 = str(input('Nome do(a) quarto(a) aluno(a): '))
nome = choice([nome1, nome2, nome3, nome4])
print('O aluno escolhido foi \033[0;32m{}\033[m.' .format(nome))