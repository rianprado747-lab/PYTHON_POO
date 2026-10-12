from rich import print, inspect
from classes import Aluno, Professor, Funcionario, Pessoa

def main():
    a1 = Aluno(nome = 'Rian', idade = 23, curso = 'ADS', turma = 'D6')
    a1.fazer_aniversario()
    inspect(a1, methods = True)
    a1.estudar()

    p1 = Professor(nome = 'Satoru Gojo', idade = 28, especialidade = 'O Ilimitado', nivel = 'Especial')
    p1.fazer_aniversario()
    inspect(p1, methods = True)
    p1.dar_aula()
    p1.estudar()
    print()

    f1 = Funcionario(nome = 'TonhãoCaminhão', idade = 43, cargo = 'Motorista', setor = 'Entrega')
    f1.bater_ponto()
    f1.estudar()

if __name__ == '__main__':
    main()