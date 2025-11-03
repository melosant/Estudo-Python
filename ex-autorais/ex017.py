# Programa 17 - Contador de Vogais

# entrada da palavra
word = input("Digite uma palavra: ")
word = word.upper() # armazena a palavra em maiúsculo na variável
vogais = 0

for letter in word: # laço de repetição vai passar por cada letra na palavra
    # estrutura condicional, se tiver vogal, soma na variável.
    if letter == "A":
        vogais += 1
    elif letter == "E":
        vogais += 1
    elif letter == "I":
        vogais += 1
    elif letter == "O":
        vogais += 1
    elif letter == "U":
        vogais += 1
# impressão do resultado
print(f"A palavra {word}, contém {vogais} vogais!")