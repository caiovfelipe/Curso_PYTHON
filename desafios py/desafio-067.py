while True:
    n = int(input('Digite um número para saber sua tabuada: '))
    if n < 0:
        break
    for c in range(1, 11):
        n2 = n * c
        print(f'{n} x {c} = {n2}')
    
print('Fim')

        