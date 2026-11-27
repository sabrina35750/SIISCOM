from models import Categoria, Produto, Fornecedor, Movimento_estoque

categoria1 = Categoria('Eletronicos', 'Produtos eletronicos e gadget')
categoria2 = Categoria('Papelaria', 'Materiais escolares')
categoria3 = Categoria('imformática', 'acessorios e equipamentos')

fornecedor1 = Fornecedor('Fornecedor A', '(27)3354-6212', 'fornecedorA@gmail.com' )
fornecedor2 = Fornecedor('Fornecedor B', '(27)1515-5846', 'fornecedorB@gmail.com' )

produto1 = Produto('Notebook', 5000.00, 10, categoria1, fornecedor1)
produto2 = Produto('Caneta', 2.50, 100, categoria2, fornecedor1)
produto3 = Produto('Teclado', 150.00, 20, categoria3, fornecedor2)

print(produto1.apresentar())
print(produto2.apresentar())
print(produto3.apresentar())

try:
    movimento1 = Movimento_estoque('entrada', 5, '26/11/2026', produto1)
    movimento1.executar()

    movimento2 = Movimento_estoque('saida', 4, '26/11/2026', produto1)
    movimento2.executar()

    movimento3 = Movimento_estoque('saida', 5, '26/11/2026', produto1)
    movimento3.executar()
except ValueError as erro:
    print(f'Ocoreu um erro: {erro}')

