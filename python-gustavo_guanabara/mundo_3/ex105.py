# Programa 105 : Notas em funções
# Funções / Escopo de Variáveis (Aula 21)

def notas(*n, sit=False):
    '''
    *n - numero de notas que serão passadas (tupla)
    sit=False - se for True, verifica a situação do aluno
    '''
    boletim = dict()
    media = 0

    for i in n:
        media += i
        
    media = media / len(n)

    boletim['Total'] = len(n)
    boletim['Maior Nota'] = max(n)
    boletim['Menor Nota'] = min(n)
    boletim['Média'] = media
    if sit == True:
        if media > 7.0:
            boletim['Situação'] = 'BOA'
        elif media >= 6.0 and media < 7.0:
            boletim['Situação'] = 'RAZOÁVEL'
        else:
            boletim['Situação'] = 'RUIM'

    return boletim
 
resp = notas(2.5, 9.5, 4.5, 6.5)
print('-' * 70)
print(resp)