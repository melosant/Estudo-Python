# Programa 103 : ficha de jogador
# Funções / Escopo de Variáveis (Aula 21)

def ficha(name, goals):
    print(f'O jogador {name} fez {goals} gol(s) no campeonato.')
    
nome = input('Digite o nome do jogador : ')
if nome == '':
    nome = '<desconhecido>'
gols = input('Digite o número de gols : ')
if gols == '':
    gols = '0'
ficha(nome, int(gols))