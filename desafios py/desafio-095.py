lista = list()

dicionario = dict()

quant_jogadores = int(input('Quantos jogadores serão contabilizados?: '))

for z in range(quant_jogadores):
    dicionario["Nome"] = str(input(f'Nome do jogador {z+1}: '))
    listajogos = list()
    quant_jogos = int(input('Quantos jogos foram jogados?: '))
    for c in range(quant_jogos):
        golsc = int(input(f'Número de gols no jogo {c+1}: '))
        listajogos.append({f'Jogo': c+1, 'Gols': golsc})
    lista.append({'Jogador': dicionario.copy(), 'Jogos': listajogos})
    

for jogadorc in lista:
    nome = jogadorc['Jogador']["Nome"]
    print(f'Dados do jogador {nome}')
    for jogoc in jogadorc['Jogos']:
        num_jogo = jogoc['Jogo']
        num_gols = jogoc['Gols']
        print(f'No jogo {num_jogo}, a quantidade de gols foi: {num_gols}')