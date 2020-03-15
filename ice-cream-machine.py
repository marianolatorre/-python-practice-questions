"""
10 min
Implement the IceCreamMachine's scoops method so that it returns all
combinations of one ingredient and one topping. If there are no ingredients or
toppings, the method should return an empty list.
For example,
IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"]).scoops()
should return
[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']].
    class IceCreamMachine:
        def __init__(self, ingredients, toppings):
            self.ingredients = ingredients
            self.toppings = toppings
        def scoops(self):
            pass
    machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
    print(machine.scoops()) #should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]
"""


class IceCreamMachine:
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings
    def scoops(self):
        product=[]
        for ingredient in self.ingredients:
            for topping in self.toppings:
                product.append([ingredient,topping])
        return product

print("first test")
machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
print(machine.scoops()) #should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]

print("second test")
machine = IceCreamMachine([], ["chocolate sauce"])
print(machine.scoops()) #should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]

print("second test")
machine = IceCreamMachine(["hello"], [])
print(machine.scoops()) #should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]
