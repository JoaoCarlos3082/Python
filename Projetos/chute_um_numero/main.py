import random

help(random)

def titulo():
    print('==='*10)
    print('')
    print('Chute o numero que eu pensei de 0 a 100.'.upper())
    print('')
    print('==='*10)

titulo()

def checar_numero(numero, acerto):

    if numero == numero_aleatorio:
        acerto = True # flag para o acerto do numero
        print(f'Parabens você acertou o numero que eu estava pesando era o {numero_aleatorio}.')
    
    # ver se o numero digitado esta proximo de numero_aleatorio de 10
    elif numero_aleatorio - numero <= 10 and numero_aleatorio - numero >= 0:
        acerto = False
        print(f'Um pouco mais que {numero}.')
        print()

    elif numero - numero_aleatorio <= 10 and numero - numero_aleatorio >= 0:
        acerto = False
        print(f'Um pouco menos que {numero}.')
        print('')

    elif numero_aleatorio < numero:
        acerto = False
        print(f'O numero que eu pensei e menor que {numero}.')
        print()


    elif numero_aleatorio > numero:
        acerto = False
        print(f'O numero que eu pensei e maior que {numero}.')
        print()

    return acerto  

while True:  
    numero_aleatorio = random.randint(0, 100) # Numero aleatorio
    tent = 0 # numero de tentativas
    flag_continue = False
            
    while True:
        chute = input('Numero: ').strip()
        valor_permitido = None
        acerto = False
        cont = False


        # Transformando o valor em um inteiro
        try:
            chute_int = int(chute)

        # Se não for possivel ser um iteiro   
        except:    
            print('Digite um numero inteiro entre 0 e 100.')
            continue
        
        # vendo se o valor e menor que 0 ou maior que 100
        if chute_int < 0 or chute_int > 100:
            valor_permitido = False
            print(f'Valor não permitido tem que ser entre 0 a 100, valor digitado foi {chute_int}.')   

        # continuado o programa caso o numero respeite as condições
        else:
            tent += 1
            valor_permitido = True

        if valor_permitido == True:
            acerto = checar_numero(chute_int, acerto)
            if acerto == True:
                print('')
                print(f'Numero de tentativas para foi de {tent}!.')
                print('')
                break
    continuar = input('Continuar [s] ou digite qual quer coisa para finalizar: ')[0].strip().lower()

    while flag_continue is False:
        if continuar == 's':
            print('Tudo bem.')
            flag_continue = False
            break

        else:
            flag_continue == True
            break 
               

    if flag_continue == True:
        break
        
