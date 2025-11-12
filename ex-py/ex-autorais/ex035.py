# Programa 35 - Registro Notas de Alunos (Cisco)
# utilizando dicionários e tuplas
# atribui uma tupla como valor de uma chave no dicionário

classe = {}

while True:
    nome = input("Digite o nome do aluno (ou deixe em branco para parar) : ")
    if nome == "":
        break
    nota = float(input('Digite a nota do aluno : '))
    if nota < 0 or nota > 10:
        break

    if nome in classe:
        classe[nome] += (nota, )
    else:
        classe[nome] = (nota, )

    for nome in sorted(classe.keys()):
        soma = 0
        cont = 0
        
        for nota in classe[nome]:
            soma += nota
            cont += 1

        print(f'{nome} : {soma / cont}')

print('\nPROGRAMA FINALIZADO.')