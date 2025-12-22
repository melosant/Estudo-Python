import pandas as pd
import sqlalchemy

# importando a query escrita
with open('pandas-2025/dia09/etl.sql') as open_file:
    query = open_file.read()

'''
1. Abriu a ETL criada na pasta
2. Envia a query para o banco de dados
3. Retornou os dados do banco baseado na query escrita
'''
engine = sqlalchemy.create_engine('sqlite:///pandas-2025/data/olist.db')
df = pd.read_sql_query(query, con=engine)
print(df)

# to sql (cluster não feito)
# replace usado para que drope a tabela e a salve novamente caso já exista
df.to_sql('seller_scluster',
            con=engine, 
            index=False,
            if_exists='replace',)