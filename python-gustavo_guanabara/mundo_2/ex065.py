media = 0
qtd = 0
resp = ''

num = int(input('Informe um número inteiro :'))
qtd += 1
media += num
maior = num
menor = num

while resp != 'N':
    resp = input('Deseja continuar a digitar valores [S/N] : ').upper()
    
    if resp != 'N':
        num = int(input('Informe um número inteiro :'))
        qtd += 1
        media += num
        
        if num > maior:
            maior = num
        if num < menor:
            menor = num


print(f'''
-=-=-=-=-=-=-=-
MÉDIA : {media / qtd:.2f}
MAIOR : {maior}
MENOR : {menor}''')