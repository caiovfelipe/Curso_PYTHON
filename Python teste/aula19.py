estado = dict()
brasil = list()
while True:
    estado['uf'] = str(input('Digite o estado: '))
    estado['sigla'] = str(input('Digite a sigla desse estado: '))
    brasil.append(estado.copy())
    resp = str(input('Deseja continuar? [s/n] '))
    if resp in 'Nn':
        break
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem o valor {v}')


'''brasil = list()
estado1 = {'uf': 'São Paulo', 'sigla': 'SP'}
estado2 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])'''
