# Aula 162-163
# Aumento de 10% no preço de produtos
from copy import deepcopy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = deepcopy(produtos)
for dicts in novos_produtos:
    dicts['preco'] *= 1.10

print('Antes do aumento :\n')
for dicts in produtos:
    dicts['preco'] = round(dicts['preco'], 2)
    print(dicts)

print('\nDepois do aumento :\n')
for dicts in novos_produtos:
    dicts['preco'] = round(dicts['preco'], 2)
    print(dicts)