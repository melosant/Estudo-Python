# Programa 24 - Ordem Descrescente usando Listas e BubbleSort

minha_lista = [10, 25, 14, 3, 8]

# -------------- BubbleSort

troca = True # variável de controle de trocas e repetição

while troca: # loop principal
    troca = False # atribuído False à variável para ao menos uma volta ser feita
    for i in range(len(minha_lista) - 1): # loop vai até o penúltimo elemento da lista (pois compara o atual elemento com o próximo)
        if minha_lista[i] < minha_lista[i + 1]: # se o elemento atual for menor que o próximo
            troca = True # atribuído True para o loop fazer mais uma volta
            minha_lista[i], minha_lista[i + 1] = minha_lista[i + 1], minha_lista[i] # troca de posição

# --------------- Forma Simplificada utilizando métodos de lista
# minha_lista.sort()
# minha_lista.reverse()

print(minha_lista)