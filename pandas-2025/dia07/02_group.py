import pandas as pd

transacoes = pd.read_csv('pandas-2025/data/transacoes.csv', sep=';')

# df agrupa as informações por IdCliente
print(transacoes.groupby(by=['IdCliente']).count())
# series retorna quantidade de transações por IdCliente
# [[]] = df / [] = series
# as_index = False cria indexs e Id vira coluna, True utiliza o IdCLiente como index
print(transacoes.groupby(by=['IdCliente'], as_index=False)[['IdTransacao']].count())

# qtde_transacoes, total de pontos e media de pontos por transacao
# metodo agg : passa o nome das colunas e os métodos que serão aplicados
summary = transacoes.groupby(by=['IdCliente'], as_index=False).agg({
                    'IdTransacao': ['count'],
                    'QtdePontos': ['sum', 'mean']})

# cria um multi index
print(summary)
# pra acessar um multi index
print(summary[('QtdePontos', 'mean')])

# para definir o nome das colunas e acabar com o multi index
summary.columns = ['IdCliente', 'QtdeTransacao', 'TotalPontos', 'AvgPontos']
print(summary)