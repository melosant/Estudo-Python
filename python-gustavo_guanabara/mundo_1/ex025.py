# programa 25 : verifica se tem SILVA no nome completo informado
# Manipulando Strings (Aula 9)

nome = input('Digite seu nome completo : ').upper().split()
print(f'Seu nome tem Silva ? {'SILVA' in nome}')