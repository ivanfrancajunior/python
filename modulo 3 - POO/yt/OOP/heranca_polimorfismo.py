""" 
   Em resumo, na herança simples em Python, uma classe pode estender o 
   comportamento de outra classe, adicionando novos métodos ou atributos, 
   ou sobrescrevendo os métodos existentes, sem modificar diretamente 
   a classe base. Isso promove a organização e a modularidade do código, 
   facilitando a manutenção e a extensibilidade do sistema. 
"""


class ClasseGenerica(object):

    def __init__(self, nome:str) -> None:
        self.nome = nome

    def falar_nome(self):
        print(f'{self.nome} - {self.__class__.__name__}')

class ClasseHerdeira(ClasseGenerica):
    pass

gen = ClasseGenerica('Generica')
her = ClasseHerdeira('Herdeira')

gen.falar_nome()

her.falar_nome()

# help(ClasseGenerica)

'''
sobreposição de métodos (override method): 

 A sobreposição de métodos permite que uma classe substitua o comportamento de um
 método da classe pai, fornecendo sua própria implementação. Isso é útil quando 
 você deseja que uma classe filha tenha um comportamento específico para um 
 método, adaptado às suas próprias necessidades, sem modificar diretamente a 
 classe pai.

'''

class HerdeiraDiferente(ClasseGenerica):
    
    def falar_nome(self):
        print(f'[METODO ALTERADO]: {self.nome} - {self.__class__.__name__}')

her_diff = HerdeiraDiferente('Herdeira Diferente')

her_diff.falar_nome()

'''
    O método super() em Python é uma função especial que é usada dentro de uma 
    classe para acessar métodos e atributos da classe pai (superclasse). 
    Ele é frequentemente usado em métodos de uma classe filha para chamar a 
    implementação da mesma função na classe pai, permitindo estender ou 
    modificar o comportamento sem duplicar código.

'''

class Animal(object):
    def fazer_som(self):
        print(f"{self.__class__.__name__} fazendo som")


class Cachorro(Animal):
    
    def fazer_som(self):
        super().fazer_som()


class Gato(Animal):
    
    def fazer_som(self):
        super(Gato,self).fazer_som() # os parametros são implicitos


print('\n','USANDO SUPER:', '\n')

bixo = Animal()
dog = Cachorro()
cat = Gato()

bixo.fazer_som()
dog.fazer_som()
cat.fazer_som()


'''
    Herança múltipla:

    Na herança múltipla, uma classe filha pode herdar atributos e métodos de 
    várias classes mães. Isso é feito listando as classes pai separadas por 
    vírgula na definição da classe filha. Quando métodos ou atributos são 
    chamados em uma instância da classe filha, o Python procura em cada classe 
    pai, seguindo uma ordem específica chamada de ordem de resolução de métodos 
    (MRO), para encontrar a implementação desejada.


    mro method: 

    O método mro() (Method Resolution Order) em Python é uma função que retorna 
    a ordem de resolução de métodos para uma classe. Essa ordem indica a 
    sequência na qual as classes são pesquisadas para encontrar métodos durante 
    a resolução de métodos em herança múltipla.

'''

class Pai:
    def metodo_pai(self):
        print("Método do Pai1")

class Mae:
    def metodo_mae(self):
        print("Método do Pai2")

class Filha(Pai, Mae):
    
    def metodo_pai(self):
        return super().metodo_pai()
    
    def metodo_mae(self):
        return super().metodo_mae()

obj = Filha()
obj.metodo_pai()  # Saída: Método do Pai1
obj.metodo_mae()  # Saída: Método do Pai2

print(Filha.mro()) 
#output:  [<class '__main__.Filha'>, <class '__main__.Pai'>, <class '__main__.Mae'>, <class 'object'>]

'''
Mixins:

    Os Mixins são classes que fornecem funcionalidades específicas e podem ser 
    combinadas com outras classes através da herança múltipla. Eles são úteis para 
    adicionar comportamentos especializados a uma classe sem criar uma relação de 
    herança direta. Os mixins geralmente contêm métodos ou atributos que são 
    compartilhados entre várias classes que possuem características comuns, 
    permitindo assim a reutilização de código e a promoção da modularidade e da 
    coesão do código.



    Vamos considerar um exemplo com um mixin relacionado a um objeto do dia a dia,
     como um dispositivo eletrônico, como um smartphone.

    Digamos que queremos criar um mixin para adicionar funcionalidades de 
    conectividade Bluetooth a diferentes tipos de dispositivos eletrônicos, 
    como smartphones, fones de ouvido sem fio, etc. Podemos criar um mixin 
    chamado BluetoothMixin que fornece métodos para conectar e desconectar 
    dispositivos via Bluetooth.

'''

class AbstractBluetoothMixin:
    def conectar_bluetooth(self, dispositivo):
        print(f"Conectando ao dispositivo via Bluetooth: {dispositivo}")

    def desconectar_bluetooth(self, dispositivo):
        print(f"Desconectando do dispositivo via Bluetooth: {dispositivo}")

