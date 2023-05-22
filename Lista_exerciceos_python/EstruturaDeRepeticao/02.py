#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

login = input('Nome de Usuario: ')

while True:
    senha = input('Senha do Usuario: ')

    if senha == login:
        print('A senha não pode ser igual a o login')

    else:
        break    