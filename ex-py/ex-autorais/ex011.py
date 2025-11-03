# Programa 11 - Sequência de Fibonacci

# declaração variáveis iniciais
a = 0
b = 1
cont = 0

term = int(input("Digite quantos termos da sequência quer ver : "))
if term <= 0: # se for menor ou igual a zero, não existe sequência
    print("Por favor, digite um valor positivo.")
else:
    # estrutura de loop while (enquanto)
    while cont < term:
        print(a, end =" ") # imprime número atual da sequência
        proximo = a + b # soma dos 2 anteriores
        # troca das variáveis
        a = b 
        b = proximo
        cont += 1