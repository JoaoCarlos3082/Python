nome = input('Qual o seu nome: ')

if len(nome) <=4:
    print(f'Seu nome {nome} é curto.')

elif len(nome) <=6:
    print(f'Seu nome {nome} tem um tamanho normal.')

else:
    print(f'Seu nome {nome} é longo')