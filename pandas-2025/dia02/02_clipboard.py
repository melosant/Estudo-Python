import pandas as pd

# é o ctrl+c (copiei a bobo.csv)
# é usado para algo experimental, investigativo de um arquivo
df = pd.read_clipboard(sep=';')
print(df)