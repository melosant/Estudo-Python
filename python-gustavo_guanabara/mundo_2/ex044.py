preco = float(input('Informe o preço do produto : '))

print("""
1 - À VISTA (10% DE DESCONTO)
2 - À VISTA NO CARTÃO (5% DE DESCONTO)
3 - PARCELAMENTO EM ATE 2X (PREÇO NORMAL)
4 - PARCELAMENTO 3X OU MAIS (20% DE JUROS)
      
      SELECIONE A OPÇÃO:""")

opcao = int(input())

if opcao == 1:
    print(f'PREÇO FINAL : R${preco * 0.90:.2f}')
elif opcao == 2:
    print(f'PREÇO FINAL : R${preco * 0.95:.2f}')
elif opcao == 3:
    print(f'''
PREÇO FINAL : R${preco:.2f}
PARCELAMENTO : 2X DE R${preco/2:.2f}''')
else:
    numero = int(input('Qtd de parcelas (min.3) : '))
    if numero < 3 :
        print('QUANTIDADE NÃO PERMITIDA !')
    else:
        preco_reaj = preco * 1.20
        print(f'''
PREÇO FINAL : R${preco_reaj:.2f}
PARCELAMENTO : {numero}X DE R${preco_reaj/numero:.2f}''')