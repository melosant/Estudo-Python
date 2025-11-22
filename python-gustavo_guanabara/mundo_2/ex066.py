soma = qtd = 0

while True:
    n = int(input('Digite um número (999 para parar) : '))
    if n == 999:
        break
    else:
        soma += n
        qtd += 1

print(f'A soma dos {qtd} valores é {soma}')