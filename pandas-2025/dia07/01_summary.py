import pandas as pd

idades = [32, 44, 12, 54, 65, 89, 15, 15, 55, 32, 48, 44, 25, 18, 28]
idades = pd.Series(idades)
# são exemplos de agregação, sumarização
# print(idades.sum(),idades.max(),idades.min(),idades.mean(), idades.describe())

clientes = pd.read_csv('pandas-2025/data/clientes.csv', sep=';')
print(clientes['flTwitch'].sum()) # qts pessoas tem a twitch
print(clientes['flTwitch'].mean()) # % de pessoas q tem a twitch

redes_sociais = ['flEmail', 'flTwitch', 'flYouTube', 'flBlueSky', 'flInstagram']
# aplica a media em cada uma das colunas do df
print(clientes[redes_sociais].mean())
# selecionando somente em colunas numericas
print(clientes.select_dtypes('number').mean())
# ou dessa forma
num_columns = clientes.dtypes[~(clientes.dtypes == 'object')].index.tolist()
print(clientes[num_columns].describe())