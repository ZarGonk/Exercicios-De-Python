# Declaração de classe
class Person:
    # Criando documentação para minha classe
    """
    Essa classe cria um gafanhoto, que é uma pessoa que tem nome e idade.

    Para criar uma nova pessoa, use:
    Variavel = Person(name, age)
    """
    def __init__(self, name='guess', age=0):  # Metodo construtor
        # Atributos de Instancia
        self.name = name
        self.age = age

    # Metodos de instancia
    def anniversary(self):
        self.age += 1

    def __str__(self): # Dunder Method
        return f"Nome: {self.name} e Idade: {self.age}"


if __name__ == "__main__":
    # Declaração de objetos
    p1 = Person("Rogerinho", 34)
    p1.anniversary()
    print(p1)

    # print(p1.__doc__) # __doc__ = dunder attribute



    p2 = Person("Farofina", 18)
    print(p2)

    print(p2.__dict__)
    print(p2.__getstate__())