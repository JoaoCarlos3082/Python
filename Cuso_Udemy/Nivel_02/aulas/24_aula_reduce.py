# reduce - faz a redução de um iterável em um valor
from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]


# def funcao_do_reduce(acumulador, produto):
#     print('acumulador', acumulador)
#     print('produto', produto)
#     print()
#     return acumulador + produto['preco']

# reduce
total = reduce(
    lambda acumulador, produto: acumulador + produto['preco'],
    produtos,
    0
)

print('Total é', total)

# primeiroa forma de fazer com 'codigo'

# total = 0
# for p in produtos:
#     total += p['preco']

# print(total)

# segunda forma de fezer com 'sum'

# print(sum([p['preco'] for p in produtos]))