class Fornecedor:
    def __init__(self, nome, telefone, email):
        self.nome: nome
        self.telefone: telefone
        self.email: email

    def apresentar(self):
        return (
            f'fornecedor: {self.nome}\n'
            f'telefone: {self.telefone}\n'
            f'email: {self.email}\n'
            )