import streamlit as st
import pandas as pd 
import requests
import datetime

# põe a função em cache por 1 dia - maior rapidez
@st.cache_data(ttl='1day')
def get_selic():
    '''
    conexão com a api da taxa selic
    '''
    url = 'https://www.bcb.gov.br/api/servico/sitebcb/historicotaxasjuros'
    resp = requests.get(url)
    df = pd.DataFrame(resp.json()['conteudo'])

    df["DataInicioVigencia"] = pd.to_datetime(df['DataInicioVigencia']).dt.date
    df["DataFimVigencia"] = pd.to_datetime(df['DataFimVigencia']).dt.date
    df["DataFimVigencia"] = df['DataFimVigencia'].fillna(datetime.datetime.today().date())
    return df


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

def main_metas():
    col1, col2 = st.columns(2)

    data_inicio_meta = col1.date_input('Início da Meta : ', max_value=df_stats.index.max())
    # pega todos os indices q antecedem ou sao iguais a data selecionada como inicial (intervalo entre uma e outra)
    data_filtrada = df_stats.index[df_stats.index <= data_inicio_meta][-1]

    # input informações financeiras
    salario_bruto = col2.number_input('Salário Bruto', min_value=0., format='%.2f')
    salario_liq = col2.number_input('Salário Líquido', min_value=0., format='%.2f')
    custos_fix = col1.number_input('Custos Fixos', min_value=0., format='%.2f')
    
    # patrimonio inicial na data escolhida
    valor_inicio = df_stats.loc[data_filtrada]['Valor']
    with st.container(border=True):
        st.markdown(f'**Patrimônio no início da meta:** R$ {valor_inicio:.2f}')
    
    # pega a taxa selic e faz scrapping da data mais próxima que a taxa foi atualizada
    selic_gov = get_selic()
    filter_selic_date = (selic_gov['DataInicioVigencia'] < data_inicio_meta) & (selic_gov['DataFimVigencia'] > data_inicio_meta)
    selic_default = selic_gov[filter_selic_date]['MetaSelic'].iloc[0] 

    # exibição da selic na data + fórmulas da selic para rendimento
    selic = st.number_input('Selic', min_value=0., value=selic_default, format='%.2f')
    selic_ano = selic / 100
    selic_mes = (selic_ano + 1) ** (1/12) - 1

    # cálculos de rendimento e patrimonio
    rendimento_ano = valor_inicio * selic_ano
    rendimento_mes = valor_inicio * selic_mes
    mensal = salario_liq - custos_fix + rendimento_mes
    anual = 12 * (salario_liq - custos_fix) + rendimento_ano

    # exibição das info's
    pot_col1, pot_col2 = st.columns(2)
    with pot_col1.container(border=True):
        st.markdown(f'**Potencial Arrecadação Mês**:\n\n R$ {mensal:.2f}',
                    help=f'{salario_liq:.2f} + (-{custos_fix:.2f}) + {rendimento_mes:.2f}')
    
    with pot_col2.container(border=True):
        st.markdown(f'**Potencial Arrecadação Anual**:\n\n R$ {anual:.2f}',
                    help=f'12 * {salario_liq} + (-{custos_fix}) + {rendimento_ano}')

    meta_col1, meta_col2 = st.columns(2)
    with meta_col1.container(border=True):
        meta_estipulada = st.number_input(f'**Meta Estipulada**', format='%.2f', value=anual)
        patrimonio_final = meta_estipulada + valor_inicio 
    with meta_col2.container(border=True):
        st.markdown(f'**Patrimônio Estimado Pós-Meta**:\n\n {patrimonio_final:.2f}',
                    help=f'{meta_estipulada} + {valor_inicio}')
        
    return data_inicio_meta, valor_inicio, meta_estipulada, patrimonio_final

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
    columns_config_meses = {
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
        st.dataframe(df_stats, column_config=columns_config_meses)
    
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

        tab_main, tab_data_meta, tab_graph = st.tabs(tabs=['Configuração', 'Dados', 'Gráfico'])

        with tab_main:
            data_inicio_meta, valor_inicio, meta_estipulada, patrimonio_final = main_metas()
   
        with tab_data_meta:
            meses = pd.DataFrame({
                'Data Referência':[(data_inicio_meta + pd.DateOffset(months=i)) for i in range(1, 13)],
                'Meta Mensal':[valor_inicio + round(meta_estipulada / 12, 2) * i for i in range(1, 13)],
                })
            meses['Data Referência'] = meses['Data Referência'].dt.strftime("%Y-%m")
            
            df_patrimonio = df_stats.reset_index()[['Data', 'Valor']]
            df_patrimonio['Data Referência'] = pd.to_datetime(df_patrimonio['Data']).dt.strftime('%Y-%m')
            meses = meses.merge(df_patrimonio , how='left', on='Data Referência')

            meses = meses[['Data Referência', 'Meta Mensal', 'Valor']]
            meses['Atingimento Mês %'] = meses['Valor'] / meses['Meta Mensal']
            meses['Atingimento Ano %'] = meses['Valor'] / patrimonio_final
            meses['Atingimento Esperado'] = meses['Meta Mensal'] / patrimonio_final
            meses = meses.set_index('Data Referência')

            columns_config_meses = {
        'Meta Mensal': st.column_config.NumberColumn('Meta Mensal', format='R$ %.2f'),
        'Valor': st.column_config.NumberColumn('Valor Atingido', format='R$ %.2f'),
        'Atingimento Mês %': st.column_config.NumberColumn('Atingimento Mês %', format='percent'),
        'Atingimento Ano %': st.column_config.NumberColumn('Atingimento Ano %', format='percent'),
        'Atingimento Esperado': st.column_config.NumberColumn('Atingimento Esperado', format='percent'),
    }
            st.dataframe(meses, column_config=columns_config_meses)

        with tab_graph:
            st.line_chart(meses[['Atingimento Ano %', 'Atingimento Esperado']])