# Aula 162-163
# Ordene os produtos por preço crescente
from copy import deepcopy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

produtos_ordenados_por_preco = deepcopy(produtos)
produtos_ordenados_por_preco = sorted(produtos_ordenados_por_preco, key=lambda p: p['preco'])

for dicts in produtos_ordenados_por_preco:
    print(dicts)