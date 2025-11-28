# PROJETO FINAL PYTHON ESSENTIALS 1
# JOGO DA VELHA COM RESPOSTAS RANDOMIZADAS DA MÁQUINA

import time
import random
import os

# função para exibir tabuleiro
def mostrartab(board):
    for linha in range(3):
        print() # pula uma linha para cada linha da matriz
        for colunas in range(3):
            print(f"[  {str(board[linha][colunas])}  ]",end=' ')

# função que verifica casas livres
def vazio(board):
    tablivre = []
    for linha in range(3):
        for colunas in range(3):
            valor = board[linha][colunas]
            if valor != 'X' and valor != 'O': # se não tiver 'X' ou 'O'
                tablivre.append(valor) # adiciona à lista dos livres
    return tablivre

# função que verifica as vitórias
def verificar_vitoria(simbolo, board):
    for linha in board:
        if linha.count(simbolo) == 3: # se tiver o mesmo símbolo nas linhas
            return True
        
    for col in range(3): # se tiver o mesmo símbolo nas colunas
        if board[0][col] == simbolo and board[1][col] == simbolo and board[2][col] == simbolo:
            return True
        
    # se tiver os mesmos símbolos nas diagonais
    if board[0][0] == simbolo and board[1][1] == simbolo and board[2][2] == simbolo:
        return True
    if board[0][2] == simbolo and board[1][1] == simbolo and board[2][0] == simbolo:
        return True
    
    return False

# atualização do tabuleiro
def atualizartab(board, numero, simbolo):
    num_ajustado = numero - 1 # se selecionado 5, fica 5-1
    linha = num_ajustado // 3 # número da linha
    coluna = num_ajustado % 3 # numero da coluna
    board[linha][coluna] = simbolo # atribui o símbolo à linha e coluna

# --------- início do programa ----------
# inicia o tabuleiro
tabuleiro = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
rodada = 0

print("\nBem vindo! Usuário 'O' e máquina 'X'.")

while True:
    time.sleep(2)
    os.system('cls')
    mostrartab(tabuleiro)
    livres = vazio(tabuleiro)

    # verifica inicialmente se há casas livres
    if not livres:
        print("\nDeu velha! Empate.")
        break

    # resposta do usuario
    try:
        resp_jogador = int(input(f"\nSua vez ('O'). Escolha {livres} : "))
        if resp_jogador in livres: # se a escolha tiver livre
            atualizartab(tabuleiro, resp_jogador, 'O') # atualiza o tabuleiro
            if verificar_vitoria('O', tabuleiro): # e verifica condições de vitoria
                mostrartab(tabuleiro)
                print("\nVocê venceu!! Parabéns.")
                break
            rodada += 1

        else: # se a escolha já estiver ocupada
            print("\nPosição inválida. Por favor, selecione outra.")
            continue

    except ValueError: # caso haja erro no valor selecionado
        print("\nPfv, digite um número válido.")
        continue

    # resposta do computador
    # atualiza as posições livres antes de jogar
    livres = vazio(tabuleiro)
    if not livres: # se estiver tudo ocupado, volta para o inicio e registra empate
        continue

    print("Computador pensando...")
    time.sleep(1)

    # escolhe uma opção entre as casas vazias
    jogada_pc = random.choice(livres)
    atualizartab(tabuleiro, jogada_pc, 'X') # atualiza tabuleiro
    if verificar_vitoria('X', tabuleiro): # verifica condições de vitória
        mostrartab(tabuleiro)
        print('\nQue pena! O computador venceu.')