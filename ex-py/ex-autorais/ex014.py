# Programa 14 - Caixa Registradora

# declaração de variáveis
itens = 0
soma = 0
registro = 0

# loop infinito
while True:
    registro = float(input("Digite o valor do item ou digite 0 para encerrar : "))
    if registro == 0: # se digitar 0, quebra o loop
        break
    else: # digita o valor, adiciona 1 à variável itens e o valor na variável soma.
        itens += 1
        soma += registro

print()
# imprime total de compra e itens.
print(f"""\nTOTAL DA COMPRA : {soma}
TOTAL DE ITENS : {itens}""")