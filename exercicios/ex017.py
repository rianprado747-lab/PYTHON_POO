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
        caixa = Panel(f'[red]R${self.preco:.2f}[/]',title = self.nome,width = 10, style = 'blue')
        print(caixa)

p1 = Produto('Teclado',650)
p1.etiqueta()

p2 = Produto('Caminhoneta',34000)
p2.etiqueta()
