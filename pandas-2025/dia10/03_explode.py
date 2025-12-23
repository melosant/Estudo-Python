# case cartão crédito
# soma das parcelas baseadas nos meses

import pandas as pd

df = pd.read_csv('pandas-2025/dia10/dados_cartao.csv', sep=';')

# converte a data da transação para datetime
df['dtTransacao'] = pd.to_datetime(df['dtTransacao'])
# calc valor da parcela
df['vlParcela'] = df['vlVenda'] / df['qtParcelas']
# indica o número da parcela
df['ordemParcela'] = df.apply(lambda row: [i for i in range(row['qtParcelas'])], axis=1)
# faz o explode baseado na ordem da parcela, cada linha vai receber o valor da ordem
df_explode = df.explode('ordemParcela')

def calcParcela(row):
    '''
    Mostra o mês de pagamento da parcela.
    Soma um ao mês da transação, e após isso ao anterior baseado na ordem e à quantidade
    '''
    dt = row['dtTransacao'] + pd.DateOffset(months=row['ordemParcela'])
    dt = f'{dt.year}-{dt.month}'
    return dt

# aplica a ordem
df_explode['dtParcela'] = df_explode.apply(calcParcela, axis=1)
# faz um groupby do id e da data, somando todas as parcelas baseadas nas datas
df_explode = (df_explode.groupby(['idCliente', 'dtParcela'])
                        ['vlParcela'].sum()
                        .reset_index())
print(df_explode)