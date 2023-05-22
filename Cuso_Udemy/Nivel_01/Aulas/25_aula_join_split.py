"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""


frase = 'Elden ring melhor e que god of war para de chorar e pronto'

frase_split = frase.split(' ')

print(frase_split)

frase_com_espaso = '   frase com muitos espasos   '

print(frase_com_espaso.strip())  # tira espaços do inicio e final
print(frase_com_espaso.lstrip()) # do lado esquerdo
print(frase_com_espaso.rstrip()) # do lado direito 
