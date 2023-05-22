nome = input('Nome: ')
idade = int(input('idade: '))

if nome and idade:
    print(f'Seu nome é {nome} é sua idade é {idade}, seu nome tem {len(nome)} caracteres, a primeira letra do seu nome é {nome[0]} e a ultima é {nome[-1]}')

