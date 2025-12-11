from itertools import zip_longest

estados = ['Salvador', 'Ubatuba', 'Belo Horizonte']
uf = ['BA', 'SP', 'MG', 'RJ']

def zipper(l1, l2):
    return [
        (l1[i], l2[i]) for i in range(3)
    ]

print(f'Usando função : {zipper(estados, uf)}')
print(f'\nUsando zip : {list(zip(estados, uf))}')
print(f'\nUsando ziplongest : {list(zip_longest(estados, uf))}')