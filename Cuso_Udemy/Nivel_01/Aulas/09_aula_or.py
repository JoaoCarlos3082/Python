# 'OR' (ou) ele para no primeiro valor verdadeiro.

entrada = input(' [E]ntrar ou [S]air: ')

senha = input('Senha: ')

senha_check = '12345'

if entrada == 'E' or entrada == 'e' and senha == senha_check:
    print('Entrando.')

else:
    print('Saido.')