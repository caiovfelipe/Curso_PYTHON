matriz = list()
col1 = list()
col2 = list()
col3 = list()
for c in range(3):
    num1 = int(input(f'Digite o número para a coordenada (1, {c+1}): '))
    col1.append(num1)
matriz.append(col1[:])
for f in range(3):
    num2 = int(input(f'Digite o número para a coordenada (2, {f+1}): '))
    col2.append(num2)
matriz.append(col2[:])
for d in range(3):
    num3 = int(input(f'Digite o número para a coordenada (3, {d+1}): '))
    col3.append(num3)
matriz.append(col3[:])

for l in range(0,3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

