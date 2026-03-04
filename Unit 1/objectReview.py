#1
"Class properties are variables that belong  to a class store information about an object created from that specific class"

#3
"A class method is a function inside a class that defines actions"

#3
class Student:
    def __init__ (self, name, age, grade, uniform):
        self.name = name
        self.age = age
        self.grade = grade 
        self.uniform = uniform 

    def study(self):
        "James is studying."

    def take_test(self):
        "James is taking a test"

    def is_In_Uniform(self):
        if self.uniform == False:
            print("this student has detention")
        else:
            print("student is good. no detention.")

    def study(self,subject):
        print(self.name + "is studying for" + subject)

    def updateGrade(self, testScore):
        average = 95
        testScore += average
        average  /= 5
        print(average)

student1 = Student(15, 10, 'John', True)
student2 = Student(17, 11, 'Rick', False)

student1.is_In_Uniform()
student2.updateGrade(70)


#4

class VGC:
    def __init__(self, name, health, archetype, ammo, power,shootingPercent):
        self.name = name
        self.health = health
        self.archetype = archetype
        self.power = power 
        self.ammo = ammo
        self.shootingPercent = shootingPercent


    # method FPS games
    def fireWeapon(self, weapon):
        if self,ammo
    # method Fighting games
    def block(self, damage):
        damage = 0
        return damage

    def normalAttack(self, hitConnects, opponent):
        if hitConnects:
            opponent.health -= self.power


    # method (Any) Sports games 
    def shooting_2pt(self, shootingPercent):
