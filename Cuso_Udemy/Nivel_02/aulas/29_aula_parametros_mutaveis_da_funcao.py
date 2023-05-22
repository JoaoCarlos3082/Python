# problema dos parâmetros mutaveis da função

def lista_nome_com_erro(nome, lista=[]): # apresenta um problema com o uso de um parâmetro mutável como valor padrão. Isso pode levar a resultados inesperados, pois a mesma lista é compartilhada entre todas as chamadas da função que não passam um segundo argumento.
    lista.append(nome)
    return lista

nome_com_erro1 = lista_nome_com_erro('Carlos') # criando a lista 01
lista_nome_com_erro('Varus', nome_com_erro1)   # adicionado valores na lista 01

# Com o parâmetro mutável com valor padrão '[]' faz com que as lista fiquem compatilhadas 

nome_com_erro2 = lista_nome_com_erro('Maria')
lista_nome_com_erro('Aatrox', nome_com_erro2)

print(nome_com_erro1)
print(nome_com_erro2)

print()
print('---'*10)
print()

def lista_nome_correta(nome, lista = None): # Melhor de corregir para não ter o erro e colocar a lista como 'None'
    if lista is None: # criando a lista toda vez que não e passado o parametro de lista
        lista = []
    lista.append(nome)
    return lista

nome01 = lista_nome_correta('Matheus') # criando a lista 01
lista_nome_correta('Martins', nome01)  # adicionado valores na lista 01

nome02 = lista_nome_correta('Douglas')
lista_nome_correta('Pedro', nome02)


print(nome01)
print(nome02)
