print("=" * 42)
print("      SISTEMA COMERCIAL - SISCON")
print("=" * 42)
print('Bem-vindo ao sistema!')
print('Projeta desenvolvido em python.')


from models.categoria import Categoria

categoria1 = Categoria('Hort Frut', 'Frutas e Legumes')
print(categoria1.apresentar())

categoria2 = Categoria('Papelaria', 'Materiais escolares')
print(categoria2.apresentar())

categoria3 = Categoria('Iformatica', 'Acessorios e Equipamentos')
print(categoria3.apresentar())

from models.produto import Produto

produto1 = Produto('caderno', 10, 80)

print(produto1.apresentar())

produto1.calcular_valor_estoque()