aluno = {}

aluno['Nome'] = str(input('Nome do aluno : '))
aluno['Média'] = float(input(f'Média do aluno {aluno['Nome']} : '))
if aluno['Média'] >= 7.0:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'

for k,v in aluno.items():
    print(f'{k} é igual a {v}.')