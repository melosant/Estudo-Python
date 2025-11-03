# Conversor de segundos

print("+", "-" * 18, "+")
print("CONVERSOR DE SEGUNDOS")
print("+", "-" * 18, "+")
# Variáveis
total_seg = int(input("\nDigite a quantidade total de segundos : ")) # segundos totais
horas = total_seg // 3600 # 1 hora = 3600s (divisão inteira)
resto = total_seg % 3600 # segundos restantes depois das horas
min = resto // 60 # 1 minuto = 60s (divisão inteira)
seg = resto % 60 # segundos restantes.

# impessão pós conversão.
print(f"\n{horas} horas(h), {min} minutos(min) e  {seg} segundos(s).")