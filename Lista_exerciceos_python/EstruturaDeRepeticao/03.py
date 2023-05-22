#Faça um programa que leia e valide as seguintes informações:
"""''
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
''' """

nome = input("Nome: ").strip()
idade = int(input("Idade: "))
salario = int(input("Salario: "))
sexo = input("F, M")[0].strip()
estado_civel = input("Solteiro(s), Casado(c), Viuvo(v), Divociado(d)")[0].strip().lower()


if len(nome) > 3:
    print("nome maior que 3 caracteres")

else:
    print('O nome tem menos que 3 caracters.')

if idade >= 0 and idade <=150:
    print(f'Idade {idade} esta entre 150 anos')

else:
    print('Idade invalida')

if salario > 0:
    print(f'Salario {salario}R$ e maior que zero')  

else:
    print(f'Salario {salario}R$ e menor que zero')  

if sexo in 'FfMm':
    print(f'Sexo: {sexo}')

else:
    print(f'Sexo invalido: {sexo}')

if estado_civel in 'scvd':
    print(f'Estado civil: {estado_civel}')

else:
    print(f'Estado civil invalido: {estado_civel}')                              