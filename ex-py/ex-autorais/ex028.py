# Programa 28 - Números Secretos em Lista
import random

# declaração variáveis
lista_secreta = [] 

for i in range(3): # loop para adição de 3 números aleatórios na lista
    numeros = random.randint(1, 20)
    lista_secreta.append(numeros)

print("=" * 20)
print("Advinhe o Número Secreto")
print("=" * 20)

while True: # loop principal 
    chute = int(input("Digite seu palpite : ")) # entrada do chute
    if chute in lista_secreta: # se estiver presente na lista
        posicao = lista_secreta.index(chute) # função para descobrir a posição na lista
        print(f"\nVocê Acertou! O número {chute} estava presente na lista na posição {posicao}.") # impressão do acerto
        break # acerto = fim do loop
    else: # se não
        print(f"\nO número {chute} não está na lista!\n") # impressão do erro

print(f"\nLista Final : {lista_secreta}") # impressão lista final