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
    df["Data"] = pd.to_datetime(df["Data"], format='%d/%m/%Y').dt.date

    exp1 = st.expander('Dados Brutos')

    # exibição dos dados
    columns_fmt = {"Valor": st.column_config.NumberColumn("Valor", format="R$ %f")}
    exp1.dataframe(df, hide_index=True, column_config=columns_fmt)
    
    # criação de um expander + abas dentro delas
    exp2 = st.expander('Dados Institucionais')
    tab_data, tab_history, tab_share = exp2.tabs(['Dados', 'Histórico', 'Distribuição'])

    # visão das instituições
    df_instituicao = df.pivot_table(index='Data', columns='Instituição', values='Valor')
    with tab_data:
        st.dataframe(df_instituicao, hide_index=False,column_config={
            "Death Star": st.column_config.NumberColumn("Death Star", format='R$ %f'),
            "Iron Bank": st.column_config.NumberColumn("Iron Bank", format='R$ %f'),
            "Republic Bank": st.column_config.NumberColumn("Republic Bank", format='R$ %f'),
            "TMW Bank": st.column_config.NumberColumn("TMW Bank", format='R$ %f')
        })
    
    # grafico temporal
    with tab_history:
        st.line_chart(df_instituicao)

    # obtém a distribuição da data selecionada 
    with tab_share:
    
# FUNçÂO QUE EXIBE UM INPUT DE CALENDÁRIO
#     date = st.date_input('Data para Distribuição',
#                        min_value=df_instituicao.index.min(),
#                          max_value=df_instituicao.index.max())
#     if date not in df_instituicao.index:
#         st.warning("Entre com uma data válida! Todo dia 5 de cada mês.")  
#     else:

        # Filtro de data
        date = st.selectbox("Selecione a data que deseja conferir", options=df_instituicao.index)
        st.bar_chart(df_instituicao.loc[date])