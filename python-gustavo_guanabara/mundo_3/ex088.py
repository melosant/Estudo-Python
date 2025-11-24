from random import randint
from time import sleep

jogos = []
temp = []
qtd = 0

print('-=' * 10)
print('     MEGA-SENA')
print('-=' * 10)

qtd = int(input('Quantos jogos deseja que eu sorteie? '))

print('-=' * 20)
for i in range(qtd):
    for j in range(6):
        temp.append(randint(1,60))
    jogos.append(temp[:])
    temp.clear()
    sleep(.5)
    print(f'Jogo {i+1}: {jogos[i]}')

print('-=' * 20)
print('\nBoa Sorte!')