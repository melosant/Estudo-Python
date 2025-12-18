import pandas as pd

clientes = pd.read_csv('pandas-2025/data/clientes.csv', sep=';')

# caso existam NaN's, dropna vai eliminar todas as linhas que tem NaN
print('DROPNA\n')

clientes = clientes.dropna()
print(clientes)

# esse é o default, qualquer Na irá dropar a linha
clientes.dropna(how='any')
# a linha inteira tem que ser Na para poder dropar
clientes.dropna(how='all')

df = pd.DataFrame({
    'nome': ['Téo', None, 'Nah', 'Marcio'],
    'idade': [None, None, 43, 52],
    'salario':[3453, 4324, None, 5423]
})


print('\nDROPNA PARAMETROS\n')
# dropa Na do dataframe com base na coluna idade.
print(df.dropna(subset=['idade']))
# dropa se tiver ao menos um Na na idade ou no salario
print(df.dropna(how='any' ,subset=['idade', 'salario']))
# dropa se tiver Na tanto em idade quanto em nome

# preenche onde tem Na com o valor escolhido
# pode preencher o df inteiro, ou uma serie
print('\nFILLNA\n')
print('PREENCHENDO TUDO COM 0:\n',df.fillna(0))
print('\nPREENCHENDO COM AS MÉDIAS:\n', df.fillna(df[['idade', 'salario']].mean()))
df['idade'] = df['idade'].fillna(0)
df['salario'] = df['salario'].fillna(0)
print('\nPREENCHENDO SERIES:\n', df)
print('\nPREENCHENDO UMA LINHA:\n', df.fillna({'nome':'alguem', 'idade': 0}))