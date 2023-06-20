n = int(input('Digite um número para descobrir seu fatorial: '))
fat = 1
i = 2
while i <= n:
    fat *= i
    i += 1
print('O fatorial de {} é {}.'.format(n, fat))