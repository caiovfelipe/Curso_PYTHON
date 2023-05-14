reais = float(input('Qual o valor em reais que você quer transferir para dolar? R$'))
dolar = reais / 5.12
print('O valor de \033[0;32m{}\033[m reais pode valer \033[0;31m{:.2f}\033[m dolares'.format(reais, dolar))