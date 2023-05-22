#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

temperatura_mes = [23.1, 25.2 , 19.8, 19.1 ,25.9, 15.21, 19.7, 21.9, 31.2, 29.1, 21.3, 16.3]

mes = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul','Ago', 'Set', 'Out', 'Nov', 'Dez']

for i in range(12):
    print(f'{mes[i]} - {temperatura_mes[i]}', end=' ')