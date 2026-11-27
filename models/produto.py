class Produto:
    def __init__(self, nome, preco, estoque, categoria, fornecedor):
        self.nome = nome
        self.preco = float(preco)
        self.estoque = int(estoque)
        self.categoria = categoria
        self.fornecedor = fornecedor

    def apresentar(self):
        return (
            f'Nome: {self.nome}\n' 
            f'Preço: R${self.preco}\n'
            f'Estoque: {self.estoque} unidades\n'
            f'Categoria: {self.categoria.nome}\n'
            f'Fornecedor: {self.fornecedor.nome}\n'
            )

    def calcular_valor_estoque(self):
        valor = self.estoque * self.preco
        return f'o valor do estoque é :{valor}'

    def adicionar_estoque(self, quantidade):
        if quantidade <= 0:
            raise ValueError ("A quantidade deve ser maior que zero")
        self.estoque += quantidade
        print(f'A quantidade {quantidade} foi adicionada no estoque.')
        print(f'Quantidade em estoque atual {self.estoque}')
 
    def remover_estoque(self, quantidade):
        if quantidade <= 0:
            raise ValueError ("A quantidade deve ser maior que zero")
        if self.estoque < quantidade:
            raise ValueError (f"Estoque insuficiente. Quantidade atual: {self.estoque}")
        self.estoque -= quantidade
        print(f'A quantidade {quantidade} foi removida do estoque.')
        print(f'Quantidade em estoque atual {self.estoque}')
 

        