salario = float(input('Qual o valor de seu salario? R$'))
#Regra de 3/x
salario_aumento = salario + (salario * 15 / 100)
#calcula os 15% do salario e adiciona ao salario normal
print('O seu salario, com um aumento de 15%, é {}.'.format(salario_aumento))