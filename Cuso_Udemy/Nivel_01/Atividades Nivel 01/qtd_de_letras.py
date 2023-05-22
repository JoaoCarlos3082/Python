frase = 'Eu odeio trabalhar na OI, queria ser demitido logo mais não rola, foda!'

i = 0 
qtd_letra_mais_apareceu = 0
letra_que_mais_apareceu = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_letra_mais_apareceu_atual = frase.count(letra_atual)

    if qtd_letra_mais_apareceu < qtd_letra_mais_apareceu_atual:
        qtd_letra_mais_apareceu = qtd_letra_mais_apareceu_atual
        letra_que_mais_apareceu = letra_atual

    #print(f'{letra_atual} {frase.count(letra_atual)}')
    i += 1

print('A letra que mais apareceu foi: ',letra_que_mais_apareceu)
print('Apareceu X',qtd_letra_mais_apareceu)
