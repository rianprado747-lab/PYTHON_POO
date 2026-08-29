'''
Crie a classe Funcionário, onde podemos cadastrar nome,setor e cargo. Crie também um método que permita ao funcionário
se apresentar.
'''
from rich import print
from rich import inspect
class Funcionario:
    #atributos de classe
    empresa = 'VASCO DA GAMA'
    def __init__(self, nome, setor, cargo):
        #atributos de instancia
        self.nome = nome
        self.setor = setor
        self.cargo = cargo


    def apresentar(self) -> str: # a seta -> diz para a função retornar uma string
        return (f':handshake:Olá meu nome é [red]{self.nome}[/] e ocupo o cargo de [blue]{self.cargo}[/] e trabalho '
                f'com {self.setor}. Atualmente trabalho na empresa [black on white]{Funcionario.empresa}[/].')

p1 = Funcionario('Madruga','Futebol', 'Técnico do Vascão')
print(p1.apresentar())
print()
p2 = Funcionario('Saul','Direito', 'Advogado')
print(p2.apresentar())

inspect(p1, methods = True)
