cadastro = {}

cadastro['Nome'] = str(input('Nome : ').capitalize())
cadastro['Idade'] = int(input('Ano de nascimento : '))
cadastro['CTPS'] = int(input('Carteira de Trabalho (0 se nao tiver) : '))
cadastro['Idade'] = 2025 - cadastro['Idade']

if cadastro['CTPS'] == 0:
    print()
    print('=-' * 20)
    for k,v in cadastro.items():
        print(f'{k} tem o valor {v}.')
    print('=-' * 20)
    
else:
    cadastro['AnoContratação'] = int(input('Ano da Contratação : '))
    cadastro['Salário'] = float(input('Salário : R$'))
    idadecontratacao = cadastro['Idade'] - (2025 - cadastro['AnoContratação'])
    cadastro['Aposentadoria'] = idadecontratacao + 35

    print()
    print('=-' * 20)
    for k,v in cadastro.items():
        print(f'{k} tem o valor {v}.')
    print('=-' * 20)