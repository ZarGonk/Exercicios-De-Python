class ContaBancaria:
    """Criação de uma conta bancaria de saque e depositos"""
    def __init__(self, id, name, saldo = 0):
        self.id = id
        self.titular = name
        self.saldo = saldo
        print(f"Conta {self.id} Criada com sucesso. Saldo Atual de R$ {self.saldo:,.2f}")
    
    def __str__(self):
        return f'A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo.'

    def deposito(self, value):
        self.saldo += value
        print(f'Deposito de R$ {value:,.2f} realizado')
        

    def saque(self, value):
        if self.saldo > value:
            self.saldo -= value
            print(f'Saque de R$ {value:,.2f} realizado')

        print(f'Saldo NEGADO. Valor atual R${self.saldo:,.2f}: SALDO INSUFICIENTE')
        

c1 = ContaBancaria(456, "Gustavo", 3000)
c1.deposito(500)
c1.saque(8000)
print(c1)