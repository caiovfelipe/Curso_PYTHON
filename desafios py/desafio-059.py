n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opcao = 0
while opcao != 5:
    print('''
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA
    ''')
    opcao = int(input('Sua opção: '))

    if opcao == 1:
        ns = n1 + n2
        print('A soma é {}.'.format(ns))
    if opcao == 2:
        nm = n1 * n2
        print('A multiplicação dos números é {}.'.format(nm))
    if opcao == 3:
        if n1 > n2:
            print('O número {} é maior do que o número {}.'.format(n1, n2))
        elif n1 == n2:
            print('Os dois números são iguais.')
        else:
            print('O número {} é maior do que o número {}.'.format(n2, n1))
    if opcao == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
print('A execução do programa foi abortada.')
print('Obrigado por usar nosso programa!.')