# programa 18 : seno, cos e tang de um angulo
# Utilizando módulos (Aula 8)

from math import sin, tan, cos, radians

ang = float(input('Digite o ângulo que vocÊ deseja : '))

# tem que transformar em radianos
print(f'''
Seno de {ang} = {sin(radians(ang)):.2f}
Cosseno de {ang} = {cos(radians(ang)):.2f}
Tangente de {ang} = {tan(radians(ang)):.2f}''')