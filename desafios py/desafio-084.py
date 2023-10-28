# Inicialize listas vazias para armazenar nomes e pesos
nomes = []
pesos = []

# Solicite ao usuário que insira os dados das pessoas
while True:
    nome = input("Digite o nome da pessoa (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    peso = float(input("Digite o peso da pessoa: "))
    
    nomes.append(nome)
    pesos.append(peso)

# Verifique quantas pessoas foram cadastradas
total_pessoas = len(nomes)

# Verifique o peso máximo e mínimo
peso_maximo = max(pesos)
peso_minimo = min(pesos)

# Encontre as pessoas com peso máximo e mínimo
pessoas_peso_maximo = [nomes[i] for i, peso in enumerate(pesos) if peso == peso_maximo]
pessoas_peso_minimo = [nomes[i] for i, peso in enumerate(pesos) if peso == peso_minimo]

# Mostre os resultados
print(f"Total de pessoas cadastradas: {total_pessoas}")
print(f"Pessoas mais pesadas ({peso_maximo} kg): {', '.join(pessoas_peso_maximo)}")
print(f"Pessoas mais leves ({peso_minimo} kg): {', '.join(pessoas_peso_minimo)}")


'''
pessoa = list()
pessoas = list()
menor = list()
maior = list()
magro = gordo = 0
quant=0
quant = int(input('Quantas pessoas deseja adicionar?'))
for c in range(quant):
    pessoa.append(str(input('Nome: ')))
    pessoa.append(int(input('Peso: ')))
    pessoas.append(pessoa[:])
    pessoa.clear()
pessoas.sort()
maior.append(pessoas[0][0])
for p in pessoas:
    for f in p:
        if pessoas[0][1] == pessoas[p][f]:
            maior.append(pessoas[f][0])

print(maior)






#Output
print(f'Foram cadastradas {quant} pessoas.')
print(f'')'''
