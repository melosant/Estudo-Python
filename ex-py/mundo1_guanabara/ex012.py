valor = float(input('Digite o valor do produto : R$'))
desconto = valor * 0.95
# desconto = valor - (valor * 5/100)

print(f'O valor do produto era R${valor}, mas foi aplicado um desconto de 5% e seu valor final é de R${desconto:.2f}.')