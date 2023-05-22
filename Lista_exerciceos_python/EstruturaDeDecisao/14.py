#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
"""
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E

  O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
  """

nota_01 = int(input('Nota 01: '))
nota_02 = int(input('Nota 02: '))

media = (nota_01 + nota_02) / 2




if media >= 9 and media <=10:
    print('Nota: A')
    print(f'Media {media}, APROVADO')

elif media >= 7.5 and media <=9:
    print('Nota: B')
    print(f'Media {media}, APROVADO')

elif media >= 6 and media <= 7.5:
    print('Nota: C')    
    print(f'Media {media}, APROVADO')

elif media >= 4 and media <= 6:
    print('Nota: D')
    print(f'Media {media}, REPROVADO')

else:
    print('Nota: E')   
    print(f'Media {media}, REPROVADO')     

print(media)    
