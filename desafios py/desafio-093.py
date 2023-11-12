
lista = list()
dic = dict()
quantg = 0


#Pegar o nome
nome = str(input('Nome do jogador: '))
#Quantas partidas
quantp = int(input('Número de partidas: '))
#Fazer um for para cada partida
for c in range(quantp):
    golsc = int(input(f'Número de gols no jogo {c+1}: '))
#Guardar em uma lista para cada partida (copy)
    lista.append({f'Jogo': c+1, 'Gols': golsc})
#Contagem de gols no for
    quantg += golsc
#No fim da execução, guardar o a quantidade de gols do dict
for jogo in lista:
    print(f'No jogo {jogo["Jogo"]}, a quantidade de gols foi: {jogo["Gols"]}')
print(f'A quantidade total de gols foi: {quantg}')
#Guardar nos dicionários

#Mostragem