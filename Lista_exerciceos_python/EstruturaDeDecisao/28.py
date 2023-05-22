#O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
'''
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
'''

print('                      Até 5 Kg           Acima de 5 Kg')
print('File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg')
print('Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg')
print('Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg')

print('Qual a carne')
opc = input('File Duplo[1], Alcatra[2], Picanha[3]: ')[0].strip()
kg = int(input('Qauntos Kg: '))
forma = input('forma de pagmento cartão tabajara com 5%, de desconto ou OUTROS: [C/O] ')[0].strip()
total = 0
tipo = ''

if opc == '1':
    tipo = 'File Duplo'
    if kg <= 5:
        total = kg * 4.90

    else:
        total = kg * 5.80    

elif opc == '2':
    tipo = 'Alcatra'
    if kg <5:
        total = kg * 5.90

    else:
        total = kg * 6.80    

elif opc == '3':
    tipo = 'Picanha' 
    if kg <5:
        total = kg * 6.90
        
    else:
        total = kg * 7.80    

else: 
    print('OPEÇÂO invalida.')        
   

if forma in 'cC':
    print(f'Tipo: {tipo}\nKg: {kg}\nTotal: {total}R$\nForma de Pagmento: Cartão Tabajara\nDesconto: 5%')    


elif forma in 'Oo':
    print(f'Tipo: {tipo}\nKg: {kg}\nTotal: {total}R$\nForma de Pagmento: Outros\nDesconto: 0%')  

else:
    print('Forma de pamentento invalida.')      


