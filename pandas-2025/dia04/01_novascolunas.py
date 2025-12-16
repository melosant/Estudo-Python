import pandas as pd
import numpy as np

df = pd.read_csv('pandas-2025/data/clientes.csv', sep=';')

# retorna uma serie com os valores mais 100 (operação direta) e os adiciona numa nova coluna
df['points_100'] = df['qtdePontos'] + 100

# para operar entre series, é necessário ter a mesma dimensão
# operação or
df['EmailorTwitch'] = df['flEmail'] + df['flTwitch']
print(df.head())

# operação and 
df['EmailandTwitch'] = df['flEmail'] * df['flTwitch']
print(df.head())

# total de redes sociais
df['qtdeSocial'] = df['flEmail'] + df['flTwitch'] + df['flYouTube'] + df['flBlueSky'] + df['flInstagram']
print(df.head())

# só mostra 1 se tiver todas as redes
df['allSocial'] = df['flEmail'] * df['flTwitch'] * df['flYouTube'] * df['flBlueSky'] * df['flInstagram']
print(df.head())

# transformando uma coluna usando numpy para funções matemáticas
print(np.log(df['qtdePontos'] + 1)) # +1 usado somente para evitar infinitos