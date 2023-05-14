preco_produto = int(input('Qual é o valor do produto? '))
print('''FORMAS DE PAGAMENTO:
[1] à vista no dinheiro/cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
formapg = int(input('Qual é a forma de pagamento? '))
if formapg == 1:
    descontpreco = (preco_produto / 10) * 9
    print('O preço do produto, com o desconto aplicado, fica {}.'.format(descontpreco))
elif formapg == 2:
    descontpreco = (preco_produto / 100) * 95
    print('O preço do produto, com o desconto aplicado, fica {}.'.format(descontpreco))
elif formapg == 3:
    dividido = preco_produto / 2
    print('De acordo com a forma de pagamento escolhida, o preço continuará o mesmo. Você pagará 2x de {}'.format(dividido))
elif formapg == 4:
    descontpreco = (preco_produto / 10) * 12
    totalparc = int(input('Quantas parcelas? '))
    parcela = descontpreco / totalparc
    print('De acordo com a forma de pagamenro escolhida, o preço ficará {}, sendo dividido em {}x de {}.'.format(descontpreco, totalparc, parcela))
else:
    total = 0
    print('Opção inválida. Tente novamente.')
print('SUa compra de R${:.2f} vai custar R${:.2f} no final'.format(preco_produto, descontpreco))