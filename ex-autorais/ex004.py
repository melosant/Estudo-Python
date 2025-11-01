# Programa 4 - Soma Acumulada de 5 Números

i = 1
soma = 0
while i < 6: # loop de 5 números
    num = int(input("Digite um número: "))
    i += 1
    soma += num

# impressão da soma dos 5 numeros
print(f"A soma dos 5 números é de {soma}")