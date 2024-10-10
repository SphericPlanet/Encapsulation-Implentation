class Computer:
    #class variable
    #make it private using __
    __max_price = 1000

    #getter method
    def get_max_price(self):
        return self.__max_price
    
    #setter method
    def set_max_price(self, price):
        self.__max_price = price


comp = Computer()
print(comp.get_max_price())
#price is now 900
comp.set_max_price(900)
print(comp.get_max_price())