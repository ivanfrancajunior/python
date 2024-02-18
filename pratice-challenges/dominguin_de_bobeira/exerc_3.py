'''
Create a class Smoothie and do the following:

Create an instance attribute called ingredients.

Create a get_cost method which calculates the total cost of the ingredients used to make the smoothie.

Create a get_price method which returns the number from get_cost plus the number from get_cost multiplied by 1.5. Round to two decimal places.

Create a get_name method which gets the ingredients and puts them in alphabetical order into a nice descriptive sentence. If there are multiple ingredients, add the word "Fusion" to the end but otherwise, add "Smoothie". Remember to change "-berries" to "-berry". See the examples below.


Crie um Smoothie de classe e faça o seguinte:

Crie um atributo de instância chamado ingredientes.

Crie um método get_cost que calcule o custo total dos ingredientes usados para fazer o smoothie.

Crie um método get_price que retorne o número de get_cost mais o número de get_cost multiplicado por 1,5. Arredonde para duas casas decimais.

Crie um método get_name que obtenha os ingredientes e os coloque em ordem alfabética em uma frase descritiva agradável. 

Se houver vários ingredientes, adicione a palavra "Fusion" ao final, mas, caso contrário, adicione "Smoothie". Lembre-se de trocar "-berries" por "-berry". Veja os exemplos abaixo.


    Ingredient	Price

Strawberries        $1.50
Banana	            $0.50
Mango	            $2.50
Blueberries	        $1.00
Raspberries	        $1.00
Apple	            $1.75
Pineapple	        $3.50

link: https://edabit.com/challenge/yuPWwSbCGPm2KzSzx
'''

class Smoothie():
    prices = {
	"Strawberries" : "$1.50",
	"Banana" : "$0.50",
	"Mango" : "$2.50",
	"Blueberries" : "$1.00",
	"Raspberries" : "$1.00",
	"Apple" : "$1.75",
	"Pineapple" : "$3.50"
}
    def __init__(self, ingredients: list) -> None:
        self.ingredients = ingredients
    
    def get_cost(self) -> float:
        
        price = 0
        
        for item in self.flavor_list:

            if  item["name"] == self.ingredients:
            
                price = item['price']
        
        return price

        


    def smootie_price(self,*args):

        if len([*args]) < 1: 
            return 'No ingredients added.'
        
        return round(self.get_cost([*args]) * 1.5,2)
    
    def get_name(self,ingredient:str | list[str] )-> float:
        
        if not ingredient: 
            return 'Empty list.'

        if isinstance(ingredient, str):
            return f'{ingredient} Smoothie.'

        if isinstance(ingredient,list) and len(ingredient) > 1:

            for item in ingredient:
                
                if 'berrie' in item:
                  
                  item_name = item.replace('berries','berry')

            return f'{item_name}' + 'Fusion'

s1 = Smoothie(["Banana"])

print(s1.ingredients)
print(s1.get_cost())

# class Smoothie:
# 	def __init__(self, ingredients):
# 		self.ingredients= ingredients
	
# 	def get_cost(self):
# 		cost = 0
# 		for item in self.ingredients:
# 			cost+=float(prices[item][1:])
# 		return "${}".format(format(round(cost,2),'.2f'))
		
# 	def get_price(self):
# 		return "${}".format(format(round(float(self.get_cost()[1:])+float(self.get_cost()[1:])*1.5,2),'.2f'))
	
# 	def get_name(self):
# 		ingredients = self.ingredients.copy()
# 		ingredients.sort()
# 		for ind,item in enumerate(ingredients):
# 			ingredients[ind] = item.replace("berries" , "berry")
# 		if len(ingredients)>1:
# 			ingredients.append('Fusion')
# 		else:
# 			return "{} Smoothie".format(ingredients[0])
# 		string = ' '.join(ingredients)
# 		return string
# s1 = Smoothie(["Banana"])

# print(s1.ingredients)
# print(s1.get_price())