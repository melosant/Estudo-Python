# Programa 114 : Refazendo ex104
# Tratamento de erros e exceções (aula 23)


def leiaint(msg):
    valor = 0
    while True:
        try:
            valor = int(input(msg))
            break
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar este número.')
            break
        except:
            print('ERRO! Digite um número inteiro válido.', end=' ')
    return valor

def leiareal(msg):
    valor = 0
    while True:
        try:
            valor = float(input(msg))
            break
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar este número.')
            break
        except:
            print('ERRO! Digite um número real válido.', end=' ')
    return valor

num = leiaint('Digite um número inteiro: ')
numreal = leiareal('Digite um número real: ')

print(f'\nVocê acabou de digitar o número inteiro {num}.') 
print(f'Você acabou de digitar o número real {numreal}.') 