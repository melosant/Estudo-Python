# Programa 106 : Interactive Help
# Funções / Escopo de Variáveis (Aula 21)
def interactive(fun):
    print('\033[1;97m\033[1;44m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f"Acessando manual do comando '{fun}'")
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0;0m')
    print(f'{help(fun)}')


while True:
    print('\033[1;41m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('SISTEMA DE AJUDA PYHELP')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0;0m')

    comando = input('Função ou Biblioteca > ').lower()
    if comando == "fim":
        break

    interactive(comando)

print('\033[1;31mPrograma Finalizado!\033[0;0m')