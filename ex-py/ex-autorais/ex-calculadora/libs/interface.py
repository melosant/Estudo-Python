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