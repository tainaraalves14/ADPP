import unittest
from src.conta import Conta


class TestConta(unittest.TestCase):
    def setUp(self):
        self.conta = Conta("001", "Maria")

    def test_deposito_valido(self):
        self.conta.depositar(200)
        self.assertEqual(self.conta.saldo, 200)

    def test_saque_valido(self):
        self.conta.depositar(150)
        self.conta.sacar(50)
        self.assertEqual(self.conta.saldo, 100)

    def test_saque_invalido(self):
        self.conta.depositar(50)
        self.conta.sacar(100)  # Deve ser ignorado
        self.assertEqual(self.conta.saldo, 50)

    def test_extrato(self):
        self.conta.depositar(100)
        self.assertIn("Saldo: R$100.00", self.conta.extrato())


if __name__ == "__main__":
    unittest.main()
