soma = 0
vzs = 0
for n in range(3, 496, 6):
        if n%3 == 0:
            vzs += 1
            soma += n
print('A soma dos {} valores contabilizados é {}'.format(vzs, soma))
            