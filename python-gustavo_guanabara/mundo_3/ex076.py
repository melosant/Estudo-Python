listagem = ('Lápis', 1.75, 
            'Borracha', 2.00, 
            'Caderno', 15.90, 
            'Estojo', 25.00, 
            'Transferidor', 4.20, 
            'Compasso', 9.99, 
            'Mochila', 120.32, 
            'Canetas', 22.30, 
            'Livro', 34.90)

# print(f'''
# -----------------------------------------------------
#                 LISTAGEM DE PREÇOS
# -----------------------------------------------------
# {listagem[0]}.................................R${listagem[1]}
# {listagem[2]}..............................R${listagem[3]}
# {listagem[4]}...............................R${listagem[5]}
# {listagem[6]}................................R${listagem[7]}
# {listagem[8]}..........................R${listagem[9]}
# {listagem[10]}..............................R${listagem[11]}
# {listagem[12]}...............................R${listagem[13]}
# {listagem[14]}...............................R${listagem[15]}
# {listagem[16]}.................................R${listagem[17]}''')


print('-' * 30)
print('      LISTAGEM DE PREÇOS')
print('-' * 30)
for c in range(0, (len(listagem))):
    if c % 2 == 0:
        print(f'{listagem[c]:.<30}' ,end='')
    else:
        print(f'R$ {listagem[c]}')