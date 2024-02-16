# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

from typing import Optional


class Motor: 
    def __init__(self, name:str) -> None:
        self.name = name
    
    def get_name(self):
        return self.name

class Fabricante: 
    def __init__(self, name) -> None:
        self.name = name

class Car: 
    def __init__(self, car_name:str, motor_name=None , label_name=None ) -> None:
        self.car_name = car_name
        self.motor_name = motor_name
        self.label_name = label_name

    @property
    def motor(self):
        if self.motor_name is not None:
            return self.motor_name.name
        else:
            return None

    @motor.setter
    def motor(self, name:str) -> str:
        self.motor_name = name

    @property
    def label(self):
        if self.label_name is not None:
            return self.label_name.name
        else:
            return None
    
    @label.setter
    def label(self, name:str) -> None:
        self.label_name = name


v8 = Motor('V6')
regular = Motor('1.6')
volkswagen = Fabricante('Volkswagen')
porche = Fabricante('Porche')

panamera = Car('Panamera')
gol = Car('Gol')

gol.motor = regular
gol.label = volkswagen
panamera.motor = v8
panamera.label = porche

print(panamera.motor)
print(panamera.label)

print(gol.motor)
print(gol.label)


