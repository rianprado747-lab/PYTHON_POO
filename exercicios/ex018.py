from rich import print
from rich.panel import Panel
'''
Crie a classe Churrasco, onde seja possivel informar quantas pessoas vão participar e mostre quanto de carne deve ser
comprado, o custo total do churrasco e o preço por pessoa.
Consumo padrão : 400g por pessoa 
preço : R$82,40/kg
'''

class Churrasco:
    def __init__(self,titulo = '',pessoas =0,):
        self.pessoas = pessoas
        self.titulo = titulo

    def analisar(self):
        kg = self.pessoas * 0.4
        valor = 82.40 * kg
        caixa = Panel(f'[white]{self.pessoas} pessoas irão participar do churrasco[/]'
                      f'\n[red]R${valor:.2f} por pessoa[/] '
                      f'\n[purple]{kg}KG de carne será necessário[/]',
                      title = self.titulo,style = 'blue', width= 30)
        return caixa
c1 = Churrasco('Churrasco do Rian',50)
print(c1.analisar())

c2 = Churrasco('BANQUETE DE NÚMENOR',90)
print(c2.analisar())

