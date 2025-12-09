import streamlit as st
import pandas as pd 

st.set_page_config(page_title='Finanças', page_icon='💰')
st.markdown('''
# Boas Vindas!
## Nosso APP Financeiro.

Espero que você curta a experiência da nossa solução para organização financeira.
''')

# Widget para upload de arquivo
file_upload = st.file_uploader(label='Faça upload dos dados aqui', type=['csv'])

if file_upload:

    # leitura dos dados
    df = pd.read_csv(file_upload)

    # exibição dos dados
    columns_fmt = {"Valor": st.column_config.NumberColumn("Valor", format="R$ %f")}
    st.dataframe(df, hide_index=True, column_config=columns_fmt)