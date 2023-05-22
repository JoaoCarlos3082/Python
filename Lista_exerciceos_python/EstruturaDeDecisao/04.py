# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input('Letra: ')[0].strip().lower()

if letra in 'aioueAIOUE':
    print('Vogal')

else:
    print('Consoante')
