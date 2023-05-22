import random

cpf = ''

for c in range(0,9):
    cpf += str(random.randint(0,9))

nove_digitos = cpf[:9]
lista = []
resultado = []
resultado2 = []

for numero in range(0,9):
    lista.append(int(cpf[numero])) 

cont = 0
for mult in cpf:
    if cont < 9:
        numero = 10 - cont
        resultado.append(lista[cont] * numero)
        cont += 1
    else:
        break    

primeiro_digito = (sum(resultado) * 10) % 11 

if primeiro_digito > 9:
    primeiro_digito = 0
else:
    primeiro_digito = primeiro_digito

lista.append(primeiro_digito)
cpf += str(primeiro_digito)

cont2 = 0
for mult2 in cpf:
    if cont2 < 10:
        numero = 11 - cont2
        resultado2.append(lista[cont2] * numero)
        cont2 += 1
    else:
        break  

segundo_digito = (sum(resultado2)* 10) % 11  

if segundo_digito > 9:
    segundo_digito = 0
else:
    segundo_digito = segundo_digito

lista.append(segundo_digito)       
cpf += str(segundo_digito)

cpf_calculado = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

if cpf == cpf_calculado:
    print(f'{cpf} é valido!')
else:
    print(f'{cpf} é invalido!')    
        