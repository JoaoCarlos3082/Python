# isinstace - paara saber se objeto é de determinado tipo

lista = [1, 2, 3, 1.2, 1.3, 1.4, 'a', 'b', 'c', [2, 3, 2], (5, 2, 4), {0, 2}, {'nome':'jao'}]
'''
for i in lista:
    print(i, isinstance(i, str))# mostrando os items e seus tipos. EX: int, float, str, list, tuple, dict, etc...
'''

for i in lista:
    if isinstance(i, str):
        print('Todos os tipos STR:', i)

    elif isinstance(i, int):
        print('Todos os tipos INT:', i)

    elif isinstance(i, float):
        print('Todos os tipos FLOAT: ', i)    
