import pandas as pd

'''
Leia o arquivo transacoes.csv com a formatação correta;
Adicione uma coluna com valores 1;
Salve o dataframe com nome: transacoes_1.csv
'''

transacoes = pd.read_csv('pandas-2025/data/transacoes.csv', sep=';')
transacoes['valores_1'] = 1
print(transacoes)

transacoes.to_csv('pandas-2025/dia02/transacoes_1.csv')