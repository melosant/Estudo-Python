# Programa 7 - Média das Notas

# -------------------------- SEM USAR LOOP ---------------------------------

# nome = input("Digite o nome do aluno : ")
# n1 = float(input(f"Digite a primeira nota do aluno {nome} : "))
# n2 = float(input(f"Digite a segunda do aluno {nome} : "))
# n3 = float(input(f"Digite a terceira nota do aluno {nome} : "))

# media = (n1 + n2 + n3) / 3
# print(f'\nMÈDIA DO ALUNO : {media:.2f}\n')

# if media >= 7.0:
#     print(f'O aluno {nome} está APROVADO!')
# elif media >= 5.0 and media < 7.0:
#     print(f'O aluno {nome} está em RECUPERAÇÃO!')
# else:
#     print(f"O aluno {nome} está REPROVADO!")

# --------------------------- USANDO LOOP --------------------------------

nome = input("Digite o nome do aluno : ")
i = 1
soma = 0

# loop para registro de notas e as adiciona na variável soma
for i in range(1, 4):
    nota = float(input((f"Digite a {i}° nota : ")))
    soma += nota

# cálculo da média mais a impressão formatada
media = soma / 3
print(f"A média do aluno {nome} foi : {media:.2f}")

# estrutura condicional para verificação de situação
if media >= 7.0:
    print(f"O aluno {nome} foi APROVADO!")
elif media >= 5.0 and media < 7.0:
    print(f"O aluno {nome} está de RECUPERAÇÂO!")
else:
    print(f"O aluno {nome} está REPROVADO!")