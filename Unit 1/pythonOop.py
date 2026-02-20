# OOP = Object Oreinted Programing

# An object is a blueprint for describing something.

# Computer Object Descriptors
# it can tell time
# it can access the internet/search up things
# there's a power button
# it has programs



# you can play games on it
# it has 

# Properties = the datattypes 

class ComputerItem:
    def _init_(self, color, shape, soundrOutput, brand, ram, price, storage ):
        self.color = color
        self.shape = shape
        self.soundOutput = soundrOutput
        self.brand = brand
        self.ram = ram
        self.price = price
        self.storage = storage
        self.processor = processor

    def repairServices(self):
         print('great which repair subscription do you want?')

    def warremty(self):
         print('Which insurance do you want?')

    def buyNowPayLater(self):
        print("how much do you want to pay")

msi_Computer = Computers("msi","MSI". "blue", 24, 2,False,False,16,7800)
msi_Computer.repairService

class Phones:
    def __init__(self, name, brand, color, shape, storage, portability, camera, ):

apple_1 = Computers("apple m4", "black", 10.00, 320, True, True, 120, 'm4')
apple_2 = Computers("apple m4", "white", 10.00, 320, True, True, 80, 'm4')