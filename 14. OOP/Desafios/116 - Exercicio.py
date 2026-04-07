from rich import print

class Funcionario:
    def __init__(self, name='Guests', sector='Mendigo', position='Desempregado'):
        self.name       = name
        self.sector     = sector
        self.position   = position
    
    def apresentação(self):
        return f'Olá, sou [blue]{self.name}[/] e sou [blue]{self.position}[/] do setor de [green]{self.sector}[/] da empresa VAI QUE É TUA'


c1 = Funcionario("Maria", "Administração", "Diretora")
print(c1.apresentação())

c2 = Funcionario("Pedro", "TI", "Programador")
print(c2.apresentação())