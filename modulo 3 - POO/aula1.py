# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))


class Pessoa:
    def __init__(self, nome, sobrenome) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
    def greeting(self):
        print(f'Olá eu sou {self.nome} {self.sobrenome}, muito prazer!')
   
p1 = Pessoa('Mario', 'Alberto')
p1.greeting()





# Atributos 
class Car: 
    ano_atual = 2024

    def __init__(self, marca,modelo) -> None:
        self.modelo = modelo
        self.marca = marca

uninho_de_firma = Car("Fiat", 'Uno')

print(f'{uninho_de_firma.modelo} {uninho_de_firma.marca}')