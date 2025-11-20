soma = 0
cont = 0

for i in range(6):
    num = int(input('Digite um número inteiro : '))
    if num % 2 == 0:
        soma += num
        cont += 1

print(f'Foram registrado {cont} números pares, e a soma entre eles é {soma}.')