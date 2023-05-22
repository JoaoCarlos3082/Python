#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# a - A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# b - A mensagem "Reprovado", se a média for menor do que sete;
# c - A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota_1 = float(input('Nota 01: '))
nota_2 = float(input('Nota 02: '))

media = (nota_1 + nota_2) / 2

if media >= 7:
    print('aprovado')

elif media == 10:
    print('Aprovado com Disitnção ')

else:
    print('Reprovado')    