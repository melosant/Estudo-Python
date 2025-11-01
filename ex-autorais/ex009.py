# Programa 9 - Advinhe a Senha

senha = 'python' # senha correta
resposta = "" # string vazia
tentativa = 0

# loop principal para tentativas de senha
while senha:
    resposta = input("Digite a senha: ")
    tentativa += 1
    
    # se usuário digita a senha certa, quebra o loop
    # caso contrário, imprime uma mensagem de erro e continua o loop
    if resposta == senha:
        break
    else:
        print("Errou, bobão!")

print(f"Parabéns, conseguiu sair do loop! TENTATIVAS : {tentativa}")
