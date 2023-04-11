import math

print('Olá! Bem vindo a Calculator in a nutshell, a sua calculadora na linha de comando! Por favor, escolha qual conta deseja fazer:')
escolha = input('Digite mais, subtracao, divisao e multiplicacao: ')
adicao = 'mais'
tirar = 'subtracao'
dividir = 'divisao'
multiplicar = 'multiplicacao'

if escolha == adicao:
    print('Ok! digite os numeros as quais deseja obter a soma:')
    num1 = int(input('Digite o primeiro numero: '))
    num2 = int(input('Digite o segundo numero: '))
    soma = num1 + num2
    print('A noma entre {} e {} é igual a: {}' .format(num1, num2, soma))
    print('Muito obrigado por usar a minha calculadora <3')

elif escolha == tirar:
    print('Ok! Digite os numeros as quais deseja obter a subtração: ')
    sub1 = int(input('Digite o primeiro numero: '))
    sub2 = int(input('Digite o segundo numero: '))
    tira = sub1 - sub2
    print('A subtração entre {} e {} é {}' .format(sub1, sub2, tira))
    print('Muito obrigado por usar a minha calculadora <3')

elif escolha == dividir:
    print('Ok! Digite os números dos quais deseja obter a sua divisão: ')
    div1 = int(input('Digite o primeiro número: '))
    div2 = int(input('Digite o segundo número: '))
    dividido = div1 / div2
    print('A divisão entre {} e {} é igual a {}' .format(div1, div2, dividido))
    print('Muito obrigado por usar a minha calculadora <3')

elif escolha == multiplicar:
    print('Ok! Digite os númedos dos quais deseja obter sua multiplicação: ')
    mul1 = int(input('Digite o primeiro número: '))
    mul2 = int(input('Digite o segundo número: '))
    multiplicado = mul1 * mul2
    print('A multiplicação entre {} e {} é igual a {}'.format(mul1, mul2, multiplicado))
    print('Muito obrigado por usar a minha calculadora <3')

else:
    print('Ops! Você ditigou as instruções de forma errada. Por favor, certifique-se se escrever exatamente as palavras adicao e subtracao')


    