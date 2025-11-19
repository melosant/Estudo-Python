valor = float(input('Digite o valor da casa desejada : R$'))
anos = int(input('Em quantos anos deseja pagar esta casa ? '))
salario = float(input('Digite o valor do seu salario : R$'))

prestacao = valor / (anos * 12)

if prestacao > (salario * 0.30):
    print('Financiamente negado!')
else:
    print(f'''
VALOR DO IMÓVEL = R${valor}
VALOR DAS PRESTAÇÕES = R${prestacao:.2f} durante {anos} anos.''')