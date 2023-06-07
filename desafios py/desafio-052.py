n = int(input('Digite um número para verificar se ele é primo: '))
cont = 0
for v in range(1, n+1):
    if n%v == 0:
        cont+=1
if cont == 2:
    print('O número {} é dividido {} vezes.'.formart(n,cont))
    print('Por isso ele É primo')
else:
    print('O número {} é dividido {} vezes.'.format(n, cont))
    print('Por isso ele NÃO é primo')
