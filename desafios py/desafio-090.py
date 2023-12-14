aluno = dict()
aluno['Nome'] = str(input('Digite o nome do aluno: '))
aluno['Média'] = float(input(f'Digite a média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'
print(f'O aluno {aluno["Nome"]} obteve uma média igual há {aluno["Média"]}, e portanto, está {aluno["Situação"]}')
                    