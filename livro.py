class Livro:
    def __init__(self, título, autor, num_paginas):
        self.titulo = título
        self.autor = autor
        self.num_paginas = num_paginas
    def mostrar_informacoes(self):
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Número de páginas:", self.num_paginas)

    def calcular_palavra_por_pagina(self, total_palavras):
        if self.num_paginas == 0:
            return 0
        else:
            return total_palavras / self.num_paginas

livro_exemplo = Livro("Dom Casmurro", "Machado de Assis", 256)
livro_exemplo.mostrar_informacoes()
total_palavras = 64000 
palavras_por_pagina = livro_exemplo.calcular_palavras_por_pagina(total_palavras)
print("Quantidade de palavras por página:", palavras_por_pagina)
