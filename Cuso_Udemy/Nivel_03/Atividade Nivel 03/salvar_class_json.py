# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json

caminho_arquivo = "c:/Users/cliente/Desktop/CODE/python/CURSO_PYTHON/Nivel_03/Atividade Nivel 02/salvar_class_json.json"

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Carlos', 19)
p2 = Pessoa('Maria', 21)
p3 = Pessoa('Carla', 15)

dado = [vars(p1), vars(p2), vars(p3)] # pegando a lista com os valores da class

# crinado uma função para adiar a execução.
def fazer_dump():
    with open(caminho_arquivo, 'w') as arquivo:
        json.dump(dado, arquivo, ensure_ascii=False, indent=2)

# if para que o dump so ocorra no main
if __name__ == '__main__':
    fazer_dump()        