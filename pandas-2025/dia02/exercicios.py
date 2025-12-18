import pandas as pd

transacoes = pd.read_csv('pandas-2025/data/transacoes.csv', sep=';')
transacoes['valores_1'] = 1
print(transacoes)

transacoes.to_csv('pandas-2025/dia02/transacoes_1.csv')