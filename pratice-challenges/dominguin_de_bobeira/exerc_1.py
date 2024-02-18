'''
    # Classes For Fetching Information on a Sports Player

    Create a class that takes the following four arguments for a particular football player:

    name
    age
    height
    weight
    Also, create three functions for the class that returns the following strings:

    get_age() returns "name is age age"
    get_height() returns "name is heightcm"
    get_weight() returns "name weighs weightkg"
'''

class Player:
    def __init__(self, name:str, age:int, height:float, weight:float) -> None:
        self._name = name
        self._age=age
        self._height=height
        self._weight = weight

    @property
    def name(self):
        
        return self._name
        
    @name.setter
    def name(self, name:str)->str:
        if not isinstance (name,str):
            raise TypeError('This field must be a string')
        self._name = name
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age:int)->int:
        if not isinstance (age,int):
                raise TypeError('This field must be a integer value')
        self._age = age
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, height:float|int)->float|int:
        if not isinstance (height,int) or isinstance (height,float):
            raise TypeError('This field must be a integer float or integer.')
        self._height = height
    
    @property
    def weight(self):
        return self._weight
    
    @weight.setter
    def weight(self, weight:float|int)->float|int:
        
        if not isinstance (weight,float) or not isinstance(weight, int):
                raise TypeError('This field must be a integer float or integer.')
        self._weight = weight

    def get_age(self) -> str:
        return f'{self._name} is age {self._age}'
    
    def get_height(self) -> str:
        return f'{self._name} is {self._height}cm'
    
    def get_weight(self) -> str:
        return f'{self._name} weighs {self._weight}kg'

first =  Player("David Jones", 25, 175, 75)
        

print(first.name,
first.age,
first.weight,
first.height, sep='\n')

print(first.get_age(),
first.get_weight(),
first.get_height(), sep='\n')



