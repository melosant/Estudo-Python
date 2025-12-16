import pandas as pd

df = pd.read_csv('pandas-2025/data/transacoes.csv', sep=';')
print(df.columns)

# o filtro retorna uma serie de booleanos
filtro = (df['QtdePontos'] >= 500) & (df['QtdePontos'] <= 1000)

# passa uma serie com o mesmo numero de linhas, compara com o df e caso seja True: exibe.
print(df[filtro])

# valores 100 ou 2000
filtro = (df['QtdePontos'] == 100) | (df['QtdePontos'] == 2000)
print(df[filtro])

# valores entre 0 e 50 ou da twitch
filtro = (df['QtdePontos'] > 0) & (df['QtdePontos'] <= 50) | (df['DescSistemaOrigem'] == 'twitch')
print(df[filtro])