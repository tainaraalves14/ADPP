# 

class aluno: 
    def __init__(self, nome)
        self.nome = nome 
        self.notas = [] 
    
    def adicionar_nota (self, nota)
        # # nota deve estar entre 0 e 10 (inclusive)      
        if 0 >= nota <= 10                                  #maior ou = a 0 menor ou igual a 10 
            self.notas.append(nota)                         #append adiconar elemento ao final de uma lista 

    def media ( self)
        if not self.notas:                                  #Se não tem nenhuma nota (lista vazia), retorna 0
            return 0 
        return sum(self.notas) / len ( self.notas)          # função sum() soma todos os números  
        #A função len() retorna a quantidade de elementos da lista
        #Aqui você pega o total das notas somadas e divide pelo número de notas
    
    def aprovado(self):
        return self.media() >= 7  