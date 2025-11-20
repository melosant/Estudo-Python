soma = 0
qtd = 0
n = 0 

while n != 999:
    n = int(input('Digite um número (999 para parar): '))
    if n != 999:
        soma += n
        qtd += 1

print(f'Foram digitados {qtd} numeros e a soma entre eles é {soma}.')