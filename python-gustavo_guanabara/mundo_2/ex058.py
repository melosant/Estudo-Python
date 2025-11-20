# rework do exercício 28 com while
from random import randint

numero_secreto = randint(0, 10)
tentativas = 0

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print(' Vou pensar em um número entre 0 e 10')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

chute = int(input('Informe qual seu chute : '))
tentativas += 1
while chute != numero_secreto:
    print("Errou, bobão. Tenta dnv ai!")
    chute = int(input('Informe novamente qual seu chute : '))
    tentativas += 1

print(f"Você enfim acertou. O número era {numero_secreto} e precisou de {tentativas} tentativas.")