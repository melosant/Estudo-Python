# Perguntas e Respostas
# Aula 126
acertos = 0

perguntas = [
    {
    'Pergunta' : 'Quanto é 2 + 2?',
    'Opções' : ['1', '3', '4', '5'],
    'Resposta' : '4',
},
    {
    'Pergunta' : 'Quanto é 5 * 5?',
    'Opções' : ['0', '20', '15', '25'],
    'Resposta' : '25',
},
    {
    'Pergunta' : 'Quanto é 10 / 2?',
    'Opções' : ['5', '20', '2', '10'],
    'Resposta' : '5',
}] 

for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    for i, opcao in enumerate(pergunta['Opções']):
        print(f'{i}) {opcao}')
        
    while True:
        try:
            escolha = int(input('Escolha sua opção: '))
            break
        except:
            print('Escolha uma opção válida.')
            continue

    if pergunta['Opções'][int(escolha)] == pergunta['Resposta']:
        acertos += 1
        print('Acertou!\n')

print(f'Você acertou {acertos} de 3 respostas.')