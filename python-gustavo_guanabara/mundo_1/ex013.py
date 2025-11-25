# programa 13 : aplicando aumento de 15% num salario que o usuário informa
# Operadores Aritméticos (Aula 7)

salario = float(input('Digite o salario do funcionario : R$'))
aumento = salario * 1.15
# aumento = salario + (salario * 15/100)

print(f'O salário do funcionario era R${salario}, com o aumento de 15% da empresa, o seu novo salário é de R${aumento:.2f}.')