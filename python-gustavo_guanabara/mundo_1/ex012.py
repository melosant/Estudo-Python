# programa 12 : aplicando 5% no valor de um produto
# Operadores Aritméticos (Aula 7)

valor = float(input('Digite o valor do produto : R$'))
desconto = valor * 0.95
# desconto = valor - (valor * 5/100)

print(f'O valor do produto era R${valor}, mas foi aplicado um desconto de 5% e seu valor final é de R${desconto:.2f}.')