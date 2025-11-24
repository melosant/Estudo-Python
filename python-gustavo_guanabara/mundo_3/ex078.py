valores = []

for i in range(5):
    v = int(input(f'Digite o valor para posição {i} : '))
    valores.append(v)


print('=-' * 20)
print(f'Você digitou os valores {valores}')
print(f'O maior valor foi {max(valores)} nas posições ', end='')
for c in range(len(valores)):
    if valores[c] == max(valores):
        print(c, end=' ')

print(f'\nO menor valor foi {min(valores)} nas posições ', end='')

for c in range(len(valores)):
    if valores[c] == min(valores):
        print(c, end=' ')