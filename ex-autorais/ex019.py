# Programa 19 - Calculadora Simples
repetição = "" # variável para controle do loop

while True: # loop infinito
    # variáveis de entrada do número
    num1 = float(input("Digite o primeiro número : "))
    num2 = float(input("Digite o segundo número : "))

    print("-" * 30)
    print("\n Selecione a Operação :\n")
    print("-" * 30)
    print("""
    1 - SOMA
    2 - SUBTRAÇÃO
    3 - DIVISÃO
    4 - MULTIPLICAÇÃO
    0 - CANCELAR""")
    # variável para escolha de operação
    ope = input("\nQual a opção [0-4] : ")

    # condicional : cálculo realizado mediante a operação escolhida
    if ope == "1":
        print(f"{num1} + {num2} = ", num1 + num2)
    elif ope == "2":
        print(f"{num1} - {num2} = ", num1 - num2)
    elif ope == "3":
        print(f"{num1} / {num2} = ", num1 / num2)
    elif ope == "4":
        print(f"{num1} x {num2} = ", num1 * num2)
    else:
        break # caso de resposta "0" = fim do loop

    # controle do loop : se a resposta for "N" = fim do loop.
    repetição = input("\nDeseja fazer outra operação (S/N) ? ")
    if repetição.upper() == "N":
        break    

print("\nFim do programa!")