class Smartphone:
    def fazer_ligacao(self, numero):
        print(f"Fazendo ligação para o número: {numero}")

    def enviar_mensagem(self, mensagem):
        print(f"Enviando mensagem: {mensagem}")

class FoneDeOuvido:
    def reproduzir_musica(self, musica):
        print(f"Reproduzindo música: {musica}")

class SmartphoneComBluetoothMx(Smartphone, AbstractBluetoothMixin):
    pass

class FoneDeOuvidoComBluetoothMx(FoneDeOuvido, AbstractBluetoothMixin):
    pass

# Exemplo de uso

smartphone = SmartphoneComBluetoothMx()
smartphone.conectar_bluetooth("Fone de Ouvido Bluetooth")
smartphone.fazer_ligacao("123456789")
smartphone.desconectar_bluetooth("Fone de Ouvido Bluetooth")

fone_de_ouvido = FoneDeOuvidoComBluetoothMx()
fone_de_ouvido.conectar_bluetooth("Smartphone")
fone_de_ouvido.reproduzir_musica("Playlist Favorita")
fone_de_ouvido.desconectar_bluetooth("Smartphone")


'''
    CLASSES E MÉTODOS ABSTRATOS:

    uma classe abstrata é uma classe que não pode ser instanciada diretamente e 
    é projetada para ser uma classe base para outras classes. Ela geralmente 
    contém métodos abstratos, que são métodos sem implementação definida na 
    classe abstrata.

    Resumidamente, classes abstratas em Python servem como esqueletos para outras
      classes, fornecendo uma estrutura comum e definindo métodos que devem ser 
      implementados pelas subclasses.

    Os métodos abstratos são definidos usando o módulo abc (Abstract Base Classes)
      e são marcados com o decorador @abstractmethod. Eles precisam ser 
      implementados nas subclasses para que estas possam ser instanciadas 
      corretamente e só possuem a assinatura destes métodos.

    Em essência, classes e métodos abstratos em Python são utilizados para 
    definir uma estrutura comum e garantir que as subclasses implementem 
    certos comportamentos obrigatórios, promovendo a coesão e a reutilização 
    de código.
    
'''

from abc import ABC, abstractmethod
from typing import Any

class AbstractBluetoothMixin(ABC):
    @abstractmethod
    def conectar_bluetooth(self, dispositivo: str) -> None: ...

    @abstractmethod
    def desconectar_bluetooth(self, dispositivo: str) -> None: ... 

class Smartphone(ABC):
    def fazer_ligacao(self, numero:int):
        print(f"Fazendo ligação para o número: {numero}")

    def enviar_mensagem(self, mensagem):
        print(f"Enviando mensagem: {mensagem}")

class FoneDeOuvido(ABC):
    def reproduzir_musica(self, musica:str):
        print(f"Reproduzindo música: {musica}")

class SmartphoneComBluetoothMx(Smartphone, AbstractBluetoothMixin):
    def conectar_bluetooth(self, dispositivo):
        print(f"Conectando ao dispositivo via Bluetooth: {dispositivo}")

    def desconectar_bluetooth(self, dispositivo):
        print(f"Desconectando do dispositivo via Bluetooth: {dispositivo}")

class FoneDeOuvidoComBluetoothMx(FoneDeOuvido, AbstractBluetoothMixin):
    def conectar_bluetooth(self, dispositivo):
        print(f"Conectando ao dispositivo via Bluetooth: {dispositivo}")

    def desconectar_bluetooth(self, dispositivo):
        print(f"Desconectando do dispositivo via Bluetooth: {dispositivo}")

# Exemplo de uso
smartphone = SmartphoneComBluetoothMx()
smartphone.conectar_bluetooth("Fone de Ouvido Bluetooth")
smartphone.fazer_ligacao("123456789")
smartphone.desconectar_bluetooth("Fone de Ouvido Bluetooth")

fone_de_ouvido = FoneDeOuvidoComBluetoothMx()
fone_de_ouvido.conectar_bluetooth("Smartphone")
fone_de_ouvido.reproduzir_musica("Playlist Favorita")
fone_de_ouvido.desconectar_bluetooth("Smartphone")

'''
    Criando Exceções em Python

    Exceções próprias em Python são classes que representam erros específicos ou excepcionais que podem ocorrer durante a execução de um programa. Essas classes são geralmente definidas pelo desenvolvedor para lidar com situações específicas e podem ser personalizadas para incluir informações adicionais sobre o erro.

    São geralmente definidas como subclasses da classe base Exception ou de suas subclasses mais específicas, como RuntimeError ou ValueError. Isso permite que as exceções próprias herdem comportamentos e métodos dessas classes base, facilitando a captura e o tratamento de erros de maneira consistente.

'''

class MinhaExcecao(Exception):
    def __init__(self, mensagem):
        self.mensagem = mensagem
        super().__init__(mensagem)

    def __str__(self):
        return f"Minha Exceção: {self.mensagem}"

def verificar_numero(numero):
    if numero < 0:
        raise MinhaExcecao("O número não pode ser negativo.")

try:
    numero = -5
    verificar_numero(numero)
except MinhaExcecao as e:
    print(e)

