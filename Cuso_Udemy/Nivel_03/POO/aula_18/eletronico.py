from aula_18_LOG import LogPrintMixin

class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if not self._ligado:
            self._ligado = True

    def desligar(self):
        if self._ligado:
            self._ligado = False

class SmartPhone(Eletronico, LogPrintMixin):
    def ligar(self):
        super().ligar()
    
        if self._ligado:
            msg = f'{self._nome} esta ligado'
            self.log_success(msg)
    
    def desligar(self):
         super().desligar()
         if self._ligado:
            msg = f'{self._nome} esta desligado'
            self.log_erro(msg)
    
