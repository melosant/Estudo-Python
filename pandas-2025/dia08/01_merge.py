import pandas as pd

transacoes = pd.read_csv('pandas-2025/data/transacoes.csv', sep=';')
clientes = pd.read_csv('pandas-2025/data/clientes.csv', sep=';')

# da o merge com o df transacoes como base (esquerda) e com clientes (direita)
# how='left' -> mantém a dimensão o df base
# on=['IdCliente] -> usa o id do cliente como base para o merge
# suffixes=[''] -> define os sufixos de ambas os df's no merge
print(transacoes.merge(right=clientes,
                 how='left',
                 on=['IdCliente'],
                 suffixes=['Transacao', 'Cliente']))

df1 = pd.DataFrame({
    'transacao': [1,2,3,4,5],
    'idCliente': [1,2,3,2,2],
    'nome': ['t1', 't2', 't3', 't4', 't5'],
    'valor': [10, 45, 32, 17, 87]
})

df2 = pd.DataFrame({
    'id': [1,2,3,4],
    'nome': ['teo', 'nathã', 'mah', 'jose']
})

# caso as colunas usadas como base para o merge tenham nomes diferentes, usa left_on e right_on
print(df1.merge(right=df2, 
                left_on=['idCliente'], 
                right_on=['id'],
                how='left', 
                suffixes=['Transacao', 'Cliente']))

