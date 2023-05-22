# filter é um filtro funcional
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

pro = [
    {'nome': 'Produto 5', 'preco': 20.00},
    {'nome': 'Produto 1', 'preco': 30.32},
    {'nome': 'Produto 3', 'preco': 40.11},
    {'nome': 'Produto 2', 'preco': 195.87},
    {'nome': 'Produto 4', 'preco': 690.90},
]


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


def filtrar_preco(produto):#criar o filtro, no caso para valores asima de 40
    return produto['preco'] > 40


# novos_produtos = [ # filter em codigo
#     p for p in produtos
#     if p['preco'] > 100
# ]
novos_produtos = filter( # função filter do python
    lambda produto: produto['preco'] > 40, # mesma função que 'filtrar_preco' so que em lambda
    produtos# a lista de produtos 
)

novos_produtos2 = filter(
    lambda produto: produto['preco'] > 40, 
    pro
)

print_iter(produtos)
print_iter(novos_produtos)
print_iter(novos_produtos2)