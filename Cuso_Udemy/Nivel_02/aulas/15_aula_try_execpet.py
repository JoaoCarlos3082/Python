# (Parte1) try e except para tratar exceções
c = 0

try:
    a = 20
    b = 0
    c = a / b
except ZeroDivisionError as e:
    print('Dividiu por zero.')
    print(e)
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print(error)
    print(error.__class__.__name__)
except Exception:
    print('ERRO DESCONHECIDO.')

finally: #sempre e executado idenpendente do que acontece
    print('Fim')

print(c)