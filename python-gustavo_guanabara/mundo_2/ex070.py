total = mais_mil = 0
prod_bar_valor = 999999999999999999999
prod_bar_nome = ''

print('''
=-=-=-=-=-
   LOJA
-=-=-=-=-=\n''')

while True:
    nome = input('Nome do produto: ')
    valor = float(input('Valor do produto : R$'))
    total += valor
    if valor > 1000:
        mais_mil += 1
    if valor < prod_bar_valor:
        prod_bar_nome = nome
        prod_bar_valor = valor

    while True:
        escolha = input('Deseja continuar [S/N]: ').upper()
        if escolha == 'S' or escolha == 'N':
            break
    if escolha == 'N':
        break

print(f'''
=-=-= FIM DO PROGRAMA =-=-=
O total da compra foi R${total:.2f}.
Temos {mais_mil} produtos custando mais que R$1000.00
O produto mais barato foi {prod_bar_nome} custando R${prod_bar_valor}.''')
