#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

vetor = []
consoante = []

while True:
    if len(vetor) > 10:
        break

    letra = input('Letra: ')[0].strip()
    vetor.append(letra)

    if letra in 'aeiou':
        consoante.append(letra)

print(f'Forma lidas {len(consoante)} consoantes.')
print(vetor)

