# Manter Estado na class

class Filmar:
    
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando # Defininado o estado como False

    def filmar(self):

        # mantendo o estado da class
        if self.filmando is True: # mantendo o novo valor de false para true
            print(f'A {self.nome} já esta filmando')
            return # parando a execução do metudo

        print(f'A camera {self.nome} esta filmando.')
        self.filmando = True # pasando o valor False para True
    
    # desligar a filmagem
    def desligar_filmar(self):
        if self.filmando is False: # se estiver no estao de false
            print(f'A camera {self.nome} não esta filmando')
            return

        print(f'A camera {self.nome} parou de filmar.')
        self.filmando = False # passando o estado de false

    def fotografar(self):# situação onde a camera não consegue tirar foto no estado de filmar
        if self.filmando is True: # no estado True não e possivel tirar foto
            print(f'A camera {self.nome} esta filmando não e possivel tirar foto. ')
            return
        
        # Tirando a foto
        print(f'A camera {self.nome} tirou uma foto.')    

camera01 = Filmar('Motorola')

camera02 = Filmar('Sony')

camera01.filmar()
camera01.filmar()
camera01.fotografar()
camera01.desligar_filmar()
camera01.desligar_filmar()
camera01.fotografar()
print('')
camera02.desligar_filmar()
camera02.fotografar()
