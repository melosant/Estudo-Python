# Programa 1 - Comparação entre 2 números

# Solicita ao usuário que insira dois números inteiros
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
maior_num = ""

# Estrutura condicional para comparação dos números
if num1 > num2:
    maior_num = num1
else:
    maior_num = num2

# impressão do maior número
print(f"O maior número digitado foi : {maior_num}.")