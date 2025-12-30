import json

# pessoa = {
#     'nome': 'Nathã',
#     'sobrenome': 'Melo',
#     'enderecos': [
#         {'rua': 'R1', 'numero': 32},
#         {'rua': 'R2', 'numero': 55},
#     ],
#     'altura': 1.8,
#     'numeros_preferidos': (4, 7, 8, 11, 21),
#     'dev': True,
#     'nada': None
# }

# with open('aula191.json', 'w', encoding='UTF-8') as arquivo:
#     json.dump(pessoa, 
#               arquivo,
#               ensure_ascii=False,
#               indent=4)

with open('aula191.json', 'r', encoding='UTF-8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)