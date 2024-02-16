class Pessoa():
    def __init__(self, nome:str, idade:int, cpf:str) -> None:
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf

    def get_cpf(self)-> str:
        return self.__cpf
    def __apresentar_documento(self)-> str:
        return self.__cpf
    def pode_beber(self)->bool:
        if self.idade < 18 and self.__apresentar_documento() != '':
            return True

p1 = Pessoa('LALALA', 10, '134546')
print(p1.get_cpf())
print(p1.pode_beber())
# print(p1.__apresentar_documento()) ❌ 
# print(p1.__cpf) ❌
