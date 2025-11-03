# Programa 26 - Soma de elementos 

# Declaração de Variáveis
total = 0 # variável da soma total
lista_num = [] # lista vazia

print("=" * 20)
print("DIGITE 5 NÚMEROS")
print("=" * 20)


for i in range(5): # loop para entrada de dados
    numero = int(input("Digite um número1: ")) # entrada de dados
    lista_num.append(numero) # adiciona o número digitado à lista 
    total += lista_num[i] # soma o número digitado à variável total

# impressão da lista e da soma
print("\n", lista_num)
print(f"\nA soma dos valores da lista é {total}.")
