from models.categoria import Categoria

class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        

    def apresentar(self):
        return f'Nome: {self.nome} | Preço: R${self.preco} | Estoque: {self.estoque} unidades'

    def calcular_valor_estoque(self):
        valor = self.estoque * self.preco
        return f'o valor do estoque é :{valor}'

    def atualizar_estoque(self):
        print('(1) Adicionar ao estoque.')
        print('(2) Remover do estoque.')

        escolha = int(input("digite sua escolha: "))

        if escolha == 1 :
            qtd_adicionada = int(input('quantos produtos deseja adicionar?  '))
            self.estoque += qtd_adicionada
            return self.estoque
        elif escolha == 2 :
            qtd_retirada = int(input('quantos produtos deseja remover?  '))
            if qtd_retirada > self.estoque:
                
                

                self.estoque -= qtd_retirada
                return self.estoque
        else:
            print('escolha uma opção valida!!!')

        