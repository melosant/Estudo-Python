# Programa 33 - Número Primo com funções (Reutilização Programa 13)

def confere_primo(numero):
    confirm = False # começa assumindo que é um número não-primo

    cont = 2 # começa em 2 por conta que qualquer número divido por 1 da ele mesmo
    if numero <= 1:
        print("Não é primo!")
    elif numero == 2: # 2 é primo
        print("É primo!")
    else:
        while cont < numero: # 2 até um número antes do escolhido
            if numero % cont == 0: # se for divisível por algum número nesse período, para o loop e tem a confirmação de que é um não-primo
                confirm = False
                break
            else: # se não for divisível, muda a variável confirm para True, concluindo que é um número primo.
                confirm = True
                break
        # Estrutura condicional para impressão do número primo ou não-primo.
        if confirm == True:
            return "PRIMO"
        else:
            return "NÃO-PRIMO"

while True:
    num = int(input("Digite um número (0 para quebrar o loop ) : "))
    if num == 0:
        break
    else:
        resultado = print(f"{num} é um número {confere_primo(num)}")

print("Programa Finalizado!")