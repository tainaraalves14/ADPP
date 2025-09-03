import unittest
from datetime import datetime


# ----------------------------
# Nível 1 – Fundamentos da OOP
# ----------------------------

# 1. Conta Bancária
class Conta:
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor

    def extrato(self):
        return f"Conta {self.numero} - Saldo: R${self.saldo:.2f}"


# 2. Carrinho de Compras
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


# 3. Biblioteca de Mídias
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


# 4. Agenda de Contatos
class Contato:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def __eq__(self, other):
        return isinstance(other, Contato) and self.email == other.email

    def __hash__(self):
        return hash(self.email)


# 5. Conversor de Unidades
class Conversor:
    @staticmethod
    def celsius_para_fahrenheit(c):
        return (c * 9/5) + 32

    @staticmethod
    def fahrenheit_para_celsius(f):
        return (f - 32) * 5/9


# ----------------------------
# Nível 2 – Herança e Polimorfismo
# ----------------------------

# 6. Folha de Pagamento
class Funcionario:
    def pagar(self):
        raise NotImplementedError()


class CLT(Funcionario):
    def __init__(self, salario):
        self.salario = salario

    def pagar(self):
        return self.salario


class PJ(Funcionario):
    def __init__(self, horas, valor_hora):
        self.horas = horas
        self.valor_hora = valor_hora

    def pagar(self):
        return self.horas * self.valor_hora


# 7. Formas Geométricas
class Forma:
    def area(self):
        raise NotImplementedError()


class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        from math import pi
        return pi * self.raio ** 2


class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura


def soma_areas(formas):
    return sum(forma.area() for forma in formas)


# 8. Sistema de Arquivos
class Arquivo:
    def __init__(self, tamanho):
        self._tamanho = tamanho

    def tamanho_total(self):
        return self._tamanho


class Pasta:
    def __init__(self):
        self.itens = []

    def adicionar(self, item):
        self.itens.append(item)

    def tamanho_total(self):
        return sum(item.tamanho_total() for item in self.itens)


# ----------------------------
# Nível 3 – Projetos Integradores
# ----------------------------

# 9. Marketplace
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class Estoque:
    def __init__(self):
        self.produtos = {}

    def adicionar(self, produto: Produto, quantidade):
        self.produtos[produto] = self.produtos.get(produto, 0) + quantidade

    def remover(self, produto: Produto, quantidade):
        if self.produtos.get(produto, 0) >= quantidade:
            self.produtos[produto] -= quantidade
            return True
        return False


class ItemPedido:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def subtotal(self):
        return self.produto.preco * self.quantidade


class Pedido:
    def __init__(self, itens):
        self.itens = itens

    def total(self):
        return sum(item.subtotal() for item in self.itens)


class Pagamento:
    def __init__(self, pedido):
        self.pedido = pedido

    def processar(self, estoque: Estoque):
        for item in self.pedido.itens:
            if not estoque.remover(item.produto, item.quantidade):
                return False
        return True


# 10. Motor de Fluxo de Chatbot
class No:
    def executar(self, contexto):
        raise NotImplementedError()


class Mensagem(No):
    def __init__(self, texto):
        self.texto = texto

    def executar(self, contexto):
        contexto.append(f"Mensagem: {self.texto}")


class Pergunta(No):
    def __init__(self, texto):
        self.texto = texto

    def executar(self, contexto):
        contexto.append(f"Pergunta: {self.texto}")


class Condicao(No):
    def __init__(self, condicao, no_verdadeiro, no_falso):
        self.condicao = condicao
        self.no_verdadeiro = no_verdadeiro
        self.no_falso = no_falso

    def executar(self, contexto):
        if self.condicao():
            self.no_verdadeiro.executar(contexto)
        else:
            self.no_falso.executar(contexto)


# 11. Sistema de Reserva de Salas
class Sala:
    def __init__(self, capacidade):
        self.capacidade = capacidade


class Reserva:
    def __init__(self, sala, inicio, fim):
        self.sala = sala
        self.inicio = inicio
        self.fim = fim


class Agenda:
    def __init__(self):
        self.reservas = []

    def reservar(self, nova: Reserva):
        for reserva in self.reservas:
            if reserva.sala == nova.sala and not (nova.fim <= reserva.inicio or nova.inicio >= reserva.fim):
                return False
        self.reservas.append(nova)
        return True


# ----------------------------
# Testes Unitários
# ----------------------------

class TestesPIM(unittest.TestCase):

    def test_conta(self):
        c = Conta("123", "João")
        c.depositar(100)
        c.sacar(50)
        self.assertEqual(c.saldo, 50)

    def test_carrinho(self):
        carrinho = Carrinho()
        carrinho.adicionar(Item("Caneta", 2, 3))
        self.assertEqual(carrinho.total(), 6)

    def test_midia(self):
        livro = Livro("Python", 2020, 300)
        self.assertTrue(livro.idade >= 0)

    def test_contato(self):
        a = Contato("Ana", "ana@mail.com")
        b = Contato("Ana2", "ana@mail.com")
        self.assertEqual(a, b)

    def test_conversor(self):
        self.assertAlmostEqual(Conversor.celsius_para_fahrenheit(0), 32)
        self.assertAlmostEqual(Conversor.fahrenheit_para_celsius(32), 0)

    def test_folha_pagamento(self):
        c = CLT(3000)
        p = PJ(100, 50)
        self.assertEqual(c.pagar(), 3000)
        self.assertEqual(p.pagar(), 5000)

    def test_formas(self):
        formas = [Retangulo(2, 3), Circulo(1)]
        self.assertTrue(soma_areas(formas) > 0)

    def test_arquivo_pasta(self):
        arq = Arquivo(100)
        pasta = Pasta()
        pasta.adicionar(arq)
        self.assertEqual(pasta.t
