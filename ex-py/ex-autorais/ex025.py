# Programa 25 - Ordenação Alfabética de Listas
# BubbleSort também funciona com strings, relação de maior e menor pela ordem alfabética.

# --------------- BubbleSort
lista_nomes = ["Carlos", "Ana", "Zacarias", "Daniel", "Fábio"]
troca = True

while troca:
    troca = False
    for i in range(len(lista_nomes) - 1):
        if lista_nomes[i] > lista_nomes[i + 1]:
            troca = True
            lista_nomes[i], lista_nomes[i + 1] = lista_nomes[i + 1], lista_nomes[i]

# -------------- Método de Lista
# lista_nomes.sort()

print(lista_nomes)