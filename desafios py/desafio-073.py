tabela = ('Botafogo', 'Palmeiras', 'Grêmio', 'Flamengo', 'Atlético-MG', 'Fluminense', 'São Paulo', 'Internacional', 'Bragantino', 'Fortaleza', 'Athletico-PR', 'Cruzeiro', 'Santos', 'Bahia', 'Corinthians', 'Cuiabá', 'Goiás', 'América-MG', 'Vasco da Gama', 'Coritiba') #Até 24/06/2023
print(f'Os primeiros cinco colocados são os times: {tabela[:6]}')
print(f'Os ultimos 4 colocados são os times: {tabela[-4:]}')
print('A lista, se fosse organizada em ordem alfabética, seria: {}'.format(sorted(tabela)))
print('O time Santos está na posição {}'.format(tabela.index('Santos')))