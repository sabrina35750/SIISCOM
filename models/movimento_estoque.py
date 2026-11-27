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
    def executar(self):
        if self.tipo == "entrada":
            self.produto.adicionar_estoque(self.quantidade)
        elif self.tipo == "saida":
            self.produto.remover_estoque(self.quantidade)
        else:
            raise ValueError("Tipo inválido. Use 'entrada' ou 'saida'.")

