# codigo do ex035

r1 = int(input('informe o valor da 1° reta : '))
r2 = int(input('informe o valor da 2° reta : '))
r3 = int(input('informe o valor da 3° reta : '))

if r1 + r2 < r3:
    print('NÃO PODE SER TRIÂNGULO!')
elif r2 + r3 < r1:
    print('NÃO PODE SER TRIÂNGULO!')
elif r1 + r3 < r2:
    print('NÃO PODE SER TRIÂNGULO!')
else:
    print('TRIÂNGULO FORMADO!')
    if r1 == r2 == r3:
        print('TRIÂNGULO EQUILÁTERO.')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('TRIÂNGULO ISÓSCELES.')
    else:
        print('TRIÂNGULO ESCALENO.')