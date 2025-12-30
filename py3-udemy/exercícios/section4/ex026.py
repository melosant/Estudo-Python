# lista de tarefas
import os

tarefas = []
tarefas_desfeitas = []

while True:
    print('Comandos: Listar, Refazer, Desfazer.')
    resp = input('Digite uma tarefa ou comando: ').upper()

    if resp == 'LISTAR':
        if len(tarefas) == 0:
            print('\nNada a listar.\n')
        else:
            print('\nTAREFAS:\n')
            for i in tarefas:
                print(i)
            print()

    elif resp == 'DESFAZER':
        if len(tarefas) == 0:
            print('\nNada a desfazer.\n')
        else:
            tarefas_desfeitas.append(tarefas.pop())
            print('\nTAREFAS:\n')
            for i in tarefas:
                print(i)
            print()

    elif resp == 'REFAZER':
        if tarefas_desfeitas == 0:
            print('\nNada a refazer.\n')
        else:
            tarefas.insert(0, tarefas_desfeitas.pop(0))
            print('\nTAREFAS:\n')
            for i in tarefas:
                print(i)
            print()

    elif resp == 'CLEAR':
        os.system('cls')
        
    else:
        tarefas.append(resp)
        print('\nTAREFAS:\n')
        for i in tarefas:
            print(i)
        print()