import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///pandas-2025/data/olist.db')

clientes = pd.read_sql_table(table_name='tb_customers', con=engine)
print(clientes)

query = 'SELECT * FROM tb_customers LIMIT 100'
df_100 = pd.read_sql_query(query, con=engine)
print(df_100)