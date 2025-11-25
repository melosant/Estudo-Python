# programa 11 : é usado 1l de tinta para 2m de area
# Operadores Aritméticos (Aula 7)

larg = float(input('Digite a largura da parede : '))
alt = float(input('Digite a altura da parede : '))
area = larg * alt
print(f'Sua parede tem dimensão {larg}x{alt} e tem área igual a {area:.2f}m²')
tinta = area / 2
print(f'Será necessário {tinta:.2f}l de tinta.')