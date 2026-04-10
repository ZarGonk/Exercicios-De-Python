from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, idade, especializacao, nivel):
        super().__init__(nome, idade)
        self.especializacao = especializacao
        self.nivel = nivel
    
    def dar_aula(self):
        print(f'Prof. {self.nome} comecou a dar aula')