import random as rd








nomes = list()
dados = dict()
cont = 0
for i in range(0, 4):
    nome = str(input(f'Digite o nome do jogador {i+1}: '))
    nomes.append({'Nome': nome, 'Dado': 0})
z = 0
for jogador in nomes:
    print(f'Hora do(a) {jogador["Nome"]} jogar!')
    input('Dê enter para jogar o dado... ')
    cont+=1
    jogador['Dado'] = rd.randint(1, 6)

nomes.sort(key=lambda jogador: jogador['Dado'], reverse=True)

empates = [jogador for jogador in nomes if jogador['Dado'] == nomes[0]['Dado']]

if len(empates) == 1:
    print(f'O(A) jogador(a) com a maior pontuação foi {nomes[0]["Nome"]}, com {nomes[0]["Dado"]} pontos.')
else:
    print('Temos um empate! Os jogadores empatados são:')
    for empate in empates:
        print(f'O(A) jogador(a) {empate["Nome"]} com {empate["Dado"]} pontos.')

print('A tabela completa é: ')
for jogador in nomes:
    print(f'O(A) jogador(a) {jogador["Nome"]} obteve pontuação {jogador["Dado"]}.')

'''
temp = dict()
lista = list()
#Pegar o nome de cada 

for c in range(0, 3):
    temp['Nome'] = str(input(f'Digite o nome do jogador {c}'))
    lista.append(temp.copy())


#Jogar o dado
for i in lista:
    print(f'Hora do jogador {lista[i].value()} jogar o dado!')
    input('Dê enter para jogar o dado... ')
    temp['Dado'] = rd(0, 6)'''


#Colocar o dicionário em ordem