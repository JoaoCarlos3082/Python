# Métodos úteis dos dicionários em Python
# len - quantas chaves (obs: ter mais uma chave como o mesmo nome, so ira contar a ultima)
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
#        OBS: para uma copia profunda usar >>> import copy >> .deepcopy
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    'nome': 'Carlos Vieira',
    'sobrenome': 'Santos',
    'idade': 22,
    'altura': 1.8,
    'endereços': [
        {'rua': '10', 'número': 13},
        {'rua': 'Sabia', 'número': 31},
    ],
}


pessoa.update({'nome' : 'matheus'})

print(pessoa)