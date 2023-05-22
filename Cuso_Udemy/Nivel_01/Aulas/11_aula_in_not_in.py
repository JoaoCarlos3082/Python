# 'IN' (entre) 'NOT IN' (não entre)

'''
nome = 'Carlos'

print('a' in nome)
print('v' in nome)
print('-'*10)
print('v' not in nome)
print('a' not in nome)

'''

palavra = input('Palavra: ')

encontrar = input('O quer deseja procurar: ')

if encontrar in palavra:
    print(f'{encontrar} esta em {palavra}.')

else:
    print(f'{encontrar} não esta em {palavra}')    