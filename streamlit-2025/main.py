import streamlit as st
import pandas as pd 

def calc_general_stats(df):
    '''
    Função que calcula todas as colunas e retorna já calculado.

    :param df: dataframe
    '''
    # agrupa datas e valor, e cria uma nova coluna que abaixa uma célula cada valor
    df_data = df.groupby(by='Data')[['Valor']].sum()
    df_data['lag_1'] = df_data['Valor'].shift(1)

    df_data['Diferença Mensal Abs.'] = df_data['Valor'] - df_data['lag_1']
    df_data['Média 6M DIferença Mensal Abs.'] = df_data['Diferença Mensal Abs.'].rolling(6).mean()
    df_data['Média 12M DIferença Mensal Abs.'] = df_data['Diferença Mensal Abs.'].rolling(12).mean()
    df_data['Média 24M DIferença Mensal Abs.'] = df_data['Diferença Mensal Abs.'].rolling(24).mean()

    df_data['Diferença Mensal Relativa'] = df_data['Valor'] / df_data['lag_1'] - 1

    df_data['Evolução 6M Total'] = df_data['Valor'].rolling(6).apply(lambda x: x[-1] - x[0])
    df_data['Evolução 12M Total'] = df_data['Valor'].rolling(12).apply(lambda x: x[-1] - x[0])
    df_data['Evolução 24M Total'] = df_data['Valor'].rolling(24).apply(lambda x: x[-1] - x[0])

    df_data['Evolução 6M Relativa'] = df_data['Valor'].rolling(6).apply(lambda x: x[-1] / x[0] - 1)
    df_data['Evolução 12M Relativa'] = df_data['Valor'].rolling(12).apply(lambda x: x[-1] / x[0] - 1)
    df_data['Evolução 24M Relativa'] = df_data['Valor'].rolling(24).apply(lambda x: x[-1] / x[0] - 1)

    df_data['Diferença Anual'] = df_data['Valor'].rolling(13).apply(lambda x: x[-1] - x[0])

    # dropa a coluna criada anteriormente para cálculo
    df_data = df_data.drop('lag_1', axis=1)

    return df_data

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
    columns_fmt = {"Valor": st.column_config.NumberColumn("Valor", format="R$ %.2f")}
    exp1.dataframe(df, hide_index=True, column_config=columns_fmt)
    
    # criação de um expander + abas dentro delas
    exp2 = st.expander('Dados Institucionais')
    tab_data, tab_history, tab_share = exp2.tabs(['Dados', 'Histórico', 'Distribuição'])

    # visão das instituições
    df_instituicao = df.pivot_table(index='Data', columns='Instituição', values='Valor')
    with tab_data:
        st.dataframe(df_instituicao, hide_index=False,column_config={
            "Death Star": st.column_config.NumberColumn("Death Star", format='R$ %.2f'),
            "Iron Bank": st.column_config.NumberColumn("Iron Bank", format='R$ %.2f'),
            "Republic Bank": st.column_config.NumberColumn("Republic Bank", format='R$ %.2f'),
            "TMW Bank": st.column_config.NumberColumn("TMW Bank", format='R$ %.2f')
        })
    
    # grafico temporal
    with tab_history:
        st.line_chart(df_instituicao)

    # obtém a distribuição da data selecionada 
    with tab_share:
        # Filtro de data
        date = st.selectbox("Selecione a data que deseja conferir", options=df_instituicao.index)
        st.bar_chart(df_instituicao.loc[date])

    # compilado geral
    exp3 = st.expander('Estatísticas Gerais')
    # função que calcula as stats gerais
    df_stats = calc_general_stats(df)
    columns_config = {
        'Valor': st.column_config.NumberColumn('Valor', format='R$ %.2f'),
        'Diferença Mensal Abs.': st.column_config.NumberColumn('Diferença Mensal Abs.', format='R$ %.2f'),
        'Média 6M DIferença Mensal Abs.': st.column_config.NumberColumn('Média 6M DIferença Mensal Abs.', format='R$ %.2f'),
        'Média 12M DIferença Mensal Abs.': st.column_config.NumberColumn('Média 12M DIferença Mensal Abs.', format='R$ %.2f'),
        'Média 24M DIferença Mensal Abs.': st.column_config.NumberColumn('Média 24M DIferença Mensal Abs.', format='R$ %.2f'),
        'Evolução 6M Total': st.column_config.NumberColumn('Evolução 6M Total', format='R$ %.2f'),
        'Evolução 12M Total': st.column_config.NumberColumn('Evolução 12M Total', format='R$ %.2f'),
        'Evolução 24M Total': st.column_config.NumberColumn('Evolução 24M Total', format='R$ %.2f'),
        'Diferença Anual': st.column_config.NumberColumn('Diferença Anual', format='R$ %.2f'),
        'Diferença Mensal Relativa': st.column_config.NumberColumn('Diferença Mensal Relativa', format='percent'),
        'Evolução 6M Relativa': st.column_config.NumberColumn('Evolução 6M Relativa', format='percent'),
        'Evolução 12M Relativa': st.column_config.NumberColumn('Evolução 12M Relativa', format='percent'),
        'Evolução 24M Relativa': st.column_config.NumberColumn('Evolução 24M Relativa', format='percent'),
        
    }

    tab_stats, tab_abs, tab_rel = exp3.tabs(['Dados', 'Histórico de Evolução', 'Crescimento Relativo'])
    with tab_stats:
        st.dataframe(df_stats, column_config=columns_config)
    
    # exibição gráfico valor absoluto
    with tab_abs:
        abs_cols = ['Diferença Mensal Abs.', 
                'Média 6M DIferença Mensal Abs.', 
                'Média 12M DIferença Mensal Abs.',
                'Média 24M DIferença Mensal Abs.']
        st.line_chart(df_stats[abs_cols])

    #  exibição gráfico valor relativo
    with tab_rel:
        rel_cols = ['Diferença Mensal Relativa',
                'Evolução 6M Relativa',
                'Evolução 12M Relativa',
                'Evolução 24M Relativa']
        st.line_chart(data=df_stats[rel_cols])

    # exibição metas
    with st.expander('Metas'):
        col1, col2 = st.columns(2)

        data_inicio_meta = col1.date_input('Início da Meta : ', max_value=df_stats.index.max())
        # pega todos os indices q antecedem ou sao iguais a data selecionada como inicial (intervalo entre uma e outra)
        data_filtrada = df_stats.index[df_stats.index <= data_inicio_meta][-1]

        salario_bruto = col2.number_input('Salário Bruto', min_value=0., format='%.2f')
        salario_liq = col2.number_input('Salário Líquido', min_value=0., format='%.2f')
        custos_fix = col1.number_input('Custos Fixos', min_value=0., format='%.2f')
        
        valor_inicio = df_stats.loc[data_filtrada]['Valor']
        with st.container(border=True):
            st.markdown(f'<p style="text-align: center;"><b>Valor no início da meta: R$ {valor_inicio:.2f}', unsafe_allow_html=True)


        pot_col1, pot_col2 = st.columns(2)
        mensal = salario_liq - custos_fix
        with pot_col1.container(border=True):
            st.markdown(f'**Potencial Arrecadação Mês**:\n\n R$ {mensal:.2f}')
        
        mensal = salario_liq - custos_fix
        anual = mensal * 12
        with pot_col2.container(border=True):
            st.markdown(f'**Potencial Arrecadação Anual**:\n\n R$ {anual:.2f}')

        meta_col1, meta_col2 = st.columns(2)
        with meta_col1.container(border=True):
            meta_estipulada = st.number_input(f'**Meta Estipulada**', min_value=0., format='%.2f', value=anual)
            patrimonio_final = meta_estipulada + valor_inicio 
        with meta_col2.container(border=True):
            st.markdown(f'**Patrimônio Estimado Pós-Meta**:\n\n {patrimonio_final:.2f}')
