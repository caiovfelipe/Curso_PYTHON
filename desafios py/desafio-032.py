from datetime import date
ano = int(input('Digite um ano para verificar se ele é bisexto: '))
if ano == 0:
    ano = date.today().year
if ano%4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print('O ano de {} é bisexto!'.format(ano))
else:
    print('Desculpe, o ano de {} não é um ano bisexto'.format(ano))