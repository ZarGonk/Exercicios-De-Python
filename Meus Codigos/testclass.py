class MinhaClassDocumentada:
    """Está é a documentação da minha class, como exemplo do __doc__"""

    def __init__(self, name=''):
        self.name = name

    def __str__(self):
        return 'Hello, World !'


mcd = MinhaClassDocumentada("Test")
print(mcd)


print(MinhaClassDocumentada.__doc__)
print(mcd.__dict__)
print(mcd.__getstate__())
print(mcd.__class__)