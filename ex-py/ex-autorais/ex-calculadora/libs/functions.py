def linha(tam):
    print('-' * len(tam))

def exibirmenu(msg):
    linha(msg)
    print(msg)
    linha(msg)

def localentrega(msg):
    linha(msg)
    print(msg)
    print('''
\033[1;95m[1] - Região Sul
[2] - Região Sudeste
[3] - Região Norte
[4] - Região Nordeste\033[m''')
    linha(msg)

def leianome(msg):
    '''
    Função para leitura do nome do produto digitado pelo usuário.
    param msg : mensagem que será exibida no terminal
    '''
    while True:
        try:
            nome = input(msg).title()
            nome_f = nome.strip().replace(' ', '') # retira os espaços.
            if nome_f.isalnum(): # confere se o nome contém somente letras e números (sem espaço)
                break
            else: # caso não tenha, ou usuário deixe em branco.
                print('\033[1;91mDigite um nome válido.\033[m', end=' ')
        except KeyboardInterrupt: # caso queira interromper
            print('\033[1;91mO usuário desejou cancelar a compra.\033[m')
            nome = 'N'
            break
        except: # tratamento de qualquer erro que venha acontecer
            print('\033[1;91mHouve um erro no cadastro do nome.\033[m')
    
    if nome == 'N':
        nome = None
        return nome
    else:
        return nome

def leiacode(msg):
    '''
    Função para leitura do código digitado pelo usuário.
    param msg : mensagem que será exibida no terminal
    '''
    while True:
        try:
            cod = input(msg)
            if cod.isnumeric(): # se for somente numeros 
                break
            else: # caso não tenha, ou usuário deixe em branco.
                print('\033[1;91mDigite um código válido.\033[m', end=' ')
        except KeyboardInterrupt: # caso queira interromper
            print('\033[1;91mO usuário desejou não inserir o código.\033[m')
            cod = ''
            break
        except: # tratamento de qualquer erro que venha acontecer
            print('\033[1;91mHouve um erro no cadastro do código do produto.\033[m')
    if cod == '':
        cod = None
        return cod
    else:
        return cod


def leiafloat(msg):      
    '''
    Função que verifica se um numero real foi digitado
    param msg : msg a ser exibida no terminal
    '''
    valor = 0
    while True:
        try:
            valor = float(input(msg))
            break
        except KeyboardInterrupt:
            print('\033[1;91mO usuário preferiu não digitar o valor pedido.\033[m')
            break
        except:
            print('\033[1;91mERRO! Digite um número real válido.\033[m', end=' ')
    if valor == 0:
        return None
    else:
        return valor

def leiaint(msg):
    '''
    Função que verifica se um numero inteiro foi digitado
    param msg : msg a ser exibida no terminal
    '''
    valor = 0
    while True:
        try:
            valor = int(input(msg))
            if valor > 0 and valor < 5:
                break
            else:
                print('\033[1;91mERRO! Digite uma opção válida.\033[m', end=' ')
        except KeyboardInterrupt:
            print('\033[1;91mO usuário preferiu cancelar a entrega.\033[m')
            valor = None
            break
        except:
            print('\033[1;91mERRO! Digite uma opção válida.\033[m', end=' ')
    return valor

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

def resumo(nome, codigo, price, peso, local, frete, total, data, entrega):
    linha(' RESUMO DA COMPRA : ')
    print(' RESUMO DA COMPRA : ')
    linha(' RESUMO DA COMPRA : ')
    print(f'''
\033[1;93m=> NOME DO PRODUTO :\033[m {nome}
\033[1;93m=> CÓDIGO DO PRODUTO :\033[m {codigo}
\033[1;93m=> PREÇO DO PRODUTO :\033[m \033[1;32mR${price}
\033[1;93m=> PESO DO PRODUTO :\033[m {peso}kg
\033[1;93m=> LOCAL DE ENTREGA :\033[m {local}
\033[1;93m=> PREÇO DO FRETE :\033[m \033[1;32mR${frete}
\033[1;93m=> PREÇO TOTAL DA COMPRA :\033[m \033[1;32mR${total}
\033[1;93m=> DATA DA COMPRA :\033[m {data}
\033[1;93m=> DATA PREVISTA DA ENTREGA :\033[m {entrega}''')
    linha(' ' * 40)