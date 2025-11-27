def leianome(msg):
    while True:
        try:
            nome = input(msg).title()
            nome_f = nome.replace(' ', '')
            if nome_f.isalpha():
                break
            else:
                print('\033[1;91mDigite um nome válido.\033[m', end=' ')
        except KeyboardInterrupt:
            print('\033[1;91mO usuário desejou não inserir o nome.\033[m')
            nome = '<Não Informado>'
            break
        except:
            print('\033[1;91mHouve um erro no cadastro do nome.\033[m')
    return nome

def leiaint(msg):
    valor = 0
    while True:
        try:
            valor = int(input(msg))
            break
        except KeyboardInterrupt:
            print('\033[1;91mO usuário preferiu não informar a idade.\033[m')
            break
        except:
            print('\033[1;91mERRO! Digite uma idade válida.\033[m', end=' ')
    return valor