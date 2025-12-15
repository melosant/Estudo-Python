import pandas as pd

# ler o csv
df = pd.read_csv("pandas-2025/data/clientes.csv")

# salvar o csv, parquet e xlsx   (index=False ou True)
df.to_csv('pandas-2025/dia02/clientes.csv', index=False)
df.to_parquet('pandas-2025/dia02/clientes.parquet', index=False)
df.to_excel('pandas-2025/dia02/clientes.xlsx', index=False)

# pode definir o separador na hora de salvar e ler o arquivo
df_bobo = pd.read_csv('pandas-2025/data/bobo.csv', sep=';')
print(df_bobo)

