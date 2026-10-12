from rich import print
from abc  import ABC, abstractmethod # Abstract Base Class

class Pessoa(ABC): # Classe abstrata
    def __init__(self,nome = '', idade = 0 ):
        self.nome = nome
        self.idade = idade


    def fazer_aniversario(self):
        self.idade += 1

    @abstractmethod
    def estudar(self):#todas as subclasses teram esse metodo
        pass


class Aluno(Pessoa):# Colocamos ao lado da subclasse entre () a Superclasse de onde irão herdar os atributos
    def __init__(self,nome = '',idade = 0, curso = '', turma = ''):
        super().__init__(nome, idade)#Executa o INIT da Superclasse, comando obrigatorio em subclasses
        self.curso = curso
        self.turma = turma


    def fazer_matricula(self):
        print(f'O aluno {self.nome} acabou de se matricular')

    def estudar(self):
        print(f'O aluno {self.nome} está estudando {self.curso} na sala {self.turma}')


class Professor(Pessoa):# Professor herda da Superclasse Pessoa
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel


    def dar_aula(self):
        print(f'O Professor {self.nome} começou a aula\n[purple]RYOUKI TENKAI![/]')

    def estudar(self):
        print(f'O {self.nome} sensei está treinando {self.especialidade} para ultrapassar o nivel {self.nivel}')

class Funcionario(Pessoa):# Funcionario herda da Superclasse Pessoa
    def __init__(self,nome,idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor


    def bater_ponto(self):
        print(f'O funcionário {self.nome} acabou de bater o ponto e está muito'
              'bravo, pois é segunda feira ')

    def estudar(self):
        print(f'O {self.nome} está estudando para ser um {self.cargo} melhor e sair da {self.setor}')