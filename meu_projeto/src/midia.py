from datetime import datetime


class Midia:
    def __init__(self, titulo, ano):
        self.titulo = titulo
        self.ano = ano

    @property
    def idade(self):
        return datetime.now().year - self.ano


class Filme(Midia):
    def __init__(self, titulo, ano, duracao):
        super().__init__(titulo, ano)
        self.duracao = duracao


class Livro(Midia):
    def __init__(self, titulo, ano, paginas):
        super().__init__(titulo, ano)
        self.paginas = paginas
