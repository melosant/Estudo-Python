mais_velhon = ''
mais_velhoi = 0
media = 0
qtdm = 0

for i in range(4):
    print('=-=-=-=-=-=-=-=-=-=-=-=')
    nome = input('Digite o nome : ')
    idade = int(input('Digite a idade : '))
    sexo = input('Informe o sexo (M/F) : ')
    media += idade

    if idade > mais_velhoi and sexo == 'M':
        mais_velhon = nome
        mais_velhoi = idade

    if sexo == 'F' and idade < 20:
        qtdm += 1

media = media / 4

print(f'''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
MÉDIA DE IDADE DO GRUPO : {media}
NOME DO HOMEM MAIS VELHO : {mais_velhon}, {mais_velhoi} anos.
QTD DE MULHERES COM MENOS DE 20 ANOS : {qtdm}''')