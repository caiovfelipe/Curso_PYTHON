n = int(input('QUantos termos da sequencia de fibonacci você deseja obter? '))
t1, t2 = 0, 1
print('{} => {} '.format(t1, t2), end=' ')
t3 = t1 + t2
print('=> {} '.format(t3), end='')
cont = 3
while cont <= n-1:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print('=> {} '.format(t3), end='')
    cont = cont + 1
print('=> Fim')