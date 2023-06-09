c = 1
par = impar = 0
while c < 10:
    c = int(input('Digite um valor: '))
    if c != 0:
        if c % 2 == 0:
            par +=1
        else:
            impar +=1
print('Acabou')
print('Você digitou {}`números pares e {} números ímpares.'.format(par, impar))