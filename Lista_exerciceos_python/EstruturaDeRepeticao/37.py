# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes

cont = 0

maior = 0
menor = 0

while True:
    cont += 1
    altura = float(input(f'Altura do cliente {cont}: '))
    #peso = float(input(f'Pesso do cliente {cont}: '))
    if altura == 0:
        break    

    if altura > maior:
        maior = altura

    if altura > menor:
        menor = altura

    if altura < menor:
        menor = altura

print(maior)
print(menor)

