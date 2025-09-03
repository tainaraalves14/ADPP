class Item:
    def __init__(self, nome, preco, qtd):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd

    def total(self):
        return self.preco * self.qtd


class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar(self, item: Item):
        self.itens.append(item)

    def total(self):
        return sum(item.total() for item in self.itens)
