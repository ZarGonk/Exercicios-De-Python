# Declaração de classe
class Person:
    def __init__(self, name='', age=0): # Metodo construtor
        # Atributos de Instancia
        self.name  = name
        self.age = age

    # Metodos de instancia 
    def anniversary(self):
        self.age += 1
    
    def message(self):
        return print(f"Nome: {self.name} e Idade: {self.age}")


if __name__ == "__main__":
    # Declaração de objetos
    p1 = Person("Rogerinho", 34)
    p1.anniversary()
    p1.message()

    p2 = Person("Farofina", 18)
    p2.message()