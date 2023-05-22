from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

caminho = "c:/Users/cliente/Desktop/CODE/python/CURSO_PYTHON/Nivel 03/POO/aula_18/aula_18_LOG.txt"


class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente um metudo')
    
    def log_erro(self, msg):
        return self._log(f'ERRO: {msg}')

    def log_success(self, msg):
        return self._log(f'SUCCESS: {msg}')
"""   
class LogFileMixin(Log):
    def _log(self, msg):
        msg_format = f'{msg} ({self.__class__.__name__ })'
        with open(LOG_FILE, 'w') as arquivo:
            arquivo.write(msg_format)
            arquivo.write('\n')
"""
class LogFileMixin(Log):
    def _log(self, msg):
        print(msg)
        msg_fomatada = f'{msg} ({self.__class__.__name__})'
        print('Salvando no log:', msg_fomatada)
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_fomatada)
            arquivo.write('\n')

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg}({self.__class__.__name__ })')   

if __name__ == '__main__':
    lp = LogPrintMixin()     
    lp.log_erro('BATATA')           
    lp.log_success('Deu certo')
    lf = LogFileMixin()     
    lf.log_erro('BATATA')           
    lf.log_success('Deu certo')
    
