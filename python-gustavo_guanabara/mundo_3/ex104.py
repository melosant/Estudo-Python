# Programa 104 : validação de inteiro
# Funções / Escopo de Variáveis (Aula 21)

def leiaint(quest):
    verif = False
    valor = 0
    while True:
        quest = input('Digite um número: ')
        if quest.isnumeric():
            valor = int(quest)
            verif = True
        else:
            print('ERRO! Digite um número inteiro válido.')
        if verif == True:
            break

    return valor

num = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {num}.')