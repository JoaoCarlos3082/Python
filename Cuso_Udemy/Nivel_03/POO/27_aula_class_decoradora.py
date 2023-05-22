# class decoradoras

class Multiplicar:
    def __init__(self, func):
        self.func = func
        self._multiplicador = 2

    def __call__(self, *args, **kwargs):
        resultado = self.func(*args, **kwargs)

        return resultado * self._multiplicador

@Multiplicar
def soma(x, y):
    return x + y

c = soma(2, 2)
print(c)