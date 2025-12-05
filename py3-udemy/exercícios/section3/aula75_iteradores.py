# como funciona o loop for. 
text = 'Flamengo Campeão'
iterador = iter(text) # ou text.__iter__()

# for letra in text:
#     print(letra, end='')


while True:
    try:
        letra = next(iterador)
        print(letra, end='')
    except StopIteration:
        break
