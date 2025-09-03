import unittest
from datetime import datetime
from src.midia import Livro, Filme


class TestMidia(unittest.TestCase):
    def test_idade_livro(self):
        ano_atual = datetime.now().year
        livro = Livro("Python 101", ano_atual - 5, 300)
        self.assertEqual(livro.idade, 5)

    def test_idade_filme(self):
        ano_atual = datetime.now().year
        filme = Filme("Matrix", ano_atual - 20, 136)
        self.assertEqual(filme.idade, 20)


if __name__ == "__main__":
    unittest.main()
