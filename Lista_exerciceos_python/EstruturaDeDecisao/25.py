#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"""
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""

def if_verif(pergunta, classifc):
    if pergunta in 'Ss':
        classifc += 1

    elif pergunta in 'Nn':
        pass
     
    else:
        print('Digite sim[s] ou não[n]') 

    return classifc

classifc = 0

while True:
    pg1 = input("Telefonou para a vítima? [s ou n] ")[0].strip()
    classifc = if_verif(pg1, classifc) 

    pg2 = input("Esteve no local do crime? [s ou n] ")[0].strip()
    classifc = if_verif(pg2, classifc)

    pg3 = input("Mora perto da vítima? [s ou n] ")[0].strip()
    classifc = if_verif(pg3, classifc)

    pg4 = input("Devia para a vítima? [s ou n] ")[0].strip()
    classifc = if_verif(pg4, classifc)

    pg5 = input("Já trabalhou com a vítima? [s ou n] ")[0].strip()
    classifc = if_verif(pg5, classifc)


    if classifc >=5:
        print('Assasino.')
        break

    elif classifc >=3:
        print('Cúmplice.') 
        break   

    elif classifc >= 2:
        print('Suspeiro')
        break

    else:
        print('Inocente')
        break    


print(classifc)    