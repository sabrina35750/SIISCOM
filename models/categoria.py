class Categoria:
    def __init__(self, nome, descricao=""):
        self.nome = nome
        self.descricao = descricao

    def apresentar (self):
        return f'Categoria: {self.nome} | Descrição: {self.descricao}'