# programa 8 : conversão em metros
# Operadores Aritméticos (Aula 7)

distancia = float(input('Digite a distância em metros (m): '))
cm = distancia * 100
mm = distancia * 1000

print(f'A medida de {distancia}m, corresponde a {cm:.1f}cm e {mm:.1f}mm.')