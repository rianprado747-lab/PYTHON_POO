from rich import print, inspect

class Pessoa:
    def __init__(self,nome = '', idade = 0 ):
        self.nome = nome
        self.idade = idade


    def fazer_aniversario(self):
        self.idade += 1


class Aluno(Pessoa):# Colocamos ao lado da subclasse entre () a Superclasse de onde irão herdar os atributos
    def __init__(self,nome = '',idade = 0, curso = '', turma = ''):
        super().__init__(nome, idade)#Executa o INIT da Superclasse, comando obrigatorio em subclasses
        self.curso = curso
        self.turma = turma


    def fazer_matricula(self):
        print(f'O aluno {self.nome} acabou de se matricular')


class Professor(Pessoa):# Professor herda da Superclasse Pessoa
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel


    def dar_aula(self):
        print(f'O Professor {self.nome} começou a aula\n[purple]RYOUKI TENKAI![/]')


class Funcionario(Pessoa):# Funcionario herda da Superclasse Pessoa
    def __init__(self,nome,idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor


    def bater_ponto(self):
        print(f'O funcionário {self.nome} acabou de bater o ponto e está muito'
              'bravo, pois é segunda feira ')

a1 = Aluno(nome = 'Rian', idade = 23, curso = 'ADS', turma = 'D6')
a1.fazer_aniversario()
inspect(a1, methods = True)

p1 = Professor(nome = 'Satoru Gojo', idade = 28, especialidade = 'O Ilimitado', nivel = 'Especial')
p1.fazer_aniversario()
inspect(p1, methods = True)
p1.dar_aula()

f1 = Funcionario(nome = 'TonhãoCaminhão', idade = 43, cargo = 'Motorista', setor = 'Entrega')
f1.bater_ponto()
inspect(f1, methods = True)