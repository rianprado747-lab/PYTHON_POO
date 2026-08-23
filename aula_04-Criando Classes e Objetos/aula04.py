'''
Objetos são variáveis evoluídas
Em outras palavras, objetos são variáveis que, além de guardar dados, podem fazer coisas com esses dados.
Podemos definir a classe em outro arquivo e chama-lá
'''
class Eu:
    def __init__(self): #método construtor, é o começo da instância.
        self.nome = ''
        self.idade = 0

    def aniversrio(self):
        self.idade += 1

    def msg(self):
        return f'{self.nome} esta estudando POO e tem {self.idade} anos de idade'

p1 = Eu()
p1.nome = 'Rian'
p1.idade = 24
p1.aniversrio()
print(p1.msg())

g1 = Eu()
g1.nome = 'Tadeo'
g1.idade = 12
print(g1.msg())
g1.aniversrio()
print(g1.msg())
print(f'{p1.nome} tem um gato chamado {g1.nome} e ele tem {g1.idade} anos de idade')