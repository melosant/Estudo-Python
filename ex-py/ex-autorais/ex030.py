# Programa 30 - Remoção de duplicatas (Cisco)

lista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
lista_semduplicatas = []

for num in lista: # para cada número presente na lista
    if num not in lista_semduplicatas: # se número não está na lista final, é adicionado
        lista_semduplicatas.append(num)

print(lista_semduplicatas)