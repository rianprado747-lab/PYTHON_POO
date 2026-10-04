'''
Crie a classe ControleRemoto, onde vamos simular o funcionamento de um controle simples(canal,volume e liga/desliga).
'''
from rich import print
from rich.panel import Panel
class Controle_remoto:
    canal_min:int = 1
    canal_max:int = 6
    volume_min:int = 1
    volume_max:int = 5

    def __init__(self, canal = 1, volume = 2):
        self.canal_atual:int = canal
        self.volume_atual:int = volume
        self.ligado:bool = False


    def mostrar_tv(self):
        conteudo = ''
        if not self.ligado:
            conteudo = f':prohibited: [red]TV está desligada[/]'
        else:
            conteudo = 'CANAL  = '
            for c in range(Controle_remoto.canal_min, Controle_remoto.canal_max + 1):
                if c == self.canal_atual:
                    conteudo += f' [black on yellow] {c} [/] '
                else:
                    conteudo += f' {c} '

        conteudo += f'\nVOLUME = '
        for v in range(Controle_remoto.volume_min, Controle_remoto.volume_max+1):
            if v <= self.volume_atual:
                conteudo  += '[black on cyan] [/]'
            else :
                conteudo +='[black on white] [/]'


        tv = Panel(conteudo, title='[ TV ]', width=40)
        print(tv)


    def liga_desliga(self):
        self.ligado = not self.ligado


    def canal_mais(self):
        if self.ligado:
            if self.canal_atual == Controle_remoto.canal_max:
                self.canal_atual = Controle_remoto.canal_min
            else:
                self.canal_atual += 1

    def canal_menos(self):
        if self.ligado:
            if self.canal_atual == Controle_remoto.canal_min:
                self.canal_atual = Controle_remoto.canal_max
            else:
                self.canal_atual -= 1

    def volume_mais(self):
        if self.ligado:
            if self.volume_atual != Controle_remoto.volume_max:
                self.volume_atual += 1


    def volume_menos(self):
        if self.ligado:
            if self.volume_atual != Controle_remoto.volume_min:
                self.volume_atual -= 1


c = Controle_remoto()
while True:
    c.mostrar_tv()
    comando = str(input(f'\n < CH{c.canal_atual} >  - VOL{c.volume_atual} + '))
    match comando:
        case '0':
            break
        case '@':
            c.liga_desliga()
        case '<':
            c.canal_menos()
        case '>':
            c.canal_mais()
        case '-':
            c.volume_menos()
        case '+':
            c.volume_mais()
    print('\n' * 10)
