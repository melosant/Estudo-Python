import pandas as pd

df = pd.read_csv('pandas-2025/data/transacao_produto.csv', sep=';')

# somente os id produto 5 ou 11
filtro = (df['IdProduto'] == '5') | (df['IdProduto'] == '11')
print(df)

filtro = df['IdProduto'].isin(['5','11'])
print(df[filtro])

df_clientes = pd.read_csv('pandas-2025/data/clientes.csv', sep=';')

# clientes com pontos que não estão zerados
filtro = df_clientes['qtdePontos'] != 0
print(df_clientes[filtro])

# tudo oq nao for em branco
filtro = df_clientes['DtCriacao'].notna()
print(df_clientes[filtro])

# somente espaços em branco
filtro = df_clientes['DtCriacao'].isna()
print(df_clientes[filtro])