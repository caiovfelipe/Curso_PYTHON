lista = list()
listajogos = list()
dicionario = dict()

quant_jogadores = int(input('Quantos jogadores serão contabilizados?: '))

for z in range(quant_jogadores):
    dicionario["Nome"] = str(input(f'Nome do jogador {z+1}: '))
    quant_jogos = int(input('Quantos jogos foram jogados?: '))
    for c in range(quant_jogos):
        golsc = int(input(f'Número de gols no jogo {c+1}: '))
        listajogos.append({f'Jogo': c+1, 'Gols': golsc})
    lista.append({'Jogador': dicionario, 'Jogos': listajogos})

for jogador in lista:
    nome = jogador['Jogador']["Nome"]
    print(f'Dados do jogador {nome}')
    for jogo in jogador['Jogos']:
        num_jogo = jogo['Jogo']
        num_gols = jogo['Gols']
        print(f'No jogo {num_jogo}, a quantidade de gols foi: {num_gols}')

#Nota
'''
o seguinte aconteceu:
preciso resolver a questao do output

preciso desenhar numa folha uma representação da estrutura de listas e dicionarios

depois, fazer um for para o output
    
o output q tá ai n funciona meu amigo
é isso'''