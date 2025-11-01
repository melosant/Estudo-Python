# Programa 13 - Número Primo

num = int(input("Digite um número : "))
cont = 2 # começa em 2 por conta que qualquer número divido por 1 da ele mesmo
confirm = False # começa como número não-primo sempre

# zero ou negativos não são primos
if num <= 1:
    print("Não é primo!")
elif num == 2: # 2 é primo
    print("É primo!")
else:
    while cont < num: # 2 até um número antes do escolhido
        if num % cont == 0: # se for divisível por algum número nesse período, para o loop e tem a confirmação de que é um não-primo
            confirm = False
            break
        else: # se não for divisível, muda a variável confirm para True, concluindo que é um número primo.
            confirm = True
            break
    # Estrutura condicional para impressão do número primo ou não-primo.
    if confirm == True:
        print(f"{num} é um número primo!")
    else:
        print(f"{num} não é um número primo!")