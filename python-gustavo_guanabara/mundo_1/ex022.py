# programa 22 : funções para manipulação de strings
# Manipulando Strings (Aula 9)

nome = str(input('Digite seu nome completo : ')).strip() # strip somente para retirar os espaços
print(f'NOME EM MAIÚSCULO : {nome.upper()}')
print(f'NOME EM MINÚSCULO : {nome.lower()}')
print(f'QTD LETRAS AO TODO ? {len(nome) - nome.count(' ')}') 
# print(f'QTD LETRAS DO PRIMEIRO NOME : {nome.find(' ')}') # encontra o primeiro espaço, a posição dele é a quantidade de letras
nome_dividido = nome.split()
print(f'QTD DE LETRAS PRIMEIRO NOME : {len(nome_dividido[0])}') # primeiro item da lista é o primeiro nome