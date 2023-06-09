sex = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()[0]
while sex not in 'MmFf':
    print('Dados inválidos. Digite Novamente.')
    sex = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()[0]
print('Dados registrados.')