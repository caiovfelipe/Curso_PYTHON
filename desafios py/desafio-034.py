salario = float(input('Qual é o seu salário: R$'))
if salario >= 1250.00:
    porcent = salario * 0.10
    final = salario + porcent
    print('Seu salário ficará: R${}'.format(final))
else:
    porcent = salario * 0.15  # calcula 15% do salário
    final = salario + porcent
    print('Seu salário será de: R${:.2f}'.format(final))
