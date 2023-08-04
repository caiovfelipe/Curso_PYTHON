number1 = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')
number2 = ('Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
numbers = number1 + number2
while True:
    choice = int(input('Digite qual número deseja mostrar por extenso. [0 a 20] '))
    if 0 <= choice <= 20:
        print(numbers[choice])
        r = input(str('Deseja executar o programa novamente? [S/N] '))
        if r in 'Nn':
            break
    else:
        print('Número inválido. Tente novamente:')
