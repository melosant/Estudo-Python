def area(l, c):
    print(f'A área de um terreno {l}mx{c}m é {l * c:.2f}m².')

print('Controle de terreno') 
print('-' * 20)

larg = float(input('Informe a largura do terreno (em m): '))
comp = float(input('Informe o comprimento do terreno (em m): '))
area(larg, comp)