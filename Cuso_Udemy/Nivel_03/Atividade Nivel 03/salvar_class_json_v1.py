import json

from salvar_class_json import Pessoa, caminho_arquivo

with open(caminho_arquivo, 'r') as arquivo:
    #carregando os aquivos
    pessoas = json.load(arquivo)

    #expandinod a lista de pessoas e pagando seus indices
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])

    print(p1.nome, p1.idade)
    print(p2.nome, p2.idade)
    print(p3.nome, p3.idade)