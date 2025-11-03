# Programa 27 - Separação Par/Ímpar

# declaração de variáveis
lista_num = []
lista_par = []
lista_impar = []

print("=" * 20)
print("ÍMPAR OU PAR")
print("=" * 20)

for i in range(10): # loop de 10 voltas
    numero = int(input("Digite um número : ")) # entrada de dados
    lista_num.append(numero) # adição dos dados na lista geral
    if numero % 2 == 0: # se resto for 0
        lista_par.append(numero) # adiciona também na lista par
    else: # se não
        lista_impar.append(numero) # adiciona na lista ímpar

# impressão das listas finais
print(f"\nLISTA GERAL : {lista_num}")
print(f"\nLISTA PARES : {lista_par}")
print(f"\nLISTA ÍMPARES : {lista_impar}")