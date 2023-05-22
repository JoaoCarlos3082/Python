# Positional-Only Parameters (/) e Keyword-Only Arguments (*)
# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)
# 🟢 Positional-only Parameters (/) - Tudo antes da barra deve
# ser ❗️APENAS❗️ posicional.
# PEP 570 – Python Positional-Only Parameters
# https://peps.python.org/pep-0570/
# 🟢 Keyword-Only Arguments (*) - * sozinho ❗️NÃO SUGA❗️ valores.
# PEP 3102 – Keyword-Only Arguments
# https://peps.python.org/pep-3102/

def soma1(x ,y, /, u, z): #Positional-only Parameters (/) - Tudo antes da barra deve ser ❗️APENAS❗️ posicional.
    print(x + y + u + z)

soma1(1, 2)
soma1(x=1, y=2)    

def soma2(v, q):
    print(v + q)