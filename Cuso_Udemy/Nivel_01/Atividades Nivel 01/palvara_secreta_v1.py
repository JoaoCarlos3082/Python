
palavra_secreta = 'RATATA'

letras_certas = ''

tentativas = 0

while True:
    letra = input('Digite uma letra: ').upper()
    tentativas += 1

    if len(letra) > 1:
        print('Digite apenas uma letra.')
        continue
    
    if letra in palavra_secreta:
        letras_certas += letra

    palavra_correta = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_certas:
            #print(f' A letra digitada "{letra}" esta na palavra secreta.')
            print(letra_secreta)
            palavra_correta += letra_secreta

        else:
            print('*')

    if palavra_correta == palavra_secreta:
        break        


print(f'Parabens!, numero de tentativas {tentativas}')
 


