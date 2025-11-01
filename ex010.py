# Programa 10 - Fatorial

num = int(input('Digite um número : '))
result = 1 # resultado começa em 1 pq é o multiplicador
i = 1

# estrutura condicional principal
# se for menor que 0 = fatorial não existe e fim do programa
# se não for fatorial de 0 = 1
# caso contrário segue a lógica da fatorial
if num < 0:
    print("Erro! Fatorial não existente.")
elif num == 0:
    print(f"{num}! = {result}")
else:
    for i in range(1, num + 1): # índice vai até o número escolhido + 1
        result *= i # resultado anterior multiplicado pelo proximo numero na sequencia
    
    # while i < num + 1:
    #     result *= i
    #     i += 1

    print(f"{num}! = {result}")