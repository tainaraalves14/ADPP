import unittest
from src.carrinho import Carrinho, Item


class TestCarrinho(unittest.TestCase):
    def setUp(self):
        self.carrinho = Carrinho()

    def test_adicionar_item(self):
        item = Item("Caneta", 2.5, 4)
        self.carrinho.adicionar(item)
        self.assertEqual(len(self.carrinho.itens), 1)

    def test_total(self):
        self.carrinho.adicionar(Item("Lápis", 1.5, 3))
        self.carrinho.adicionar(Item("Borracha", 0.5, 2))
        self.assertEqual(self.carrinho.total(), 5.5)


if __name__ == "__main__":
    unittest.main()
