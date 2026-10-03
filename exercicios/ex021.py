'''
Crie a classe Caneta, que simule o funcionamento de uma caneta colorida, podendo escrever frases na cor relativa.
'''
'''
Crie uma classe livro, que vai simular a passagem de páginas de um livro, considerando também se o usuário chegou ao fim
da leitura.
'''
class Caneta :
    def __init__(self,cor):
        """
        Escreve um texto em preto,vermelho,azul ou verde
        """
        self.cor = cor.upper()

    def escrever (self,texto):
        if self.cor == 'PRETO':
            print(f'\033[30m{texto}\033[m')
        elif self.cor == 'VERMELHO':
            print(f'\033[31m{texto}\033[m')
        elif self.cor == 'AZUL':
            print(f'\033[34m{texto}\033[m')
        else :
            print(f'\033[32m{texto}\033[m')


c1 = Caneta('preto')
c1.escrever('Olá mundo')

c2 = Caneta ('vermelho')
c2.escrever('Olá mundo')

c3 = Caneta ('azul')
c3.escrever('Olá mundo')

c4 = Caneta ('verde')
c4.escrever('Olá mundo')
