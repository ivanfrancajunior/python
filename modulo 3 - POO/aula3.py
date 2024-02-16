# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código

class Caneta:
    def __init__(self, cor="Azul", tipo_escrita= 'Esferografica'):
        self.__cor_tinta = cor
        self.tipo_escrita = tipo_escrita

    @property
    def cor(self):
        print('ESTOU NO GETTER')
        return self.__cor_tinta
    
    @cor.setter
    def cor(self, valor: str) -> None:
        print('ESTOU NO SETTER')
        self.__cor_tinta = valor

    
    @property
    def tipo (self) -> str :
        return self.tipo_escrita
###########################


caneta = Caneta()

print(caneta.cor)
caneta.cor = 'Laranja'
print(caneta.cor)
print(caneta.tipo)
