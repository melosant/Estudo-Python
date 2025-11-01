# Programa 12 - Advinhe Número Aleatório

import random # biblioteca que gera números e faz escolhas aleatorias
num_sec = random.randint(1,20) # função que escolher um número aleatorio entre o conjunto
user = "" # string vazia

# loop principal para acerto de número aleatório
while num_sec:
    user =  int(input("Digite o número certo: "))
    if user < num_sec: # se for menor imprime a seguinte mensagem
        print(f"O número certo é maior do que {user}")
    elif user > num_sec: # se for maior imprime a seguinte mensagem
        print(f"O número certo é menor do que {user}")
    else: # se for igual, quebra o loop
        break

# imprime mensagem de acerto
print(f"""\nO número secreto era {num_sec}
Parabéns, você acertou o número secreto!!""")