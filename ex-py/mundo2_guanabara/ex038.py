n1 = int(input('Digite um número : '))
n2 = int(input('Digite outro número : '))

if n1 > n2:
    print(f'O primeiro valor é maior do que o segundo.')
elif n2 > n1:
    print(f'O primeiro valor é menor do que o segundo.')
else:
    print(f'Ambos os valores são iguais.')