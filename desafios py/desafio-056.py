idades = 0
velho = 0
mulheres = 0
contmulheres = 0
for c in range(1, 5):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(c))).strip()
    idade = int(input('Digite a idade da {}ª pessoa: '.format(c)))
    sexo = str(input('Digite o sexo da {}ª pessoa (M para sexo masculino e F para sexo feminino): '.format(c))).strip()

    idades += idade

    if sexo in 'Mm' and idade > velho:
        velho += idade
        homemmv = nome

    if sexo in 'Ff' and idade < 20:
        contmulheres += 1

print('A média de idade do grupo é: {}'.format(idades/c))
print('O nome do homem mais velho é {}'.format(homemmv))
print('Existem {} mulher(es) com menor de 20 anos.'.format(contmulheres))