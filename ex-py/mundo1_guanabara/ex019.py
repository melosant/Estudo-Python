from random import choice

alunos = []
for i in range(4):
    a = input('Digite o nome do aluno : ')
    alunos.append(a)

print(f'O aluno escolhido foi {choice(alunos)}.')