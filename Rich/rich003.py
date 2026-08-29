from rich import print
from rich.table import Table

tabela = Table(title = 'Tabela de preços')

tabela.add_column('Nome', justify = 'right', style = 'red')
tabela.add_column('Preço', justify='center', style = 'blue')
tabela.add_row('Estrela', 'R$2345.99')
tabela.add_row('Planeta', 'R$3456.99')
print(tabela)
