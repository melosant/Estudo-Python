# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy) e deepcopy (para vlaores mutáveis)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    'nome' : 'Nathã',
    'sobrenome' :'Melo',
    'pai' : 'Nilton',
    'mãe' : 'Adriana'
}

# print(len(pessoa))

# print(list(pessoa.keys()))
# for chave in pessoa:
#     print(chave)

# print(list(pessoa.values()))
# for valor in pessoa.values():
#     print(valor)

# print(list(pessoa.items()))
# for chave, valor in pessoa.items():
#     print(chave, ':', valor)

# pessoa.setdefault('idade', 18)
# print(pessoa['idade'])

# import copy
# d1 = {
#     'c1' : 1,
#     'c2' : 2,
#     'c3' : [1, 2, 3],
# }
# d2 = d1.copy()
# d3 = copy.deepcopy(d1)
# d2['c3'][1] = 777
# d3['c3'][1] = 999
# print(d1)
# print(d2)
# print(d3)

# print(pessoa.get('nome'))
# print(pessoa.get('idade'))
# print(pessoa.get('idade', 'Não Existe'))

# nomepai = pessoa.pop('pai')
# print(nomepai)
# print(pessoa)

# ultimachave = pessoa.popitem()
# print(ultimachave)
# print(pessoa)

# pessoa.update({
#     'nome' : 'Débora',
#     'idade' : 27
# })
# tupla = (('nome', 'Débora'), ('idade', 27))
# pessoa.update(tupla)
# lista = [['nome', 'Débora'], ['idade', 27]]
# pessoa.update(lista)
# pessoa.update(nome='Débora', idade=27)
# print(pessoa)