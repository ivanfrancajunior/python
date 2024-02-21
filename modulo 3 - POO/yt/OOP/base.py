'''
 Definição de classes
 Atributos 
 Metodos
 Construtor 
 Herança e Polimorfismo
'''


class Pessoa(object):
    
    def __init__(self,nome,idade) -> None:
        self.nome = nome
        self.idade = idade
        
    def apresentar(self):
        return f'Olá eu sou {self.nome} e tenho {self.idade} anos.'
    

class Aluno(Pessoa):
    def __init__(self, nome, idade, escola) -> None:
        self.nome = nome
        self.idade = idade
        self.escola = escola
    
    def apresentar(self):
        return f'Oi eu sou {self.nome} e tenho {self.idade} anos e estudo na {self.escola}.' # override de metodo
class Professor(Pessoa):
    def __init__(self, nome, idade, escola) -> None:
        self.nome = nome
        self.idade = idade
        self.escola = escola
    
    def apresentar(self):
        return f'Prazer eu sou {self.nome} e tenho {self.idade} anos e trabalho na escola {self.escola}.' # override de metodo

p1 = Pessoa('Jose', 55, )
a1 = Aluno("Mario", 20,'ABC')
pr1 = Professor('Jose', 45, 'ABC')


print(p1.apresentar())
print(a1.apresentar())
print(pr1.apresentar())