'''
Crie a classe Gamer, onde podemos cadastrar nome, nick e os jogos favoritos de uma pessoa. Crie também um método que
permita mostrar a ficha desse gamer.
'''
from rich import print
from rich.panel import Panel
from rich import inspect

class Gamer :
    def __init__(self,nome, nickname,*jg_favorito):
        self.nome = nome
        self.nick = nickname
        self.jogo = jg_favorito
        print(f'O jogo favorito do {self.nome} é {self.jogo} e seu nickname é {self.nick}')

    def ficha(self):
        conteudo = (f'Nome real : [black on white] {self.nome} [/],'
                    f'\nJogos Favoritos:\n[blue]:video_game: {'\n:video_game: '.join(sorted(self.jogo))}[/]')
        painel = Panel(conteudo, title =f'[yellow]Jogador {self.nick}[/]',width=50,)
        print(painel)

g1=Gamer('Rian','Godefroy','Elden Ring','Terraria','Dark Souls','Sekiro')
g1.ficha()

g2=Gamer('Ramon', 'Law','Fortnite', 'Warzone')
g2.ficha()

