import pandas as pd

df = pd.read_csv('pandas-2025/data/clientes.csv', sep=';')

def get_last_id(idclient):
    return idclient.split('-')[-1]

# ------------ MANEIRA RETRÓGRADA --------------
# id_novo = []
# for i in df['idCliente']:
#     novo = get_last_id(i)
#     id_novo.append(novo)

# df['novo_id'] = id_novo
# print(df.head())
   
# ------------- USANDO APPLY ------------------
# vai percorrer por n elemntos na serie e aplicar a função
df['novo_id'] = df['idCliente'].apply(get_last_id)        
print(df.head())