# Exibir índices de uma lista
# Aula 87

lista = ['Maria', 'Helena', 'Luiz']
lista.append('Nathã')

# i = 0
# for nome in lista:
#     # print(i)
#     # i += 1
#     print(lista.index(nome), nome, type(nome))

for i, nome in enumerate(lista):
    print(i, nome, type(nome))