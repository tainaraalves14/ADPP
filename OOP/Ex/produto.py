# Produto em um sistema de estoque 
# ele recebe ------ adiciona ----- vende 

class Produto:
    def __init__(self, nome, preco, estoque)
        self.nome = nome
        self.preco = preco
        self.estoque = estoque 
    
    def adicionar_estoque (self, estoque)
        if quantidade > 0 
        self.estoque +- quantidade              #incremneta se a condição for verdadeira na quantidade 

    def vender (self, quantidade)              #desde que tenha estoque suficiente e a quantidade seja positiva
        if 0 < quantidade <= self.estoque:     # ( se zero é menor que quantidade, a quantidade necessariamente é maior que zero) 
            self.estoque -= quantidade         
            return True
        return False  
        
    def esta_disponivel(self):
        return self.estoque > 0
    

