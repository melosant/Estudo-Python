# programa 24 : confere se a cidade digitada começa com SANTO
# Manipulando Strings (Aula 9)

cidade = input('Digite o nome da cidade que você nasceu : ')
divisao = cidade.upper().split()
print('SANTO' in divisao[0])