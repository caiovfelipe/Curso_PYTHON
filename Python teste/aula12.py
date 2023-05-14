nome = str(input('Qual é seu nome? '))
if nome == 'Caio':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem comum.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Que nome normal.')

print('Tenha um bom dia, {}!'.format(nome))