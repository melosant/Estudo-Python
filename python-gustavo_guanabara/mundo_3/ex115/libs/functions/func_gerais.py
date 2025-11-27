def leianome(msg):
    '''
    Função para leitura do nome digitado pelo usuário.
    param msg : mensagem que será exibida no terminal
    '''
    while True:
        try:
            nome = input(msg).title()
            nome_f = nome.strip().replace(' ', '') # retira os espaços.
            if nome_f.isalpha(): # confere se o nome contém somente letras (sem espaço)
                break
            else: # caso não tenha, ou usuário deixe em branco.
                print('\033[1;91mDigite um nome válido.\033[m', end=' ')
        except KeyboardInterrupt: # caso queira interromper
            print('\033[1;91mO usuário desejou não inserir o nome.\033[m')
            nome = '<Não Informado>'
            break
        except: # tratamento de qualquer erro que venha acontecer
            print('\033[1;91mHouve um erro no cadastro do nome.\033[m')
    return nome

def leiaint(msg):
    '''
    Função para leitura da idade inserida pelo usuário tratando os erros que possam vir na digitação
    param msg: mensagem que será exibida no terminal
    '''
    valor = 0 # idade iniciada zerada 
    while True:
        try:
            valor = int(input(msg)) # digitada corretamente
            break
        except KeyboardInterrupt: # caso queira interromper
            print('\033[1;91mO usuário preferiu não informar a idade.\033[m')
            break
        except: # qualuqer outro erro, nenhum número válido inserido
            print('\033[1;91mERRO! Digite uma idade válida.\033[m', end=' ')
    return valor