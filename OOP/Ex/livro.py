class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.paginas_restantes = paginas  #resultado da receita 

    def ler_paginas(self, n):
        if n <= 0:
            print("Número de páginas a ler deve ser maior que zero.")
            return

        if self.paginas_restantes == 0:
            print("O livro já foi completamente lido.")
            return

        if n >= self.paginas_restantes:
            print(f"Você leu as últimas {self.paginas_restantes} páginas.")
            self.paginas_restantes = 0
        else:
            self.paginas_rest_
