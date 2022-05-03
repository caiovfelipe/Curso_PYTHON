preço = float(input('Qual é o valor do produto? R$:'))
#regra de 3/x
preço_desconto = preço - (preço * 5 / 100)
preço_desconto_2 = preço_desconto - (preço_desconto * 5 / 100)
#preço - 5% e depois um desconto de 5% no ja descontado
print('O novo valor com o desconto de 5% é {}, e com 5% de desconto do novo valor, irá ficar {}'.format(preço_desconto, preço_desconto_2))