'''Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;

'''

numeros = []
media = 0
valors_acima_media = []
valores_abaixo_7 = []

while True:
    num = int(input('Numero: '))
    numeros.append(num)
    
    if num < 0:
        numeros.pop()
        break
    media = sum(numeros) / len(numeros)


print(f'Soma {sum(numeros)}')
print(f'Media {media}')

for c in range(len(numeros)):
    if numeros[c] > media:
        valors_acima_media.append(numeros[c])

print(f'Valores acima da media {media:.2f} são {valors_acima_media}')     

for c in range(len(numeros)):
    if numeros[c] < 7:
        valores_abaixo_7.append(numeros[c])

print(f'Valores abaixo de 7, {valores_abaixo_7}')        

