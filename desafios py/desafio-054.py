cont = 0
for c in range(7):
    ano = int(input('Qual é seu ano de nascimento? '))
    idade = 2023 - ano
    if idade > 18:
        cont += 1
print('Dessas sete pessoas, {} já atingiram a maioridade'.format(cont))