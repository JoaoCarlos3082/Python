"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""

def soma(a, b):
    s = a + b

    print(s)

soma(3, 4)

def ola(nome='Sem nome'):
    print(f'Ola!, {nome}')

ola('carlos')
ola()    