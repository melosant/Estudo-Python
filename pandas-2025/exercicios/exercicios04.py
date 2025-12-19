import pandas as pd

# 04.01 - Quantos clientes tem vínculo com a Twitch?
print('\n4.1:')
clients = pd.read_csv('pandas-2025/data/clientes.csv', sep=';')
filtro = clients['flTwitch'] == 1
print('QTD CLIENTES VINCULADOS À TWITCH : ', len(clients[filtro]))

# 04.02 - Quantos clientes tem um saldo de pontos maior que 1000?
print('\n4.2:')
filtro = clients['qtdePontos'] > 1000
print('QTD CLIENTES COM MAIS DE 1000 PONTOS : ', len(clients[filtro]))

# 04.03 - Quantas transações ocorreram no dia 2025-02-05?
print('\n4.3:')
filtro = pd.to_datetime(clients['DtCriacao']).dt.date.astype(str) == '2025-02-05'
print('QTD DE TRANSAÇÕES NO DIA 2025-02-05: ', len(clients[filtro]))