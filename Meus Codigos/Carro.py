class Carro:
    def __init__(self, modelo, marca, condicao):
        self.modelo = modelo
        self.marca = marca
        self.condicao = condicao
        self.estado = False
    
    def ligar_carro(self):
        if self.estado == False:
            print('Vrummm Vrumm')
            self.estado = True
            return self.estado
        
        if self.estado == True:
            print(f'{self.modelo} ja esta ligado')

    def desligar_carro(self):
        if self.estado == True:
            print(f'{self.modelo} desligado')
            self.estado = False
            return self.estado
        
        if self.estado == False:
            print(f'{self.modelo} ja esta desligado')
    

    def andar(self):
        if self.estado == True:
            print(f'{self.modelo} esta andando')
        if self.estado == False:
            print(f'{self.modelo} não pode andar: Desligado')


opala = Carro("Opala", "Chevrolet", "Novo")

#print(opala.condicao)

opala.ligar_carro()

opala.desligar_carro()
opala.andar()