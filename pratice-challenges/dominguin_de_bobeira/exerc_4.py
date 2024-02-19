'''
Coffee Shop

Write a class called CoffeeShop, which has three instance variables:

    name : a string (basically, of the shop)

    menu : a list of items (of dict type), with each item containing the item (name of the item), type (whether a food or a drink) and price.

    orders : an empty list

    and seven methods:

    ✔ add_order: adds the name of the item to the end of the orders list if it exists on the menu, otherwise, return "This item is currently unavailable!"

    ✔ fulfill_order: if the orders list is not empty, return "The {item} is ready!". If the orders list is empty, return "All orders have been fulfilled!"

    ✔ list_orders: returns the item names of the orders taken, otherwise, an empty list.

    ✔ due_amount: returns the total amount due for the orders taken.

    ✔ cheapest_item: returns the name of the cheapest item on the menu.

    ✔ drinks_only: returns only the item names of type drink from the menu.
    
    ✔ food_only: returns only the item names of type food from the menu.

    ======================== EXEMPLES: 

    tcs.add_order("hot cocoa") ➞ "This item is currently unavailable!"
    # Tesha's coffee shop does not sell hot cocoa
    
    tcs.add_order("iced tea") ➞ "This item is currently unavailable!"
    # specifying the variant of "iced tea" will help the process

    tcs.add_order("cinnamon roll") ➞  "Order added!"
    tcs.add_order("iced coffee") ➞ "Order added!"
    tcs.list_orders ➞ ["cinnamon roll", "iced coffee"]
    # all items of the current order

    tcs.due_amount() ➞ 2.17

    tcs.fulfill_order() ➞ "The cinnamon roll is ready!"
    tcs.fulfill_order() ➞ "The iced coffee is ready!"
    tcs.fulfill_order() ➞ "All orders have been fulfilled!"
    # all orders have been presumably served

    tcs.list_orders() ➞ []
    # an empty list is returned if all orders have been exhausted

    tcs.due_amount() ➞ 0.0
    # no new orders taken, expect a zero payable

    tcs.cheapest_item() ➞ "lemonade"
    tcs.drinks_only() ➞ ["orange juice", "lemonade", "cranberry juice", "pineapple juice", "lemon iced tea", "vanilla chai latte", "hot chocolate", "iced coffee"]
    tcs.food_only() ➞ ["tuna sandwich", "ham and cheese sandwich", "bacon and egg", "steak", "hamburger", "cinnamon roll"]

    ===========================================

    link: https://edabit.com/challenge/PYEuCAdGJsRS9AABA
'''
item = {'name':'item name',"type":'item type', 'price':'item price'}

class CoffeeShop:
    
    def __init__(self, name:str, menu:list[dict]={},orders:list=[]) -> None:
        self.name = name
        self.menu = menu
        self.orders = orders
  
    def add_order(self, item:str):
        
        for menu_item in self.menu:
            if menu_item['name'] == item:
                self.orders.append(menu_item)
            
            return "Order added!"        
        
        return "This item is currently unavailable!"

    def fulfill_order(self, item:str):

        if len(self.orders) > 1 :
            return "All orders have been fulfilled!"
        
        if self.orders[len(self.orders)-1] == item:
        
            self.orders.pop()
        
            return f"The {item} is ready!"

        return f'The current item isnt in the order list.'

    def list_orders(self):
        
        if len(self.orders) > 0:
            
            return self.orders
        
        return self.orders

    def due_amount(self):
        
        total_amount = 0
        
        if len(self.orders) > 0:
            for item in self.orders:
                
                total_amount += item['price']
            
            return total_amount
            
        return total_amount

    def cheapest_item(self):

        cheapest_item  = None
        
        if len(self.menu) > 0:
            
            cheapest_item = self.menu[0]
            
            for item in self.menu:

             if cheapest_item["price"] > item['price']:
            
                cheapest_item = [item]   
            
            return cheapest_item

        return cheapest_item   
    def drinks_only(self ) -> list:
        
        searh_list = []
        
        if len(self.menu) < 0:
            return f'tá bobo?'

        for item in self.menu:
        
            if item['type'] == 'drink':
                
                searh_list.append(item)
        
        return searh_list           
    def food_only(self) -> list:
        
        searh_list = []
        
        if len(self.menu) < 0:
            return f'tá bobo?'

        for item in self.menu:
        
            if item['type'] == 'food':
                
                searh_list.append(item)
        
        return searh_list        
