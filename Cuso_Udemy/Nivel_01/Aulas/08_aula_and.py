# 'AND' (e) todos os valores são True, parando no primeiro valor False

entrada = input(' [E]ntrar ou [S]air: ')

senha = input('Senha: ')

senha_check = '12345'

if entrada == 'E' and senha == senha_check:
    print('Entrando.')

else:
    print('Saido.')