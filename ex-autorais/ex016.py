#  Programa 16 - Conversor de Temperatura

print("-" * 20)
print("Conversor Temperatura")
print("-" * 20)

# variáveis + conversão com operações
graus_c = float(input("\nInforme a temperatura atual (em Celsius) : "))
graus_f = (graus_c * 1.8) + 32
graus_k = graus_c + 273

# impressão resultado
print("-" * 20)
print(f"""\nGRAUS CELSIUS : {graus_c}°
GRAUS FAHRENHEIT : {graus_f}°
GRAUS KELVIN : {graus_k}°\n""")
print("-" * 20)