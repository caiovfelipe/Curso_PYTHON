num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

maior = menor = num1 # set the initial values of maior and menor to num1

#maior
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

#menor
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

print('O maior número é {} e o menor é {}'.format(maior, menor))

'''num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
if num1 >= num2 or num1 >= num3:
    maior = num1
elif num1 <= num2 or num1 <=num3:
    menor = num1
if num2 >= num1 or num2 >= num3:
    maior = num2
elif num2 <= num1 or num2 <= num3:
    menor = num2
if num3 >= num1 or num3 >= num2:
    maior = num3
elif num3 <= num2 or num3 <= num2:
    menor = num3
print('O maior número é {} e o menor é o {}'.format(maior, menor))'''
