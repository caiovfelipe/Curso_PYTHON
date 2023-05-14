peso = float(input('Qual é seu peso?'))
altura = float(input('Qual é sua altura?'))
imc = peso / (altura**2)
print('Seu imc é {}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade mórbida')