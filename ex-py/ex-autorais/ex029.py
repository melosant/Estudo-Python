# Programa 29 - Gerenciador de Estoque
import time # biblioteca para controle do tempo
import os # biblioteca para limpar terminal windows

# declaração de variáveis
estoque = []
produto = ""

print("=" * 22)
print("GERENCIADOR DE ESTOQUE")
print("=" * 22)

while True: # loop infinito
    time.sleep(3.0) # 3seg para cada volta do loop 
    os.system('cls') # comando para limpar terminal

    print("""
O que deseja fazer :
1 - Adicionar Produto
2 - Remover Produto
3 - Listar Produtos
4 - Sair""")
    resposta = int(input("\nDIGITE A OPÇÃO (1-4) : ")) # entrada da opção

    if resposta == 1:
        produto = input("\nDigite o nome do produto : ") # entrada nome do produto
        estoque.append(produto) # adiciona produto à lista estoque
        print("\nProduto Adicionado!")
    elif resposta == 2:
        if not estoque: # se lista estiver vazia, imprime mensagem de erro ao remover.
            print("\nNão é possível remover! Nenhum produto adicionado.")
        else: # se tiver itens
            print(f"\n PRODUTOS EM ESTOQUE : {estoque}")
            delete = (input("\nDigite o nome do produto que deseja deletar : ")) # entrada nome produto para remover
            estoque.remove(delete) # função que aceita strings para remover elementos de uma lista
            print(f'\nProduto "{delete}" Removido!')
    elif resposta == 3:
        if not estoque:
            print("\nNenhum item adicionado ao estoque!") # se não tiver itens adicionados
        else:
            print("\nESTOQUE ATUAL :", estoque) # impressão da lista estoque
    elif resposta == 4 :
        break # sai do loop
    else:
        print("\nDigite uma opção válida!")

print("\nPrograma Finalizado!\n")