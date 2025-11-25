lista = [[0,0,0], [0,0,0], [0,0,0]] # declara matriz

for l in range(3):
    for c in range(3):
        lista[l][c] = int(input(f'Digite o valor na posição [{l}][{c}] : ')) # preenche os valores

print('=-' * 20)

for l in range(3): # print da matriz
    print()
    for c in range(3):
        print(f'[ {lista[l][c]} ]', end='')