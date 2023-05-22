# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

a = []
b = []
c = []

eleitores = int(input('Numero de eleitores: '))

print()
print('Candidato A, B ou C')

for i in range(eleitores):
    voto = input('Voto [A/B/C]: ')[0].upper()

    if voto == 'A':
        a.append(voto)

    elif voto == 'B':
        b.append(voto)

    elif voto == 'C':
        c.append(voto)

print(f'Os votos de cada candidato foi de A:{len(a)}, B:{len(b)}, C:{len(c)}')            
