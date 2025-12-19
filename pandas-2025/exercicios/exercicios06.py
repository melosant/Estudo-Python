import pandas as pd

# 06.01 - Qual a quantidade média de redes sociais dos usuários? E a Variância? E o máximo?
clientes = pd.read_csv('pandas-2025/data/clientes.csv', sep=';')
redes_sociais = ['flEmail', 'flTwitch','flYouTube','flBlueSky','flInstagram']
qtd = clientes[redes_sociais].sum()
print(f'QTD MÉDIA DE REDES SOCIAIS POR CLIENTES : {qtd.sum() / len(clientes):.2f}')
print('VARIÂNCIA: ', clientes[redes_sociais].var())
print('MÁXIMO: ', clientes[redes_sociais].max())

# 06.02 - Quais são os usuários que mais fizeram transações? Considere os 10 primeiros.
transacoes = pd.read_csv('pandas-2025/data/transacoes.csv', sep=';')
id_mais_transacoes = transacoes.groupby(by='IdCliente', as_index=False).agg({'IdTransacao': ['count']})
id_mais_transacoes.columns = ['IdCliente', 'QtdeTransacoes']
print('\n', id_mais_transacoes.sort_values(by='QtdeTransacoes', ascending=False).head(10))

# 06.03 - Qual usuário teve maior quantidade de pontos debitados?

total = clientes.merge(transacoes, on=['IdCliente'], how='left', suffixes=['Clientes', 'Transacoes'])[['IdCliente', 'QtdePontos']]
total = total.groupby(by='IdCliente', as_index=False).head(5)
total.columns = ['IdCliente', 'PontosDebitados']
print('\nID COM MAIS PONTOS DEBITADOS: ', total.sort_values(by='PontosDebitados', ascending=False).head(1))

# 06.04 - Quem teve mais transações de Streak?
# transacoes4 = pd.read_csv('pandas-2025/data/transacoes.csv', sep=';')
# transacao_produto = pd.read_csv('pandas-2025/data/transacao_produto.csv', sep=';')
# produtos = pd.read_csv('pandas-2025/data/produtos.csv', sep=';')

# # cliente_transacao_produto = transacoes4.merge(transacao_produto, 
# #                                               on=['IdTransacao'], 
# #                                               how='left')[['IdTransacao', 'IdCliente', 'IdProduto']]

# # df_full = cliente_transacao_produto.merge(
# #                             right=produtos,
# #                             on=['IdProduto'],
# #                             how='left')

# # df_full = df_full[df_full['descProduto'] == 'Presença Streak']
# # (df_full.groupby(by=['IdCliente'])['IdTransacao']
# #         .count()
# #         .sort_values(ascending=False)
# #         .head(1))

# produtos = produtos[produtos['DescNomeProduto']=='Presença Streak']

# id_mais_streak = (transacoes4.merge(right=transacao_produto, on=['IdTransacao'], how='left')
#                              .merge(right=produtos, on=['IdProduto'], how='inner')
#                              .groupby(by='IdCliente')['IdTransacao']
#                              .count()
#                              .sort_values(ascending=False)
#                              .head(1))  

# 06.05 - Qual a média de transações / dia?

transacoes['DtCriacao'] = pd.to_datetime(transacoes['DtCriacao']).dt.date
transacoes = transacoes.groupby(by='DtCriacao', as_index=False).count()[['DtCriacao', 'IdTransacao']]
media = (transacoes['IdTransacao'].sum() / len(transacoes['DtCriacao']))
print(f'MÉDIA DE TRANSAÇÕES POR DIA : {media:.2f}')