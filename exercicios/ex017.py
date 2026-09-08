from rich import print
from rich.panel import Panel
'''
Crie a classe Produto, onde podemos cadastrar nome e o preço. Crie também um método que mostre uma etiqueta de preço do
produto.
'''
class Produto :
    """
    Cadastra um produto com nome e preço .
    """
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        print(f'Produto {self.nome} no valor R${self.preco} cadastrado com sucesso')

    def etiqueta(self):
        caixa = Panel(f'VALOR:[red]{self.preco:^15,.2f}[/]',title = self.nome,width = 34, style = 'blue')
        print(caixa)

p1 = Produto('Iphone 17 Pro Max',25_000.85)
p1.etiqueta()

p2 = Produto('Caminhoneta',34000)
p2.etiqueta()
