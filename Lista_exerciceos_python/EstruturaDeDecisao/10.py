#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input('Qual turno você estuda (Matutino, Vespertino, Noturno): ')[0].strip()

if turno in 'Mm':
    print('Bom Dia!')

elif turno in 'Vv':
    print('Boa Tarde!')

elif turno in 'Nn':
    print('Boa noite')

else:
    print('Invalido')    