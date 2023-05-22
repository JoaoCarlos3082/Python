'''Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".'''


pergunta = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]

cont = 0
cont_resposta = 0
while True:
    if cont < len(pergunta):
        print(pergunta[cont])
        resposta = input('Sim ou Não: ')[0].strip()
        if resposta in 'Ss':
            cont += 1
            cont_resposta += 1
            continue

        elif resposta in 'Nn':
            cont += 1
            continue

        else:
            print('Responda a pergunta com sim ou não')
    else:
        break

print(cont_resposta)

if cont_resposta < 2:
    print('Inocente')

elif cont_resposta == 2:
    print('Suspeita')

elif cont_resposta == 3 or cont_resposta == 4:
    print('Complice') 

elif cont_resposta == 5:
    print('Assasino')  

    
