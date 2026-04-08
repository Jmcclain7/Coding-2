# In your unit 3 folder, create a new document called activityMar19.py Copy and paste the questions into your document and then
#  answer the following questions. You are permitted to use your notes, w3schools, and work together to answer the questions.
# do your best to complete all questions. This activity is due at the end of class.


# 1. In your own words, what is the difference between a python class and a python object?
# Please write your resonse as a string data type. 

# The difference between python class and a python object is that a class is a blueprint for creating objects.
# An object is an instance of a class that contains data. 

# 2. In your own words, what is a object property and and object method? Please
# write your response as a string data type.

# An object property is a variable that is attached to an object that holds data.
# An object method is a function attached to an object that performs an action.


# 3. Create a unique python class. Your class should have 5 properties and 3 mtethods. 
# each method should do one of the following; 
# 1 method must do some type of operation with data; an arithmetic, logical, or comparison operation
# 1 method must take in a parameter and do some operation on the parameter
# 1 method must do some type of conditional (if/else) logic. 



class VideoGameCharacter:
    def_init_(self,name,level,attack power,health):
    self.name = name
    self.level = level
    self.attack_power = attack_power
    self.health = health

    def calculate damage(self):
        damage = self.attack power & self.level
    
    def take damage(self, damage taken):
        self.health = damage taken 

    def check status(self):
        if self.health <= 0:
            self is alive = False
            self.name has been defeated.
        else:
            self.name is still alive with self.health