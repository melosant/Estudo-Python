soma = 0
qtd = 0

for i in range(1,501, 2):
    # if i & 2 != 0:  # outra forma de conferir os ímpares
    if i % 3 == 0:
        soma += i
        qtd += 1

print(f'Foram solicitados {qtd} números e a soma entre eles é : {soma}')