import pytest
from exerc_1 import Player

# def dobble(value:float) -> int|float:
#     if not isinstance(value,int|float):
#         raise ValueError('the value must be a int or float type.')
    
#     return value * 2 

# def test_if_works(value=5):
    
#     result = dobble(5)
    
#     assert result == 10


def test_if_return_a_player_name():
    
    player =  Player("David Jones", 25, 175, 75)
    
    test = player.name
    
    assert test == "David Jones"

def test_if_change_a_player_name_correctly():
    
    player =  Player("David Jones", 25, 175, 75)
    
    player.name = 'Novo Nome'
    
    assert player.name == "Novo Nome"

def test_if_raises_an_error_with_wrong_type_value_of_name():
    
    player =  Player("Test  name", 25, 175, 75)
    
    with pytest.raises(TypeError):
        test = player.name = 1


def test_if_return_a_correct_string_in_the_get_age_method():
    
    player =  Player("David Jones", 25, 175, 75)
    
    test = player.get_age()
    
    assert test == "David Jones is age 25"


def test_if_return_a_correct_string_in_the_get_weight_method():    
    player =  Player("David Jones", 25, 175, 75)
    
    test = player.get_weight()
    
    assert test == "David Jones weighs 75kg"

def test_if_return_a_correct_string_in_the_get_heught_method():    
    player =  Player("David Jones", 25, 175, 75)
    
    test = player.get_height()
    
    assert test == "David Jones is 175cm"

