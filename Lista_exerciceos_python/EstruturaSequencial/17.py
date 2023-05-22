#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# a - comprar apenas latas de 18 litros;
# b - comprar apenas galões de 3,6 litros;
# c - misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

metros_quadrado = float(input('M^2: '))

litros = metros_quadrado / 6

print(f'A quantidade de litros de tinta para pintar uma area de {metros_quadrado}m2 é de {litros:.2f}l')

latas = round(litros / 18 + 0.5) 
valor_latas = 80

galoes = round(litros / 3.6 + 0.5)
valor_galoes = 25

print(f'A quantidade de latas necessaris é {latas} latas, é o valor é de {valor_latas * latas:.1f}R$')
print(f'Os galões necessarios é {galoes} galões, é o valor é de {valor_galoes  * galoes:.1f}R$')





