#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

metros_quadrado = float(input('M^2: '))

litros = metros_quadrado / 3

print(f'A quantidade de litros de tinta para pintar uma area de {metros_quadrado}m2 é de {litros:.2f}l')

latas = round(litros / 18 + 0.5) # aredondar o numero, o raund aredonda para o numero inteiro mais proximo, para não aredondar para zero colocamos o + 0.5
# pedemos tamber pegar a função "ceil" da biblioteca "math"
# latas = math.ceil(litros / 18)
total = 80

print(f'A quantidade de latas de tintas necessaria é {latas:.1f} e o total é de {total * latas:.1f}R$')