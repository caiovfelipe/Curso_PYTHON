soma = 0
cont = 0
for q in range(1, 7):
    num = int(input('Escolha o {} número:'.format(q)))
    if num%2 == 0:
        soma+=num
        cont+=1
print('A contagem do(s) {} número(s) par(es) é {}'.format(cont, soma))