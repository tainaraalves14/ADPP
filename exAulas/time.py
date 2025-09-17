import time

def funcao_1():
    inicio = time.time()
    time.sleep(5)
    fim = time.time() #simular alguma interação
    duracao = fim - inicio
    print(f"O tempo de execução é de: {duracao:.2f} segundos")

# Executa a função
funcao_1()


#-----------------------------------------------------------

##  O que é um *decorator* em Python? 
# Um **decorator** (ou decorador) é uma função que **modifica o comportamento de outra função**, sem alterá-la diretamente.

#Decorator = papel de presente + fita
#Um decorator é como você embrulhar essa caixa com um papel e uma fita, 
# que adicionam algo extra sem abrir a caixa ou mexer no que tem dentro.

def meu_decorator(func):
    def wrapper():
        print("Antes da função")
        func()
        print("Depois da função")
    return wrapper

@meu_decorator
def diga_ola():
    print("Olá!")

diga_ola()




## 🎯 Exemplo prático: medir tempo de execução com `time`

import time

def medir_tempo(func):
    def wrapper():
        inicio = time.time()
        func()
        fim = time.time()
        print(f"Tempo de execução: {fim - inicio:.2f} segundos")
    return wrapper

@medir_tempo
def tarefa_lenta():
    time.sleep(3)
    print("Tarefa concluída!")

tarefa_lenta()


##  Dica: usando `functools.wraps` (opcional, mas recomendado)
from functools import wraps

def meu_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper



#----------------------------------------------------------
#Classes abstratas 
from abc import ABC, abstractmethod
#ABC = Abstract Base Class (Classe Base Abstrata)
#abstractmethod = decorador que marca um método como abstrato, ou seja, 
# obrigatório de ser implementado pelas subclasses.

#A ideia é criar uma estrutura base (como um "molde") que obriga outras classes a implementarem certos métodos.
class FiguraGeometrica(ABC):

    @abstractmethod
    def area(self):
        pass    ## não implementa ainda, só diz "tem que ter esse método"

    @abstractmethod
    def perimetro(self):
        pass
#qualquer figura geométrica deve ter os métodos area() e perimetro()
#Toda figura geométrica tem que ter uma forma de calcular a área e o perímetro.

class Circulo(FiguraGeometrica):

    def __init__(self, raio):
        self.raio = raio
    
    def area(self):
        return 3.14 * (self.raio ** 2)

    def perimetro(self):
        return 2 * 3.14 * self.raio
    

circulo = Circulo(raio=10)
print(circulo.area())
print(circulo.perimetro())

#Se você tentar criar um círculo sem implementar os métodos area e perimetro, o Python vai reclamar.

import math

class Triangulo(FiguraGeometrica):
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def area(self):
        s = self.perimetro() / 2  # semi-perímetro  ( )
        # fórmula de Heron
        area = math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))
        return area


class Retangulo(FiguraGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)

        


#--------------------------------------------------------------------
from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def acelerar(self):
        pass

    @abstractmethod
    def frear(self):
        pass

class Carro(Veiculo):
    def acelerar(self):
        return "Carro acelerando"

    def frear(self):
        return "Carro freando"

carro = Carro()
print(carro.acelerar())
print(carro.frear())


#------------------------------------------------------------
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Au au!"

class Gato(Animal):
    def emitir_som(self):
        return "Miau!"

cachorro = Cachorro()
gato = Gato()

print(cachorro.emitir_som())  # Au au!
print(gato.emitir_som())       # Miau!
