from libs.interface import *
import datetime

def opcaoum(price, peso):
    frete = 0
    if peso < 2.0:
        frete = 30.00
        total = price + frete
    else:
        frete = 50.00
        total = price + frete

    return total, frete

def opcaodois(price, peso):
    frete = 0
    if peso < 2.0:
        frete = 25.00
        total = price + frete
    else:
        frete = 45.00
        total = price + frete

    return total, frete

def opcaotres(price, peso):
    frete = 0
    if peso < 2.0:
        frete = 35.00
        total = price + frete
    else:
        frete = 55.00
        total = price + frete

    return total, frete

def opcaoquatro(price, peso):
    frete = 0
    if peso < 2.0:
        frete = 40.00
        total = price + frete
    else:
        frete = 60.00
        total = price + frete

    return total, frete

def data_compra():
    data = datetime.date.today()
    dataf = datetime.date.strftime(data, '%d/%m/%Y')
    prazoentrega = 10
    prazo_delta = datetime.timedelta(days=prazoentrega)
    entrega = data + prazo_delta
    entrega = datetime.date.strftime(entrega, '%d/%m/%Y')

    return dataf, entrega

def resumo(nome, codigo, price, peso, local, frete, total, data, entrega):
    linha(' RESUMO DA COMPRA : ')
    print(' RESUMO DA COMPRA : ')
    linha(' RESUMO DA COMPRA : ')
    print(f'''
\033[1;93m=> NOME DO PRODUTO :\033[m {nome}
\033[1;93m=> CÓDIGO DO PRODUTO :\033[m {codigo}
\033[1;93m=> PREÇO DO PRODUTO :\033[m \033[1;32mR${price:.2f}
\033[1;93m=> PESO DO PRODUTO :\033[m {peso}kg
\033[1;93m=> LOCAL DE ENTREGA :\033[m {local}
\033[1;93m=> PREÇO DO FRETE :\033[m \033[1;32mR${frete:.2f}
\033[1;93m=> PREÇO TOTAL DA COMPRA :\033[m \033[1;32mR${total:.2f}
\033[1;93m=> DATA DA COMPRA :\033[m {data}
\033[1;93m=> DATA PREVISTA DA ENTREGA :\033[m {entrega}''')
    linha(' ' * 40)