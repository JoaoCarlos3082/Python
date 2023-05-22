# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

lista = []
lista_reserva = []


while True:

    print('Comandos: Listar, Desfazer, Refazer')
    acao = input('Digite um "Comando" ou uma "Tarefa": ').upper()
    lista.append(acao)  
    


    #check da ação
    if acao == 'LISTAR':
        lista.remove('LISTAR')
        if len(lista) == 0: #check da lista
            print('Não tem nada para listar')

        else:    
            for i in lista:
                print(i)
        

    elif acao == 'DESFAZER':
        lista.remove('DESFAZER')
        if len(lista) == 0: #check da lista
            print('Não tem nada para Desfazer')
        
        else:
            lista_reserva.append(lista[-1]) # pegando o utimo elemento da lista ante de remover ele
            lista.pop()# removendo o utimo elemento da listar
            for i in lista:
                print(i)


    elif acao == 'REFAZER': 
        lista.remove('REFAZER')
        if len(lista) == 0: #check da lista
            print('Não tem nada para Refazer')
        
        else:
            lista.append(lista_reserva[-1]) # pegando o utimo elmento da lista
            lista_reserva.pop() # e retirando o utimo elemento da lista reserva
            for i in lista:
                print(i)
