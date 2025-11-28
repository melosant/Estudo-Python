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