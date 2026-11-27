class Conta:
    def __init__(self, nome_titular):
        self.nome_titular = nome_titular
        self.poupanca = 0
    
    def depositar(self,valor):
        if valor <= 0:
            raise ValueError ('O depósito deve ser maior que zero!')
        self.poupanca += valor


conta1 = Conta('Sabrina')
conta1.poupanca = -500



print(conta1.poupanca)

