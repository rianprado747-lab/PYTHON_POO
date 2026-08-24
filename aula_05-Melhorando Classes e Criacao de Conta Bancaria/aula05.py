class Pessoa:#Definimos o doc da classe na primeira linha de baixo usando, igual as docString de funcoes. """
    """
Essa classe cria uma pessoa com nome e idade

Para criar uma nova pessoa, use
variavel = Pessoa(nome, idade)
    """
    def __init__(self,nome = 'Vazio',idade = 0): #método construtor, é o começo da instância.
        #Definimos parametros na definição da Função da classe para passar os atributos na hora de criar o objeto.
        # Tambem podemos deixar o parâmetro com valor Default para ser opcional.
        self.nome = nome
        self.idade = idade

    def aniversrio(self):
        self.idade += 1

    def __str__(self):#todo objeto tem o metodo __str__ que mostra o endereço do objeto na memória. é chamado de Dunder Method
        return f'{self.nome} esta estudando POO e tem {self.idade} anos de idade'

    def __getstate__(self):
        return f'Estado: nome = {self.nome} ; idade = {self.idade}'

p1 = Pessoa('Rian',23)
p1.aniversrio()
print(p1)

p2 = Pessoa(nome = 'Pedro',idade = 20)
p2.aniversrio()
print(p2)

p3 = Pessoa()
p3.aniversrio()
print(p3)

print(p1.__doc__)#Chamando o manual da classe Pessoa
print(p1.__dict__) # atributo
print(p1.__getstate__()) #método, também é possivel sobrescrever o getstate().
print(p1.__class__) # mostra o nome da classe do objeto
