
"""
Lista de Exercícios – Revisão em Python — Soluções

"""

from __future__ import annotations
from collections import Counter
from math import isqrt
from pathlib import Path
from typing import List, Dict
import random
import json
import re


# 1) Número perfeito -----------------------------------------------------------
def is_perfect(n: int) -> bool:
    """Retorna True se n é um número perfeito, False caso contrário.
    Número perfeito: soma dos divisores próprios (exceto ele mesmo) é igual ao número.
    Ex.: 6 -> True (1 + 2 + 3 = 6)"""
    if n <= 1:
        return False
    soma = 1  # 1 sempre é divisor próprio de n>1
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            soma += d
            q = n // d
            if q != d and q != n:
                soma += q
    return soma == n


# 2) Contar palavras -----------------------------------------------------------
def count_words(text: str) -> Dict[str, int]:
    """Conta as palavras do texto, ignorando maiúsculas/minúsculas.
    Retorna um dicionário {palavra: contagem}."""
    tokens = re.findall(r"\w+", text.lower(), flags=re.UNICODE)
    return dict(Counter(tokens))


# 3) Primos entre dois inteiros -----------------------------------------------
def is_prime(n: int) -> bool:
    """Testa primalidade de forma eficiente para inteiros não muito grandes."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    limite = isqrt(n)
    for d in range(3, limite + 1, 2):
        if n % d == 0:
            return False
    return True


def primes_between(a: int, b: int) -> List[int]:
    """Retorna todos os números primos no intervalo fechado [min(a,b), max(a,b)]."""
    if a > b:
        a, b = b, a
    return [x for x in range(max(2, a), b + 1) if is_prime(x)]


# 4) Fatorial recursivo --------------------------------------------------------
def factorial_recursive(n: int) -> int:
    """Calcula o fatorial de n recursivamente (n >= 0)."""
    if n < 0:
        raise ValueError("n deve ser não-negativo")
    if n in (0, 1):
        return 1
    return n * factorial_recursive(n - 1)


# 5) Estatísticas de arquivo .txt ---------------------------------------------
def count_file_stats(path: str | Path) -> Dict[str, int]:
    """Conta linhas, palavras e caracteres de um arquivo texto (UTF-8)."""
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    linhas = text.splitlines()
    palavras = re.findall(r"\w+", text, flags=re.UNICODE)
    return {"linhas": len(linhas), "palavras": len(palavras), "caracteres": len(text)}


# 6) Palíndromo ----------------------------------------------------------------
def is_palindrome(s: str) -> bool:
    """Verifica se a string é um palíndromo (ignora espaços, pontuação e caso)."""
    normalizada = re.sub(r"[^0-9A-Za-zÀ-ÖØ-öø-ÿ]", "", s, flags=re.UNICODE).casefold()
    return normalizada == normalizada[::-1]


# 7) N primeiros termos de Fibonacci ------------------------------------------
def fibonacci_n_terms(n: int) -> List[int]:
    """Retorna os n primeiros termos da sequência de Fibonacci (n >= 0)."""
    if n < 0:
        raise ValueError("n deve ser >= 0")
    seq: List[int] = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq


# 8) Sorteio de nome -----------------------------------------------------------
def draw_random_name(names: List[str]) -> str:
    """Sorteia aleatoriamente um nome da lista (não vazia)."""
    if not names:
        raise ValueError("lista de nomes vazia")
    return random.choice(names)


# 9/10) CRUD de contatos (com persistência em arquivo) ------------------------
class ContactBook:
    """CRUD simples de contatos, com persistência opcional em arquivo JSON."""

    def __init__(self, filepath: str | Path | None = None):
        self._contacts: Dict[str, str] = {}
        self.filepath = Path(filepath) if filepath else None
        if self.filepath:
            self.load()

    # operações CRUD
    def add(self, name: str, phone: str) -> None:
        if name in self._contacts:
            raise ValueError("Contato já existe")
        self._contacts[name] = phone
        self.save()

    def remove(self, name: str) -> None:
        if name not in self._contacts:
            raise KeyError("Contato não encontrado")
        del self._contacts[name]
        self.save()

    def update(self, name: str, phone: str) -> None:
        if name not in self._contacts:
            raise KeyError("Contato não encontrado")
        self._contacts[name] = phone
        self.save()

    def list(self) -> Dict[str, str]:
        return dict(self._contacts)

    # Persistência
    def load(self) -> None:
        if not self.filepath:
            return
        if self.filepath.exists():
            raw = self.filepath.read_text(encoding="utf-8").strip()
            data = json.loads(raw) if raw else {}
            if not isinstance(data, dict):
                raise ValueError("Arquivo de contatos inválido")
            self._contacts = {str(k): str(v) for k, v in data.items()}

    def save(self) -> None:
        if not self.filepath:
            return
        self.filepath.parent.mkdir(parents=True, exist_ok=True)
        self.filepath.write_text(
            json.dumps(self._contacts, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )


def run_contact_cli(persist_path: str | Path | None = None) -> None:
    """Interface de linha de comando simples para o CRUD de contatos.
    Se persist_path for fornecido, os dados serão salvos em JSON."""
    book = ContactBook(persist_path)
    menu = (
        "\n=== Contatos ===\n"
        "[1] Adicionar\n[2] Remover\n[3] Atualizar\n[4] Listar\n[0] Sair\nEscolha: "
    )
    while True:
        try:
            op = input(menu).strip()
            if op == "1":
                nome = input("Nome: ").strip()
                fone = input("Telefone: ").strip()
                book.add(nome, fone)
                print("Contato adicionado.")
            elif op == "2":
                nome = input("Nome: ").strip()
                book.remove(nome)
                print("Contato removido.")
            elif op == "3":
                nome = input("Nome: ").strip()
                fone = input("Novo telefone: ").strip()
                book.update(nome, fone)
                print("Contato atualizado.")
            elif op == "4":
                contatos = book.list()
                if not contatos:
                    print("(vazio)")
                else:
                    for n, t in contatos.items():
                        print(f"- {n}: {t}")
            elif op == "0":
                print("Até mais!")
                break
            else:
                print("Opção inválida.")
        except Exception as e:
            print("Erro:", e)


if __name__ == "__main__":
    # Exemplos rápidos (descomente para testar no terminal):
    # print("6 é perfeito?", is_perfect(6))
    # print("Contagem de palavras:", count_words("Oi oi, tudo bem? Bem, bem!"))
    # print("Primos entre 10 e 30:", primes_between(10, 30))
    # print("Fatorial de 5:", factorial_recursive(5))
    # print(count_file_stats("exemplo.txt"))
    # print("radar é palíndromo?", is_palindrome("radar"))
    # print("Fibonacci(10):", fibonacci_n_terms(10))
    # print("Sorteado:", draw_random_name(["Ana", "Bia", "Caio"]))
    # Para o CRUD com arquivo local (exercícios 9/10):
    # run_contact_cli("contatos.json")
    pass
