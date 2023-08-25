count = 0
a = ()
for c in range(4):
    if count == 0 :
        b = int(input('Digite um valor: '))
    else:
        b = int(input('Digite outro valor: '))
    count+=1
    a += (b, )
print(f'Os números digitados foram os números {a}')
print('O número 9 apareceu {} vez(es)'.format(a.count(9)))
if a.count(3) == 0:
    print('O número 3 não apreceu em nenhum momento.')
else:
    print('O número três apareceu primeiro na {} posição.'.format(a.index(3)+1))
print('Os valores pares digitados foram ',end='')
for np in a:
    if np % 2 == 0:
        print(np, end='')
