from itertools import groupby

#groupby necessita que os dados estagam ordenados

#"lista" de alunos tendo "dicionarios"
alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]


grupo_alunos = sorted(alunos, key=lambda a:a['nota'])#ordenado os dados
grupos = groupby(grupo_alunos, key=lambda a:a['nota'])#colocando em grupos


for chave, grupo in grupos:#pegar a "chave" de cada grupo, ja o grupo mostra os dados que esta em cada chave
    print(chave)
    for aluno in grupo:#dados da cahve
        print(aluno)

        