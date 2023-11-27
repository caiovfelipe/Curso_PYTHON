from datetime import *

#Pedir o as informações iniciais
dicionario = dict()


dicionario["Nome"] = str(input('Nome: '))
anonascd = int(input('Ano de nascimento: '))
ano_atual = datetime.now().year
idade = ano_atual - anonascd
dicionario["Idade"] = idade
dicionario["ctps"] = int(input('Valor da CTPS (0 para não possui): '))

if dicionario['ctps'] != 0:
    dicionario["Anocontr"] = int(input('Ano de contratação: '))
    dicionario["Salario"] = int(input('Salário: R$'))

print(dicionario)
print(f'Nome: {dicionario["Nome"]}')
print(f'Idade: {dicionario["Idade"]}')
print(f'Ano de nascimento: {anonascd}')
print(f'Ctps: {dicionario["ctps"]}')

if dicionario["ctps"] != 0:
    print(f'Ano de contratação: {dicionario["Anocontr"]}')
    print(f'Salário: {dicionario["Salario"]}')
    print(f'Irá se aposentar com {((dicionario["Anocontr"] - anonascd)+35)} anos.')



#Guardar a idade. Usar uma biblioteca com o ano de guardar já com a idade atual
#Pedir o valor da ctps, e depois vir um if para calcular o ano de contratação e salário
#Salário
#Pedir ano de contratação
#Calcular com quantos anos vai ser a aposentadoria
#ano de contratação menos ano de nascimento, e somar com 35


#OBS. 35 ANOS DE CONTRIBUIÇÃO