# Programa 8 - Contador de Números Positivos e Negativos

positivos = 0
negativos = 0
zeros = 0
i = 1 # contador do while

print("+-------------------------+")
print("| POSITIVOS OUU NEGATIVOS |")
print("+-------------------------+\n")

# ------------------------- USANDO FOR

# for i in range(1, 11):
#     num = int(input(f"Digite o {i}° número: "))
#     if num > 0:
#         positivos += 1
#     elif num < 0:
#         negativos += 1
#     else:
#         zeros += 1

# ------------------------- USANDO WHILE

# loop principal para dígito de 10 números
while i < 11:
    num = int(input(f"Digite o {i}° número: "))
    i += 1
    # estrutura condicional para verificação positivos, negativos e zeros
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    else:
        zeros += 1

# impressão do resultado
print()
print(f"TOTAL DE POSITIVOS: {positivos}")
print(f"TOTAL DE NEGATIVOS: {negativos}")
print(f"TOTAL DE ZEROS: {zeros}")