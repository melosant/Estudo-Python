pessoas = []
individual = []
maior = menor = 0

while True:
    individual.append(str(input('Nome : ').capitalize()))
    individual.append(float(input("Peso (em kg): ")))

    if len(pessoas) == 0:
        maior = menor = individual[1]
    else:
        if individual[1] > maior:
            maior = individual[1]
        if individual[1] < menor:
            menor = individual[1]

    pessoas.append(individual[:])

    individual.clear()

    opc = input('Deseja continuar ? [S/N] ').upper()
    if opc == 'N':
        break

print('=-' * 15)
print(f'Total de pessoas cadastradas : {len(pessoas)}')
print(f'O maior peso foi de {maior} de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')

print(f'\nO menor peso foi de {menor} de  ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')

print()
print('=-' * 15)