#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
#(32°C × 9/5) + 32 

celsius = float(input('Celsius: '))

fahrenheit = (celsius * (9/5)) + 32

print(f'O grao celsius {celsius}c em fahrenheit é {fahrenheit:.2f}f')