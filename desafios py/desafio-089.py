cont = 0
ficha = list()

while True:

    #Nome
    if cont == 0:
        nome = str(input('Digite o nome do aluno: '))
    else:
        nome = str(input('Digite o nome do outro aluno: '))

    #Nota
    nota1 = float(input('Nota: '))
    nota2 = float(input('Nota: '))
    media = (nota1+nota2)/2
    ficha.append([nome, [nota1, nota2], media])

    #Parar execução
    resp = str(input('Deseja continuar? [S/N]: '))
    if resp in 'Nn':
        break


    cont += 1

print('-=' *30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-' *26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    conts = str(input('Deseja saber a nota de algum aluno individualmente? [S/N] '))
    if conts not in 'NnSs':
        print('Valor inválido. Digite sua resposta novamente.')
    else:
        if conts in 'Nn':
            break
        else:
            escolha = str(input('De qual aluno? '))
            for pessoa, x, med in ficha:
                if escolha == pessoa:
                    print(f'A média da pessoa {pessoa}, suas notas são {x}  e sua média é igual há {med}.')
        
