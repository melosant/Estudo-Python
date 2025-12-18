import pandas as pd

# 05.01 - Crie uma coluna nova “twitch_points” que e resultado da multiplicação do saldo de pontos e a marcação da twitch
print('5.1:')
clients = pd.read_csv('pandas-2025/data/clientes.csv', sep=';')
clients['twitch_points'] = clients['flTwitch'] * clients['qtdePontos']
print(clients)

# 05.02 - Aplique o log na coluna de saldo de pontos, criando uma coluna nova
print('\n5.2:')
import numpy as np
clients0 = pd.read_csv('pandas-2025/data/clientes.csv', sep=';')
clients0['SaldoPontos'] = np.log(clients0['qtdePontos'] + 1)
print(clients0)

# 05.03 - Crie uma coluna que sinalize se a pessoa tem vínculo com alguma (qualquer uma) plataforma de rede social.
print('\n5.3:')
clients2 = pd.read_csv('pandas-2025/data/clientes.csv', sep=';')
clients2['RedeSocial'] = clients2['flEmail'] + clients2['flTwitch'] + clients2['flYouTube'] + clients2['flBlueSky'] + clients2['flInstagram']
print(clients2)

# 05.04 - Qual é o id de cliente que tem maior saldo de pontos? E o menor?
print('\n5.4:')
clients3 = pd.read_csv('pandas-2025/data/clientes.csv', sep=';')
clients3 = clients3.sort_values('qtdePontos', ascending=False)
print('ID MAIOR: ', clients3['idCliente'].head(1))
clients3 = clients3.sort_values('qtdePontos', ascending=True).head(1)
print('ID MENOR: ', clients3['idCliente'].head(1))

# 05.05 - Selecione a primeira transação diária de cada cliente
print('\n5.5:')
transacoes5 = pd.read_csv('pandas-2025/data/transacoes.csv', sep=';')
'''
1 - ordena pela data de criação da transação
2 - cria uma coluna só com a data formata
3 - remove as duplicatas com base no IdCliente e na data mantendo somente a primeira transação
'''
transacoes5 = transacoes5.sort_values('DtCriacao')
transacoes5['data'] = pd.to_datetime(transacoes5['DtCriacao']).dt.date
print(transacoes5.drop_duplicates(keep='first', subset=['IdCliente', 'data']))