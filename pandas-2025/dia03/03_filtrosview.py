import pandas as pd

clientes = pd.read_csv('pandas-2025/data/clientes.csv', sep=';')

filtro = clientes['qtdePontos'] == 0

# não é feita uma cópia, está apontando para as linhas filtradas somente
# há duas variáveis que apontam para as mesmas linhas filtradas
# clientes_0 = clientes[filtro]
clientes_0 = clientes[filtro].copy() # caso queira desassociar

clientes_0['flag_1'] = 1

print(clientes)
print(clientes_0)