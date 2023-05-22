# Variáveis livres + nonlocal (locals, globals)

def concatenar(argumento_inicial):
    argumento_final = argumento_inicial

    def interno(valor_a_concatenar=''):
        nonlocal argumento_final # nonlocal faz com a varivel não se local assim não dando erro na execução do progroma
        argumento_final += valor_a_concatenar
        return argumento_final
    return interno    


a = concatenar('a')
print(a('b'))
print(a('2'))
final = a()
print(final)