# Declaração de classe
class Pessoa():
    def __init__(self, nome, idade, altura): # Metodo construtor 
        # Atributos de Instancia
        self.nome  = nome
        self.idade = idade
        self.altura = altura

    # Metodos de instancia 
    def aniversario(self):
        self.idade += 1
    
    def mensagem(self):
        return print(f"Nome: {self.nome} e Idade: {self.idade}")



# Declaração de objetos
p1 = Pessoa("Rogerinho", 34, 1.67)
p1.aniversario()
p1.mensagem()