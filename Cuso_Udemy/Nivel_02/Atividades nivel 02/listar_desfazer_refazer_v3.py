import json

def desfazer(lista, lista_reserva):
    print()
    if not lista: # lista vazia e false
        print('Não a nada para desfazer')    
        return # para a execução
 
    lista_reserva.append(lista[-1]) #pegando o valor que sera excluido e jogando na lista_resva
    lista.pop() #removendo o ultumo valor da lista
    print()

def listar(lista):
    print()
    if not lista: # lista vazia e false
        print('Não a nada para listar')
        return # para a execução
    
    for i in lista: #mostrando todos os valores da lista
        print(i)
    print()    

def refazer(lista, lista_reserva):
    print()
    if not lista_reserva: # lista vazia e false
        print('Não a nada para refazer')
        return # para a execução
    
    lista.append(lista_reserva[-1]) #pegando o ultimo valor excluido e colando novamente na lista
    lista_reserva.pop() #removendo o valor que foi colocado na lista
    print()

def ler(lista, caminho_arquivo):
    dados = [] 
    try: # tentar ler o arquivo
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError: # caso ocorra o erro do arquivo no existir, criar ele
        print('Arquivo não existe')
        salvar(lista, caminho_arquivo)
    return dados

def salvar(lista, caminho_arquivo):
    dados = lista
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(lista, arquivo, indent=2, ensure_ascii=False) # salvando os valores no arquvi json
    return dados 

caminho_arquivo = "c:/Users/cliente/Desktop/CODE/python/CURSO_PYTHON/Nivel 02/Atividades nivel 02/listar_desfazer_refazer_v3.json"
lista = ler([], caminho_arquivo)
lista_reserva = []


while True:

    print('Comandos: Listar, Desfazer, Refazer')
    acao = input('Digite um "Comando" ou uma "Tarefa": ').upper().strip() # colcando todo em maisculo e tirando os spassos
    lista.append(acao)
     

    #check da ação
    if acao == 'LISTAR':
        lista.remove('LISTAR')
        listar(lista)
        continue

    elif acao == 'DESFAZER':
        lista.remove('DESFAZER')
        desfazer(lista, lista_reserva)
        listar(lista)
        salvar(lista, caminho_arquivo)
        
        continue


    elif acao == 'REFAZER': 
        lista.remove('REFAZER')
        refazer(lista, lista_reserva)
        listar(lista)
        salvar(lista, caminho_arquivo)
        
        continue

    salvar(lista, caminho_arquivo) 
