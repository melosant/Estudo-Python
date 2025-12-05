# Analisador de CPF
# Aula 99-102

def calculodigitos(cont):
    soma = 0
    contador = cont
    for i in cpf_str:
        soma += int(i) * contador
        contador -= 1
    return soma

cpf_str = input('Digite os 9 primeiros dígitos do cpf : ')
if len(cpf_str) > 9 or len(cpf_str) < 9:
    print('Digite somente 9 dígitos.')
else:
    soma = calculodigitos(10)

    total = soma * 10
    p_digito = total % 11
    if p_digito > 9:
        p_digito = 0

    cpf_str = cpf_str + str(p_digito)

    soma = calculodigitos(11)

    total = soma * 10
    s_digito = total % 11
    if s_digito > 9:
        s_digito = 0

    cpf_str = cpf_str + str(s_digito)

    print(f'CPF COM OS DOIS DÍGITOS FINAIS : {cpf_str[:3]}.{cpf_str[3:6]}.{cpf_str[6:9]}-{cpf_str[9:11]}')
