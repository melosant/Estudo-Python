numeros = [[], []]

for c in range(7):
    n = int(input(f'Digite o {c+1}° número: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)

numeros[0].sort()
numeros[1].sort()
print('=-' * 15)
print(f'Números Pares : {numeros[0]}')
print(f'Números Ímpares : {numeros[1]}')