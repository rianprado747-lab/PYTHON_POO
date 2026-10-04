'''
Crie a classe Caneta, que simule o funcionamento de uma caneta colorida, podendo escrever frases na cor relativa.
'''
from operator import truediv

'''
Crie uma classe livro, que vai simular a passagem de páginas de um livro, considerando também se o usuário chegou ao fim
da leitura.
'''
from rich import print
class Caneta :
    def __init__(self,cor =''):
        """
        Escreve um texto em preto,vermelho,azul ou verde
        """
        self.cor = cor.upper()
        self.destampa = False


    def destampar(self) -> bool:
            self.destampa = True
            return True

    def tampar(self):
        self.destampa = False


    def escrever (self,texto):

        if self.destampa :
            match self.cor:# o match é tipo o escolha caso do Portugol
                case 'PRETO':
                    print(f'[black]{texto}[/]')
                case 'VERMELHO':
                    print(f'[red]{texto}[/]')
                case 'AZUL':
                    print(f'[blue]{texto}[/]')
                case 'VERDE':
                    print(f'[green]{texto}[/]')
                case _:# caso nenhuma cor seja escolhida, é como o else, usamos o _
                    print(f'[white]{texto}[/]')
        else:
            print('[red]A caneta está tampada seu Mánezão[/]')


c1 = Caneta('preto')
c1.destampar()
c1.tampar()
c1.escrever('Olá mundo')

c2 = Caneta ('vermelho')
c2.destampar()
c2.escrever('Olá mundo')

c3 = Caneta ('azul')
c3.destampar()
c3.escrever('Olá mundo')

c4 = Caneta ('verde')
c4.destampar()
c4.escrever('Olá mundo, essa cor é verde')

c5 = Caneta()
c5.destampar()
c5.escrever('Tenho duas espadas, uma de aço para homens e uma de prata para criaturas,'
            ' ambas são para monstros.S ')
