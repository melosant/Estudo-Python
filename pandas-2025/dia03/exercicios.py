import pandas as pd

# 03.01 - Quantas linhas há no arquivo clientes.csv ?
print('3.1: ')
clients = pd.read_csv('pandas-2025/data/clientes.csv', sep=';')
print('QTD LINHASxCOLUNAS : ', clients.shape)

# 03.02 - Quantas colunas do tipo int há no arquivo transacoes.csv ?
print('3.2: ')
transacoes = pd.read_csv('pandas-2025/data/transacoes.csv', sep=';')
print('QTD COLUNAS INT TRANSACOES: ', len(transacoes.select_dtypes(int).columns))

# 03.03 - Quantas colunas do tipo object há no arquivo produtos.csv ?
print('3.3: ')
products = pd.read_csv('pandas-2025/data/produtos.csv', sep=';')
print('QTD COLUNAS OBJECT PRODUTOS: ', len(products.select_dtypes(object).columns))

# 03.04 - Qual o id do cliente no índice 4 no arquivo clientes.csv ?
print('3.4: ')
print('ID CLIENTE INDICE 4: ', clients['idCliente'].iloc[4])

# 03.05 - Qual o saldo de pontos do cliente na 6a posição (sem ordenar) do arquivo clientes.csv ?
print('3.5: ')
print('SALDO DE PONTOS 6° INDICE: ', clients['qtdePontos'].iloc[6])