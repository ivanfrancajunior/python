import pytest
from exerc_2 import Employee


def test_if_have_a_valid_name_value():
    person = Employee("Mary", "Sue", 60000)

    assert person.firstname == 'Mary'

def test_if_raises_an_error_when_pass_a_wrong_firstname_type():

    person = Employee("Mary", "Sue", 60000)
    
    with pytest.raises(TypeError):
         person.firstname = 1

def test_if_raises_an_error_when_pass_a_wrong_lastname_type():

    person = Employee("Mary", "Sue", 60000)
    
    with pytest.raises(TypeError):
         person.lastname = 1


def test_if_the_correct_value_is_apply_using_a_class_method():
    molly = Employee()

    molly.from_string('Molly-Sunny-50000')

    assert molly.firstname == 'Molly'

    assert molly.lastname == 'Sunny'

    assert molly.salary == 50000

def test_if_the_correctly_type_was_been_apply_to_salary():

    molly = Employee()

    molly.from_string('Molly-Sunny-50000')

    salary = molly.salary

    assert isinstance(salary, int)