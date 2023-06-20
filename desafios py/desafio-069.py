mulher20 = homens = mais18 = 0
while True:
    idade = int(input('Digite a idade da pessoa: '))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Qual é o sexo da pessoa [M/F]: ')).upper().split()[0]
    if sexo == 'M':
        homens += 1
    if idade >= 18:
        mais18 += 1
    if sexo in 'Ff' and idade <= 20:
        mulher20 += 1
    skip= ' '
    while skip not in 'SN':
        skip = str(input('Deseja continuar [S/N]? ')).upper().split()[0]
    if skip in 'Nn':
        break
print('Operação Finalizada.')
print(f'Foram contabilizadas {mais18} pessoa(s) com mais de 18 anos.')
print(f'Foram contabilizados {mulher20} mulher(es) com mais de 20 anos.')
print(f'Foram contabilizados {homens} homens.')