'''
    Métodos especiais ou 'dunder methods'

    Os métodos especiais, também conhecidos como "dunder methods" 
    (abreviação de "double underscore methods"), são métodos em Python que têm 
    um duplo sublinhado (__) no início e no final de seus nomes. Eles são 
    chamados automaticamente pelo interpretador em situações específicas e são 
    usados para definir comportamentos especiais em objetos.

    # __repr__ : 

        É um dos métodos especiais mais comuns e é usado para retornar uma 
        representação oficial do objeto em forma de string. Essa representação 
        deve ser uma expressão Python válida que, quando avaliada, produzirá um 
        objeto com o mesmo estado. O objetivo principal do __repr__ é fornecer 
        uma representação útil para debugging e para interação 
        com o interpretador Python.
    
    # __str__: 

        É usado para retornar uma representação mais amigável do objeto em forma
          de string. Ele é chamado quando o objeto é convertido explicitamente 
          em uma string, geralmente por meio da função str(), ou quando é usado 
          em funções de formatação de string, como print(). O __str__ é usado 
          para criar uma representação legível do objeto 
          para os usuários do programa.
'''

class Geolocalizacao:
    def __init__(self, latitude:float, longitude:float) -> None:
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return f'Ponto(x={self.latitude}, y={self.longitude})'

    def __str__(self):
        return f'({self.latitude}, {self.longitude})'

# Exemplo de uso
loc = Geolocalizacao(335353.75, 4112212122.1)

print(repr(loc))  # Chama __repr__
print(str(loc))   # Chama __str__

''' TODO: __new__ '''


'''  __call__ 

    O método __call__ permite que objetos de uma classe se comportem como funções, possibilitando a execução de código específico quando são chamados. Isso oferece uma maneira poderosa de adicionar comportamentos dinâmicos a objetos em Python.
    
    ** Faz uma instância de uma classe ser callable
'''

class Call:
    def __init__(self, phone) -> None:
        self.phone = phone

call = Call(5551234)

# call() -> ❌ TypeError: 'CallMe' object is not callable.


class CallMe:
    def __init__(self, phone) -> None:
        self.phone = phone

    def __call__(self) -> None:
        print(f'Chamando {self.phone}')

call911 = CallMe(911)
call911()

''' TODO: context manegers com classes '''

'''
    Funções declaradoras com classes: 

    Funções decoradoras de classes oferecem uma maneira elegante de adicionar 
    funcionalidades, modificar comportamentos ou realizar ações adicionais em 
    classes sem alterar diretamente o código fonte da classe. Isso promove a 
    reutilização de código, modularidade e flexibilidade na extensão de classes 
    em Python.

'''

def meu_decorador_de_classe(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'

    return class_repr

def adicionar_repr(cls):
    cls.__repr__ = meu_decorador_de_classe

    return cls

@adicionar_repr
class Time:
    def __init__(self, nome:str) -> None:
        self.nome = nome

amr = Time('America')

@adicionar_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome

terra = Planeta('Terra')

print(amr)
print(terra)


''' Classes Decoradoras 

    Uma classe decoradora em Python oferece uma maneira flexível de adicionar funcionalidades ou modificar o comportamento de outras classes, encapsulando-as em uma nova classe decoradora. Isso promove a reutilização de código e a modularidade, facilitando a extensão de classes de forma organizada e elegante.
'''

class Multiplicar:
    def __init__(self,multiplicador:int) -> None:
        self.multiplicador = multiplicador


    def __call__(self, fn):
        
        def handle(*args:int|float,**kwargs:int | float) -> int|float:
            
            resultado = fn(*args,**kwargs)

            return resultado * self.multiplicador
        
        return handle

@Multiplicar(2)
def soma(x,y):
    return x + y


oito = soma(2,2)
print(oito)


''' Metaclasses'''



''' DocStrings

    Docstrings são cadeias de caracteres (strings) que fornecem documentação sobre o propósito, funcionamento e uso de funções, métodos, classes ou módulos em Python. Elas são colocadas no início de um bloco de código e são delimitadas por três aspas duplas (""").

    Resumidamente, as docstrings são usadas para documentar o código, fornecendo informações úteis para quem estiver lendo ou utilizando o código. Elas são uma parte importante da prática de programação Python, pois ajudam a entender rapidamente o propósito e o uso de diferentes partes do código.
'''

class Retangulo:
    """
    Classe para representar um retângulo.

    Atributos:
    largura (float): Largura do retângulo.
    altura (float): Altura do retângulo.
    """

    def __init__(self, largura, altura):
        """
        Inicializa um objeto Retangulo com a largura e altura especificadas.

        Parâmetros:
        largura (float): A largura do retângulo.
        altura (float): A altura do retângulo.
        """
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        """
        Calcula a área do retângulo.

        Retorna:
        float: A área do retângulo.
        """
        return self.largura * self.altura

    def calcular_perimetro(self):
        """
        Calcula o perímetro do retângulo.

        Retorna:
        float: O perímetro do retângulo.
        """
        return 2 * (self.largura + self.altura)


'''Enuns'''