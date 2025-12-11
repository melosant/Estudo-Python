# Aula 162-163
# Ordene os produtos por nome decrescente
from copy import deepcopy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

produtos_ordenados_por_nome = deepcopy(produtos)
produtos_ordenados_por_nome = sorted(produtos_ordenados_por_nome, key=lambda p: p['nome'], reverse=True)

for dicts in produtos_ordenados_por_nome:
    print(dicts)