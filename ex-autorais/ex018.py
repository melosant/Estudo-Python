# Programa 18 - Soma dos Ímpares
soma = 0

# entrada dos valores no intervalo
a = int(input("Digite o primeiro valor do intervalo : "))
b = int(input("Digite o segundo valor do intervalo : "))

# loop para passagem de cada número no intervalo
for i in range(a, b + 1):
    if i % 2 != 0: # se for ímpar, adiciona à variável soma
        soma += i

# imprime resultado final
print(f"A soma dos valores ímpares entre {a} e {b} é : {soma}")