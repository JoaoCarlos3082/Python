# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

# unsado duas barras invertidas para não dar prbolema com windwos
caminho_completo = 'C:\\Users\\cliente\\Desktop\\CODE\\python\\CURSO_PYTHON\\Nivel 02\\manipulacao_de_arquivos\\'
caminho_completo += '26_aula_arquivos.txt' # caminho na pasta
caminho = '26_aula_arquivos.txt' # caminho na raiz


'''
# abrir e fechar arquivo

arquivo = open(caminho_completo, 'w')

arquivo.close()
'''

# withc oper => abre e fecha o arquivo
with open(caminho_completo, 'w+') as arquivo: # w+ => escrve e ler 
    arquivo.write('linha 01\n') # escrita
    arquivo.write('linha 02\n')
    arquivo.writelines(
        ('linha 03\n', 'linha 04\n', 'linha 05\n') # writelines (escrever várias linhas)
    )
    arquivo.seek(0, 0)
    print(arquivo.read())  #ler o arquivo todo

print()
print('---'*10)
print()

with open(caminho_completo, 'r') as arquivo: # r => apenas ler o arquivo
    print(arquivo.read())    #ler o arquivo todo

print()
print('---'*10)
print()

with open(caminho_completo, 'r') as arquivo: 
    print(arquivo.readline()) # readline => ler linha por linha
    print(arquivo.readline())  
    print(arquivo.readline(), end='') # remover os spasos feita pela quebra de linha metodo 01  
    print(arquivo.readline().strip()) # remover os spasos feita pela quebra de linha metodo 02      
    
print()
print('---'*10)
print()

with open(caminho_completo, 'r') as arquivo:
    #print(arquivo.readlines()) # readlines => retorna uma lista de linhas
    for linha in arquivo.readlines(): 
        print(linha.strip()) 

with open(caminho_completo, 'w') as arquivo: # w apagar o arquivo e escreve
    arquivo.write('linha 11\n') 
    arquivo.write('linha 12\n')
    arquivo.writelines(
        ('linha 13\n', 'linha 14\n', 'linha 15\n') 
    )       

with open(caminho_completo, 'r') as arquivo: 
    print(arquivo.read())

with open(caminho_completo, 'a') as arquivo: # a ele escreve no final.
    arquivo.write('linha 16\n') 
    arquivo.write('linha 17\n')
    arquivo.writelines(
        ('linha 18\n', 'linha 19\n', 'linha 20\n') 
    )         

with open(caminho_completo, 'r') as arquivo: 
    print(arquivo.read())    