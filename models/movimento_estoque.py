class Movimento_estoque:
    def __init__(self, tipo, quantidade, data, produto):
        self.tipo = tipo
        self.quantidade = int(quantidade)
        self.data = data
        self.produto = produto

    def apresentar(self):
        return(
            f'Tipo: {self.tipo}\n'
            f'Quantidade: {self.quantidade}\n'
            f'Data: {self.data}\n'
            f'Produto: {self.produto.nome}\n'
        )

