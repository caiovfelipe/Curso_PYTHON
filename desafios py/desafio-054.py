from datetime import date
cont = 0
contm = 0
for c in range(7):
    ano = int(input('Qual é seu ano de nascimento? '))
    idade = date.today().year - ano
    if idade > 21:
        cont += 1
    else:
        contm += 1
print('Dessas sete pessoas, {} já atingiram a maioridade'.format(cont))
print('E também temos {} pessoa(s) que são menores de idade.'.format(contm))