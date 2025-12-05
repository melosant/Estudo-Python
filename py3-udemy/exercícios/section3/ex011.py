# Palavra Secreta
# Aula 77-80
from os import system

secret = 'FLAMENGO'
tentativas = 0
acertos = ''

while True:
    letra_digitada = input('\nDigite uma letra : ').upper()
    tentativas += 1
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in secret:
        acertos += letra_digitada

    palavra_formada = ''
    for letra in secret:
        if letra in acertos:
            palavra_formada += letra
        else:
            palavra_formada += '*'

    print(palavra_formada)

    if palavra_formada == secret:
        system('cls')
        print('\nVOCÊ VENCEU. PARABÉNS!!')
        print('A palavra era',secret)
        print(f'Foram necessárias {tentativas} tentativas.')
        break