dictmp = dict()
lista = list()
mulheres = list()
quant = quantm = media = 0
while True:
    dictmp["Nome"] = str(input('Nome: '))
    dictmp["Idade"] = int(input('Idade: '))
    dictmp["Sexo"] = str(input('Sexo: '))
    lista.append(dictmp.copy())
    quant += 1
    resp = str(input('Deseja continuar? [S/N]: '))
    if resp in 'Nn':
        break

print('As pessoas registradas foram as seguintes: ')
for pplms in lista:
    print(f'{pplms["Nome"]} com {pplms["Idade"]} anos.')
#A) variavel quantidade no while ----

for ppl in lista:
    if ppl["Sexo"] in "Ff":
        mulheres.append(ppl.copy())



print('As mulheres registradas foram: ')
for pplm in mulheres:
    print(f'{pplm["Nome"]} com {pplm["Idade"]} anos.')
#B) for, que percorra a key "sexo" de todas as pessoas, e em caso afirmativo, add em outra lista
#C) um for inicial para descobrir a média, e dentro dele, percorrer todas as idades e mostrar as pessoas

for med in lista:
    media += med["Idade"]
    quantm += 1
media = media / quantm

print(f'Pessoas com mais da média de idade ({media}):')
for pplage in lista:
    if pplage["Idade"] > media:
        print(f'{pplage["Nome"]}: {pplage["Idade"]} anos.')
        
##Adicionar limite de casas decimais na hr de mostrar a média.
