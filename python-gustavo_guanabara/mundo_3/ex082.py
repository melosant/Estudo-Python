lista = []
listapar = []
listaimpar = []

while True:
    num = int(input('Digite um número : '))
    lista.append(num)
    if num % 2 == 0:
        listapar.append(num)
    else:
        listaimpar.append(num)

    opc = input('Deseja continuar ? [S/N] ').upper()
    if opc == 'N':
        break

print(f'''
LISTA : {lista}
PARES : {listapar}
impares : {listaimpar}''')