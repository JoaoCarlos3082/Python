# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

'''
cont = 0
contop1 = 0
while True:
    print(perguntas[cont]['Pergunta'])
    for i in range(4):
        if contop1 > 3:
            opc = int(input('Opc: '))
            break
        else:
            print(f"{contop1}) {perguntas[cont]['Opções'][contop1]}")
            contop1 += 1        
            
    cont += 1

    if cont >=3:
        break
'''


qtd_acerto = 0

for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opecao in enumerate(opcoes):
        print(f'{i}) {opecao}')

    opc_escolhida = input('Opeção: ')

    acerto = False
    opc_int = None
    qtd_opecao = len(opcoes)

    if opc_escolhida.isdigit():
        opc_int = int(opc_escolhida)

    if opc_int is not None:
        if opc_int < qtd_opecao:
            if opcoes[opc_int] == pergunta['Resposta']:
                acerto = True           
                
    if acerto is True:
        print('Acerto') 
        qtd_acerto += 1

    else:
        print('Errou')

print(f'você acertou {qtd_acerto}/{len(perguntas)}')       
