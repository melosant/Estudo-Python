from datetime import date
contmaior = 0
contmenor = 0
ano_atual = date.today().year
for i in range(1, 8):
    ano_nasc = int(input(f'Digite o ano de nascimento da {i}° pessoa :'))
    diferenca = ano_atual - ano_nasc
    if diferenca >= 18:
        contmaior += 1
    else:
        contmenor += 1

print(f'''
QUANTIDADE DE MAIORES DE IDADE : {contmaior}
QUANTIDADE DE MENORES DE IDADE : {contmenor}''')