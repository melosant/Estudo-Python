# Tamanho do primeiro nome
# Aula 55

nome = input('Digite seu primeiro nome: ')

if len(nome) > 0: 
    if len(nome) <= 4:
        print('Seu nome é curto.')
    elif len(nome) > 4 and len(nome) < 7:
        print('Seu nome é normal.')
    else:
        print('Seu nome é longo.')
else:
    print('Digite ao menos uma letra.')