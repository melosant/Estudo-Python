import pandas as pd

df = pd.read_csv('pandas-2025/data/transacoes.csv', sep=';')
print(df.columns)
print()

# ao renomear, ele retorna um novo dataframe
df = df.rename(columns={'QtdePontos':'QtPontos', 
                        'DescSistemaOrigem':'SistemaOrigem'})

print(df.columns)

# se utilizar inplace=True, altera o próprio dataframe
df.rename(columns={'DtCriacao':'DataCriacao'}, inplace=True)
print(df.columns)

# para acessar mais de uma coluna é necessário passar uma lista das colunas, assim retornando um dataframe (independente da quantidade de elementos na lista)
print(df[['IdCliente', 'QtPontos']])
print(df[['IdCliente', 'QtPontos']].head())

# reordenar colunas
print(df[['IdCliente', 'IdTransacao', 'QtPontos']].head())

# ordenando em ordem alfabética as colunas
colunas = list(df.columns)
colunas.sort()
df = df[colunas]
print(df)