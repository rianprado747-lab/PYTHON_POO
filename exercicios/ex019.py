from rich import print
import time
'''
Crie uma classe livro, que vai simular a passagem de páginas de um livro, considerando também se o usuário chegou ao fim
da leitura.
'''
class Livro :
    def __init__(self,livro, paginas):
        self.livro = livro
        self.paginas = paginas
        self.paginas_livro = 1

        print(f':open_book: [blue]Você acabou de abrir  o livro [red]{self.livro}[/]',
              f'[blue]que tem [green]{self.paginas} páginas[/] no total. Agora você está na[/]',
              f'[yellow]página {self.paginas_livro}[/]'
              )

    def avancar_pagina(self, qtd = 1):
        c = 0
        for pg in range(0, qtd, 1):
            if not self.fim_livro() :
                self.paginas_livro += 1
                print(f'[yellow] Pág {self.paginas_livro} :arrow_forward:[/]', end = '')
                time.sleep(0.2)
                c += 1
        print(f'[blue] Você avançou {c} páginas e agora você está na página {self.paginas_livro}[/]')
        if self.fim_livro():
            print(f':closed_book: [red]Você cheogou ao final do livro {self.livro}.[/]')

    def fim_livro(self) -> boll :
        return True if self.paginas_livro == self.paginas else False


l1 = Livro ('A magia de Avalon', 20)
l1.avancar_pagina(5)
l1.avancar_pagina(10)
l1.avancar_pagina(50)
