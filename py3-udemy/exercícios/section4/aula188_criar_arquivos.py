import os

# para abrir um arquivo
caminho = 'C:\\Users\\natha.santos\\Documents\\ESTUDO\\Estudo-Python\\py3-udemy\\exercícios\\section4\\criar_arquivo_188.txt'
# arquivo = open(caminho, 'w')
# arquivo.close()

# with é context manager, ele abre e automaticamente já fecha o arquivo
with open(caminho, 'w+') as arquivo:
    '''
    'w+' - habilita escrita e leitura, sobrescrevendo caso já exista

    seek - move o cursor
    writelines - escreve linhas por meio de um iterável
    readline - lê linhas uma a uma
    readlines - é capaz de ler mais de uma linha 
    '''
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')   
    arquivo.writelines(('Linha 3\n', 'Linha 4'))
    arquivo.seek(0, 0)
    print(arquivo.read()) 

    arquivo.seek(0, 0)
    print('\nLendo...')
    print(arquivo.readline(), end='')
    print(arquivo.readline())
    
    arquivo.seek(0, 0)
    print('\nReadlines...')
    for linha in arquivo.readlines():
        print(linha.strip())

with open(caminho, 'a+', encoding='UTF-8') as arquivo:
    arquivo.write('\nAtenção\n')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')   
    arquivo.writelines(('Linha 3\n', 'Linha 4'))

# unlink e rmeove são para remover o arquivo, rename para renomear
# os.unlink(caminho)
# os.remove(caminho)
# os.rename(caminho, 'aula188.txt')