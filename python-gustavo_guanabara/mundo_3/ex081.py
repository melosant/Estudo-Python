lista = []
cont = 0

while True:
    num = int(input('Digite um valor : '))
    lista.append(num)
    cont += 1

    opc = input('Deseja continuar ? [S/N] ').upper()
    if opc == 'N':
        break

lista.sort(reverse=True)

print(f'''
Você digitou {cont} elementos.
Os valores em ordem decrescente {lista}''')
if 5 in lista:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não está na lista.')