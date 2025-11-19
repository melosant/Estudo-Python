from random import randint

numero_secreto = randint(0, 5)

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print(' Vou pensar em um número entre 0 e 5')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

chute = int(input('\nEm que número pensei ? '))
print('PROCESSANDO...')
if chute == numero_secreto:
    print(f'\nAff. Você ganhou, o número era {numero_secreto}.')
else:
    print(f'Eu ganhei!!! O número que pensei foi {numero_secreto} e não {chute}.')