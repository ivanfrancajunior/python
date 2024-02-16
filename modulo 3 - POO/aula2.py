# Métodos + factories

class Monstro:
    def __init__(self,nome:str ) -> None:
        self.nome = nome

   
    def gritar(self) ->None:
        print(f'{self.nome} está rugindo!!!')

    def correr():
        print('Montro começa a correr!')

    @classmethod
    def rugir(cls):
        print('Grrrrr!')

    @classmethod
    def perseguir(cls):
        return cls.correr()

bixo = Monstro('Bixo')
bixo.gritar()

Monstro.rugir()
Monstro.perseguir()