tupla = (int(input('Digite um número : ')),
      int(input('Digite um número : ')),
      int(input('Digite um número : ')),
      int(input('Digite um número : ')))

print(f'Valores Registrados : {tupla}')
print(f'O valor 9 aparece {tupla.count(9)} vezes')

if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3) + 1}° posição')
else:
    print(f'O valor 3 não apareceu nenhuma vez')

print(f'Os valores pares digitados foram ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end= ' ')
