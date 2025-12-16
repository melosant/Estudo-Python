import pandas as pd

df_clientes = pd.read_csv('pandas-2025/data/clientes.csv', sep=';')

#------- AMOSTRAS ---------
# método q exibe as 5 primeiras linhas por padrão
print(df_clientes.head(n=10))

# método q exibe as 5 ultimas linhas por padrão
print(df_clientes.tail(n=10))

# método que exibe 5 linhas aleatórias por padrão
print(df_clientes.sample(n=10))

# atributo que mostra a quantidade de linhas e colunas
print('DIMENSÃO: ', df_clientes.shape)

# atributo que exibe os nomes das colunas
print('NOME DAS COLUNAS: ', df_clientes.columns)

# atributo que exibe os índices do df (se não for definido anteriormente, o pandas cria um sequencial)
print('ÍNDICES: ', df_clientes.index)

# método q exibe informações principais do df
# a memória é dada como uma inferência caso não passe parâmetro para saber o valor real
print(df_clientes.info(memory_usage='deep'))

# retorna uma series com as keys sendo as colunas e os values o seu tipo
print('TIPOS DAS COLUNAS: ', df_clientes.dtypes)
print('TIPO DE UMA COLUNA ESPECÍFICA: "qtdePontos" =', df_clientes.dtypes['qtdePontos'])

