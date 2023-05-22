#EMPACOTAMENTO E DESMPACOTAMENTO DICT

pessoa = {'nome' : 'Carlos',
           'sobronome' : 'Vieira',
            'idade' : '19'}

a, b, c = pessoa.items()
(t1, t2), (t3, t4), (t5, t6) = pessoa.items()

print(a, b, c)

print(t1, t2, t3, t4, t5, t6)

pessoa2 = {'nome' : 'Carlos',
           'sobronome' : 'Vieira' }

dados_pessoa2 = {'idade' : '19',
                 'Altura' : '168'}

desempacotamento = {**pessoa2, **dados_pessoa2} # **dict extrai od dicionario

print(desempacotamento)

def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)


#mostro_argumentos_nomeados(nome='Joana', qlq=123)
#mostro_argumentos_nomeados(**desempacotamento)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostro_argumentos_nomeados(**configuracoes)