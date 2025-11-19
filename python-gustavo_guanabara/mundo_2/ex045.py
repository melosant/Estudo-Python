import random
import time

dic = {1 : 'PEDRA', 2 : 'PAPEL', 3 : 'TESOURA'}

print('=-=-=-=-=-=-=-=-=-=-=-=')
print('PEDRA, PAPEL OU TESOURA')
print('=-=-=-=-=-=-=-=-=-=-=-=')
print('''\nSUAS OPÇÕES :
[1] PEDRA
[2] PAPEL
[3] TESOURA
      SELECIONE (1-3) : ''')

maquina = random.randint(1,3)
jogador = int(input())

time.sleep(.5)
print('=-=-=-=-=-=-=-=-=-=-=-=')
print('  COMPUTADOR JOGANDO')
print('=-=-=-=-=-=-=-=-=-=-=-=')
time.sleep(.5)

if jogador == 1:
    if maquina == 1:
        print(f'\n{dic[jogador]} x {dic[maquina]} = Empate!!')
    elif maquina == 2:
        print(f'\n{dic[jogador]} x {dic[maquina]} = Computador Venceu!!')
    elif maquina == 3:
        print(f'\n{dic[jogador]} x {dic[maquina]} = O Jogador Venceu!!')

elif jogador == 2:
    if maquina == 1:
        print(f'\n{dic[jogador]} x {dic[maquina]} = O Jogador Venceu!!')
    elif maquina == 2:
        print(f'\n{dic[jogador]} x {dic[maquina]} = Empate!!')
    elif maquina == 3:
        print(f'\n{dic[jogador]} x {dic[maquina]} = O Computador Venceu!!')

elif jogador == 3:
    if maquina == 1:
        print(f'\n{dic[jogador]} x {dic[maquina]} = O Computador Venceu!!')
    elif maquina == 2:
        print(f'\n{dic[jogador]} x {dic[maquina]} = O Jogador Venceu!!')
    elif maquina == 3:
        print(f'\n{dic[jogador]} x {dic[maquina]} = Empate!!')
else:
    print('\nJogada Inválida.')