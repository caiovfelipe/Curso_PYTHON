valorc = float(input('Qual é o valor da casa? R$ '))
sal = float(input('Qual é o salário? R$ '))
temp = float(input('Em quantos anos ele vai pagar? '))
prest = valorc / (temp * 12)
nvsal = sal * 30 / 100
if prest > nvsal:
    print('Desculpe, mas o valor da prestação mensal é maior do que você consegue pagar')
    print('Operação não permitida.')
else: 
    print('Parabéns, o espréstimo foi aprovado!')
    print('O valor mensal será de {:.2f} por {} anos'.format(prest, temp))