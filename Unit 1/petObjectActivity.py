# Create a pet animal class function
# The class should have 4 properties and 4 methods.
# Then create 3 pets objects. Each pet should have unique
# properties and use it at least 1 method.

class pet:
    def __init__(self,color, mood, name, age, type):
        pass
        self.color = color
        self.mood = mood
        self.name = name
        self.age = age
        self.type = type

    def feedPet(self):
        print("time to feed your pet")

    def sleeping(self):
        print("our pet is resting.")

    def playtime(self):
        print("our pet wants to play a game.")

    def bathroom():
        print("needs to relieve itself")

pet_1 = pet("brown", "Happy", "Nova", "5","dog" )
pet_2 = pet("blue", "Angry", "Sam", "3", "cat")
pet_3 = pet("green","Sad", "Lily", "8", "lizard" )

pet_1.feedPet()