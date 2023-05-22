
compras = []
opc_valido = 'IRL'


while True:
    opc = input('[I]nserir | [R]emover | [L]star: ').upper()

    try:
        pergunta = str(opc)

    except:
        print('Erro na opeção.')
        continue

    if pergunta in opc_valido:
        
        if pergunta == 'I':
            valor_da_lista = input('Carrinho: ')
            compras.append(valor_da_lista)
            if valor_da_lista == '':
                print('Não foi colocado nada no carrinho')
                compras.pop()
               
        if pergunta == 'R':
            if len(compras) > 0:
                deletar = input('Qual o indice que você quer deletar: ')
                try:
                    deletar_int = int(deletar)  
                    print(f'O Item "{compras[deletar_int]}",no indice "{deletar_int}" foi removido.')  
                    del compras[deletar_int] 

                except:
                    print('Erro no indice!, colocar um indice valido')    
            else:
                print('Não há nadar a o qué remover no carrinho.')        

        if pergunta == 'L':
            if len(compras) > 0:
                for item in enumerate(compras):
                    indice, nome = item
                    print(indice,'-', nome)
            else:
                print('Não há nada no carrinho de compras.')            

    elif len(pergunta) > 1:
        print('Digite apenas uma opeção')
    else:
        print('Essa opeção não é valida.')
        continue

   

