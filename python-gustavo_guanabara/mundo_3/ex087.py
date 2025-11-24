lista = [[0,0,0], [0,0,0], [0,0,0]] # declara matriz
somapares = somaterceira = maiorvalor = 0

for l in range(3):
    for c in range(3):
        lista[l][c] = int(input(f'Digite o valor na posição [{l}][{c}] : ')) # preenche os valores
        if lista[l][c] % 2 == 0: 
            somapares += lista[l][c] # soma dos pares

        if c == 2:
            somaterceira += lista[l][c] # soma da terceira coluna

print('=-' * 20)

for l in range(3): # print da matriz
    print()
    for c in range(3):
        print(f'[ {lista[l][c]} ]', end='')

print()

for c in range(3): # maior valor da segunda linha
    if c == 0:
        maiorvalor = lista[1][c]
    elif lista[1][c] > maiorvalor:
        maiorvalor = lista[1][c]
        
print()
print('=-' * 20)
print(f'\nA soma dos valores pares é {somapares}')
print(f'A soma dos valores da terceira coluna é {somaterceira}')
print(f'O maior valor da segunda linha é : {maiorvalor}\n')