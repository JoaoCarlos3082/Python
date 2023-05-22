#Uma fruteira está vendendo frutas com a seguinte tabela de preços:
'''
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente
'''

print('                      Até 5 Kg           Acima de 5 Kg')
print('Morango         R$ 2,50 por Kg          R$ 2,20 por Kg')
print('Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg')

morango = float(input('Qauntos Kg de morango: '))
maca = float(input('Qauntos Kg de maça: '))
total_morango = 0
total_maca = 0
total_kg = morango + maca

if morango <= 5:
    total_morango = morango * 2.50

else:
    total_morango = morango * 2.20

if maca <=5:
    total_maca = maca * 1.80    

else:    
    total_maca = maca * 1.50  

if total_kg > 8 or total_morango + total_maca > 25:
    print(f'O total deu {total_maca + total_morango}R$ com {total_kg}Kg em frutas, mas com o desconto de 10% deu {(total_maca + total_morango - ((total_maca + total_morango) * 10) / 100)}')

else:
    print(f'O total deu {total_maca + total_morango}R$ com {total_kg}Kg em frutas')
