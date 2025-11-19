maior = 0
menor = 0

for i in range(3):
    n = int(input('informe um número : '))
    if n > maior:
        maior = n
    else:
        menor = n

print(f'O MAIOR NÚMERO DIGITADO FOI {maior}')
print(f'O MENOR NÚMERO DIGITADO FOI {menor}')