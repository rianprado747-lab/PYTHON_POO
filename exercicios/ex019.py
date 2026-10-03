'''
Crie uma classe livro, que vai simular a passagem de páginas de um livro, considerando também se o usuário chegou ao fim
da leitura.
'''
class Livro :
    def __init__(self,titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas

    def avancar_paginas(self,n):
        total_paginas = n
        if n < self.paginas :
            total_paginas += n
            print(f'vocâ está na página {total_paginas}')

        if total_paginas == self.paginas :
            print(f'Você chegou ao final do livro')

l1 = Livro('10 coisas que eu aprendi', 20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(5)
l1.avancar_paginas(3)
