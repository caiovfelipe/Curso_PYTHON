pessoa = list()
pessoal = list()
totp = max = min = indc = 0
while True:
    pessoa.append(str(input('Digite o nome: ')))
    pessoa.append(float(input('Digite o peso: ')))

    if len(pessoal) == 0:
        max = min = pessoa[1]
    else:
        if pessoa[1] > max:
            max = pessoa[1]
        if pessoa[1] < min:
            min = pessoa[1]
    pessoal.append(pessoa[:])
    pessoa.clear()
    qp = str(input('Quer continuar? (S/N): '))
    totp += 1
    if qp in 'Nn':
        break
print(f'O maior peso registrado foi de {max}')
for p in pessoal:
    if p[1] == max:
        print(f'A(s) pessoa(s) com o maior peso foi(ram): {p[0]}')
print(f'O menor peso registrado foi de {min}')
for c in pessoal:
    if c[1] == min:
        print(f'A(s) pessoa(s) com o menor peso foi(ram): {c[0]}')
print(pessoal)
