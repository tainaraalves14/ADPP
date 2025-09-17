#Implemente um sistema de transporte em Python utilizando classes abstratas:

#Crie uma classe abstrata Transporte com um atributo capacidade, 
# um método abstrato mover() 
# e um método concreto info() que exibe a capacidade.
#Crie duas subclasses:
# Carro, que imprime "O carro está se movendo com até X passageiros".
# Bicicleta, que imprime "A bicicleta está se movendo com até X pessoas".
# No programa principal, crie objetos das duas subclasses, adicione-os em uma lista 
# e invoque mover() e info() para cada um.



from abc import ABC, abstractmethod
#classe abstrata é uma classe que não pode ser instanciada diretamente,
# mas serve como base para outras classes.
#abstractmethod é um decorador que marca um método como abstrato, ou seja,
# obrigatório de ser implementado pelas subclasses.
#A ideia é criar uma estrutura base (como um "molde") que obriga outras classes a implementarem certos métodos.
# transporte.py

class Transporte(ABC):
    def __init__(self, capacidade: int):
        # validações básicas: inteiro e não-negativo
        if not isinstance(capacidade, int):
            raise TypeError("capacidade deve ser um inteiro")
        if capacidade < 0:
            raise ValueError("capacidade não pode ser negativa")
        self.capacidade = capacidade

    @abstractmethod
    def mover(self) -> str:
        """subclasses precisam implementar e retornar uma string descrevendo o movimento"""
        pass

    def info(self) -> str:
        """método concreto que exibe (retorna) a capacidade"""
        return f"Capacidade: {self.capacidade}"

class Carro(Transporte):
    def mover(self) -> str:
        return f"O carro está se movendo com até {self.capacidade} passageiros"

class Bicicleta(Transporte):
    def mover(self) -> str:
        return f"A bicicleta está se movendo com até {self.capacidade} pessoas"

# demonstração simples — só roda se executarmos este arquivo diretamente
if __name__ == "__main__":
    lista = [Carro(5), Bicicleta(1)]
    for t in lista:
        print(t.mover())   # chama mover() (que retorna string)
        print(t.info())    # chama info() (que retorna string)
        print("-" * 30)
  

#-----------------------------------------------------------------------------------------


#Utilizando o sistema de transporte do Exercício 1, crie testes unitários em Python com pytest:

#Teste se um objeto Carro(5) possui capacidade igual a 5.
# Teste se o método mover() de Carro retorna a string correta.
# Teste se o método mover() de Bicicleta retorna a string correta.
# Crie também um teste de falha proposital para verificar se a criação 
# de um Carro com capacidade negativa (Carro(-3)) gera um erro ou comportamento esperado.

# tests/test_transporte.py
import pytest
from transporte import Carro, Bicicleta

def test_carro_capacidade():
    c = Carro(5)
    assert c.capacidade == 5

def test_carro_mover_retorna_string_correta():
    assert Carro(5).mover() == "O carro está se movendo com até 5 passageiros"

def test_bicicleta_mover_retorna_string_correta():
    assert Bicicleta(2).mover() == "A bicicleta está se movendo com até 2 pessoas"

def test_carro_com_capacidade_negativa_deve_levantar_erro():
    with pytest.raises(ValueError):
        Carro(-3)


#-----------------------------------------------------------------------------------------


#Crie um decorator em Python chamado valida_positivo que verifica se todos os argumentos 
# numéricos de uma função são positivos:

#Se todos os argumentos forem válidos, a função deve ser executada normalmente.
#Se algum argumento for negativo, deve ser levantado um ValueError.
#Use esse decorator em pelo menos duas funções:
#raiz_quadrada(x), que retorna a raiz quadrada de x.
# divisao(a, b), que retorna o resultado de a / b.
# Teste chamando as funções com valores positivos (funciona normalmente) 
# e valores negativos (gera erro).

from functools import wraps
from numbers import Real
import math

def valida_positivo(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # verifica argumentos posicionais
        for idx, a in enumerate(args):
            # consideramos números reais (int/float), ignoramos booleans
            if isinstance(a, Real) and not isinstance(a, bool) and a < 0:
                raise ValueError(f"Argumento posicional #{idx} ({a}) é negativo")
        # verifica argumentos nomeados
        for k, v in kwargs.items():
            if isinstance(v, Real) and not isinstance(v, bool) and v < 0:
                raise ValueError(f"Argumento '{k}' ({v}) é negativo")
        return func(*args, **kwargs)
    return wrapper

@valida_positivo
def raiz_quadrada(x):
    """retorna sqrt(x). assume x >= 0 (decorator garante que x não seja negativo)."""
    return math.sqrt(x)

@valida_positivo
def divisao(a, b):
    """retorna a / b. decorator garante a e b não-negativos (mas divisão por zero ainda precisa ser tratada)."""
    if b == 0:
        raise ZeroDivisionError("divisão por zero")
    return a / b

# demonstração
if __name__ == "__main__":
    print("raiz_quadrada(9) ->", raiz_quadrada(9))
    print("divisao(10, 2) ->", divisao(10, 2))
    try:
        raiz_quadrada(-1)
    except ValueError as e:
        print("Erro esperado:", e)
    try:
        divisao(5, -2)
    except ValueError as e:
        print("Erro esperado:", e)


#-----------------------------------------------------------------------------------------

#Dicas Importantes:
#Classes abstratas (ABC): serve para garantir que as subclasses implementem métodos essenciais (mover aqui). 
# Retornar vs imprimir: retornamos strings em mover() — isso facilita testar. 
# Em programas reais, muitas vezes você retorna dados e só imprime no __main__ ou na camada de apresentação.
# Validação no __init__: validar logo na construção do objeto evita objetos em estado inválido (por exemplo, capacidade negativa).
# Use functools.wraps para manter nome e docstring da função original.
# Decida claramente o que o decorator verifica (aqui: números reais; zero=permitido).
# Teste com positionais e keywords. Testes: prefira testar comportamento (o que a função retorna) e também os erros esperados (pytest.raises).