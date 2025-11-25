# programa 17 : calculo da hipotenusa
# Utilizando módulos (Aula 8)

import math
catop = float(input('Digite o valor do cateto oposto : '))
catad = float(input('Digite o valor do cateto adjacente : '))
# hipo = (catop ** 2 + catad ** 2) ** (1/2)
hipo = math.hypot(catop, catad) # usando módulo math

print(f'O valor da hipotenusa é {hipo:.2f}.')