# Programa 23 - Verificador de Senha

print("=" * 30)
print("VERIFICADOR DE SENHA")
print("""
A SENHA DEVE CONTER :
- 8 CARACTERES
- NÚMERO
- LETRA MAIÚSCULA""")
print("=" * 30)
print()

validacao = False # variável de verificação

while validacao != True: # enquanto a condição não for válida, continua loop

    senha = input("Digite uma senha : ") # emtrada da senha
    # variáveis de verificação começam em False
    tem_numero = False
    tem_letra = False
    tem_maiusc = False
    
    for i in senha: # loop que passa por cada dígito da senha
        if i.isdigit(): # função que verifica se o dígito é um número (0-9)
            tem_numero = True
        if i.isalpha(): # função que verifica se o dígito é uma letra (a-z)
            tem_letra = True
        if i.isupper(): # função que verifica se o dígito é uma letra maiúscula
            tem_maiusc = True
        
        # se todas as condições forem atendidas, fim do loop.
    if tem_letra == True and tem_maiusc == True and tem_numero == True:
        validacao = True
        break

    else: # se não...
        if len(senha) < 8: # menos de 8 caracteres
            print("A senha deve ter pelo menos 8 caracteres.")
        elif tem_numero == False: # condição tem_numero não atendida
            print("A senha deve conter pelo menos um número.")
        elif tem_letra == False: # condição tem_letra não atendida
            print("A senha deve conter pelo menos uma letra.")
        elif tem_maiusc == False: # condição tem_maiusc não atendida
            print("A senha deve conter pelo menos uma letra maiúscula.")

print("Senha Válida!") # fim do programa.