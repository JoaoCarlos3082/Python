import os

caminho_completo = 'C:\\Users\\cliente\\Desktop\\CODE\\python\\CURSO_PYTHON\\Nivel 02\\manipulacao_de_arquivos\\'
caminho_completo += '27_aula_arquivos_v2.txt'

with open(caminho_completo, 'w') as arquivo: # Caracteres especiais 
    arquivo.write('Atenção\n')
    arquivo.write('Jão\n')
    arquivo.write('çççççç^^^^\n')

with open(caminho_completo, 'a', encoding='utf8') as arquivo: # colocando em utf 8 para nao ter erro de caracteres especiais
    arquivo.write('Atenção\n')
    arquivo.write('Jão\n')
    arquivo.write('çççççç^^^^\n')    

# remove o arquivo

#os.remove(caminho_completo)
#os.unlink(caminho_completo)    