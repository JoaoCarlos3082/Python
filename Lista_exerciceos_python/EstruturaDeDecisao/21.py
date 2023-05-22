#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

saque = 376

if saque < 10 or saque > 600:
    print("Valor de saque inválido!")
else:
    notas100 = saque // 100
    saque = saque % 100

    notas50 = saque // 50
    saque = saque % 50

    notas10 = saque // 10
    saque = saque % 10

    notas5 = saque // 5
    saque = saque % 5

    notas1 = saque // 1

    print("Notas de 100 reais:", notas100)
    print("Notas de 50 reais:", notas50)
    print("Notas de 10 reais:", notas10)
    print("Notas de 5 reais:", notas5)
    print("Notas de 1 real:", notas1)