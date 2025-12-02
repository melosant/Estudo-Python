# Iteração de strings usando while
# Aula 65

nome = input('Digite seu nome : ')
i = 0

while i < len(nome):
    print(f'*{nome[i]}',end='')
    i += 1