from random import randint as rd
a = ()
for c in range(5):
    a += (rd(1, 100), )
print(f'Os números sorteados foram: {a}')
x = sorted(a, reverse=True)
print(x)
print('O maior número foi: {}'.format(x[0]))
print('O menor número foi: {}'.format(x[-1]))