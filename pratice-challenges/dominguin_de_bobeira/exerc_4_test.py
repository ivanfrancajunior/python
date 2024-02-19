import pytest
from exerc_4 import CoffeeShop

def test_should_return_a_error_message_if_item_not_been_in_menu():

    acs = CoffeeShop('Alissa CoffeeShop')

    feat_test = acs.add_order('hot cocoa')

    assert feat_test == 'This item is currently unavailable!'

def test_should_return_a_cofirmation_message_if_the_item_has_in_menu():

    acs = CoffeeShop('Alissa CoffeeShop',[{'name':'ice tea',"type":'drink', 'price':10}])

    feat_test = acs.add_order('ice tea')
    print(feat_test)
    
    assert feat_test == "Order added!"

def test_if_the_order_list_isnt_empty():
    
    acs = CoffeeShop('Alissa CoffeeShop',[{'name':'ice tea',"type":'drink', 'price':10}],['ice tea'] )

    acs.add_order('ice tea')
    
    assert len(acs.orders) == 2

def test_if_display_the_correct_message_when_fullfill_the_order():

    acs = CoffeeShop('Alissa CoffeeShop',[{'name':'ice tea',"type":'drink', 'price':10}],['ice tea'] ) 

    feat_test = acs.fulfill_order('ice tea')

    assert feat_test == 'The ice tea is ready!'
def test_if_a_item_was_correctly_removed_to_the_order_list():

    acs = CoffeeShop('Alissa CoffeeShop',[{'name':'ice tea',"type":'drink', 'price':10}],['ice tea'] ) 

    acs.fulfill_order('ice tea')

    assert len(acs.orders) == 0

def test_if_display_the_correct_message_when_fullfill_the_item_erong_name():

    acs = CoffeeShop('Alissa CoffeeShop',[{'name':'ice tea',"type":'drink', 'price':10}],['ice tea'] ) 

    feat_test = acs.fulfill_order('orange juice')

    assert feat_test == 'The current item isnt in the order list.'

def test_if_display_a_order_list():
    acs = CoffeeShop(
        'Alissa CoffeeShop',[
        {'name':'ice tea',"type":'drink', 'price':10}, {'name':'coffee',"type":'drink', 'price':3.0}
        ],[
            {'name': 'ice tea', 'type': 'drink', 'price': 10},{'name':'coffee',"type":'drink', 'price':3.0}
            ] 
            ) 

    feat_test = acs.list_orders()

    assert feat_test == [{'name': 'ice tea', 'type': 'drink', 'price': 10}, {'name':'coffee',"type":'drink', 'price':3.0}]
def test_if_the_list_of_orders_start_empty():
    acs = CoffeeShop('Alissa CoffeeShop',[{'name':'ice tea',"type":'drink', 'price':10}, {'name':'coffee',"type":'drink', 'price':3.0}] ) 

    feat_test = acs.list_orders()

    assert feat_test == acs.orders

def test_if_returns_a_correct_amount_value():
    acs = CoffeeShop('Alissa CoffeeShop',[{'name':'ice tea',"type":'drink', 'price':10}, {'name':'coffee',"type":'drink', 'price':3.0}],[{'name':'ice tea',"type":'drink', 'price':10}, {'name':'coffee',"type":'drink', 'price':3.0}] )

    test_case = acs.due_amount()

    assert test_case == 13.0

def test_if_a_0_will_return_when_no_items_in_the_order_list():
    acs = CoffeeShop('Alissa CoffeeShop',[{'name':'ice tea',"type":'drink', 'price':10}, {'name':'coffee',"type":'drink', 'price':3.0}],[] )

    test_case = acs.due_amount()
    
    assert float(test_case) == 0.0 

def test_if_return_the_cheap_item_correctly():

    acs = CoffeeShop('Alissa CoffeeShop',[{'name':'ice tea',"type":'drink', 'price':10}, {'name':'coffee',"type":'drink', 'price':3.0}] )

    test_case = acs.cheapest_item()

    assert test_case == [{'name':'coffee',"type":'drink', 'price':3.0}]

def test_if_only_drink_types_will_be_return():

    acs = CoffeeShop('Alissa CoffeeShop',[{'name':'ice tea',"type":'drink', 'price':10}, {'name':'coffee',"type":'drink', 'price':3.0}, {'name':'pizza',"type":'food', 'price':3.0}, {'name':'hamburger',"type":'food', 'price':3.0},{'name':'coffee',"type":'anything', 'price':3.0}] )

    test_case = acs.drinks_only()

    assert test_case == [{'name': 'ice tea', 'type': 'drink', 'price': 10}, {'name': 'coffee', 'type': 'drink', 'price': 3.0}]


def test_if_only_food_types_will_be_return():

    acs = CoffeeShop('Alissa CoffeeShop',[{'name':'ice tea',"type":'drink', 'price':10}, {'name':'coffee',"type":'drink', 'price':3.0}, {'name':'pizza',"type":'food', 'price':3.0}, {'name':'hamburger',"type":'food', 'price':3.0},{'name':'coffee',"type":'anything', 'price':3.0}] )

    test_case = acs.food_only()

    assert test_case == [{'name': 'pizza', 'type': 'food', 'price': 3.0}, {'name': 'hamburger', 'type': 'food', 'price': 3.0}]


# acs = CoffeeShop('Alissa CoffeeShop',[{'name':'ice tea',"type":'drink', 'price':10}, {'name':'coffee',"type":'drink', 'price':3.0}, {'name':'pizza',"type":'food', 'price':3.0}, {'name':'hamburger',"type":'food', 'price':3.0},{'name':'coffee',"type":'anything', 'price':3.0}], [])

# feat_test = acs.add_order('ice tea')
# feat_test = acs.add_order('coffee')
# # feat_test = acs.due_amount()
# count = acs.due_amount()
# print(acs.list_orders())
# print(feat_test)
# print(len(acs.menu))
# print('here drinks-> ', acs.drinks_only())
# print('here food-> ', acs.food_only())
# print(count)






