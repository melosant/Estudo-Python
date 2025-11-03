# Programa 15 - Cadastro Simples

# declaração de variáveis
total = 0
mais_velha_nome = ""
mais_velha_idade = 0
soma = 0
media = 0
cadastro = ""

# loop infinito
while True:
    # entradas de nome e idade
    cadastro = input("Digite o nome da pessoa : ")
    idade = int(input("Digite sua idade : "))

    # adiciona 1 ao total de pessoas e à idade na variável soma (a cada volta do loop)
    total += 1
    soma += idade

    # condicional para guardar nome da pessoa mais velha
    if idade > mais_velha_idade:
        mais_velha_nome = cadastro
        mais_velha_idade = idade

    continuar = input('Deseja cadastrar outra pessoa ? (S/N) ') # pergunta de confirmação para repetição
    if continuar.upper() == 'N': # função para deixar a entrada em maiúsculo
        break # se o usuário digitar 'N' ou 'n' quebra o loop

media = soma / total # media das idades (soma das idades totais dividido pelo total de pessoas)
# imprime total de pessoas, média das idades formatadas e nome da pessoa mais velha
print(f"""TOTAL DE PESSOAS CADASTRADAS : {total}
MÉDIA DAS IDADES : {media:.2f}
NOME DA PESSOA MAIS VELHA : {mais_velha_nome}""")