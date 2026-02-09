def soma(a, b):
    s = a + b
    return s

## print(soma(5, 5))


class Soma():
    def __init__(self,a , b):
        self.a = a
        self.b = b

    def soma_de_dois_numeros(self):
        s = self.a + self.b
        return s

s = Soma(20, 5).soma_de_dois_numeros()
## print(s)