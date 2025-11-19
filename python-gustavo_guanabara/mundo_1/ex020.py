import random

alunos = []
for i in range(4):
    a = input('Digite o nome do aluno : ')
    alunos.append(a)
    
random.shuffle(alunos) # embaralha randomicamente
print(f'Ordem da Lista : {alunos}.')