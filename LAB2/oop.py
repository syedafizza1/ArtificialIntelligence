"""Exercise 1: Write a class of Dog, each dog must be of species type mammal. Each dog has its name
and age. The class can have method for description () and sound () which dog produces. Create an
object and perform some operations. """

class Dog:
 # Class Attribute
 species = 'mammal'
 # Initializer / Instance Attributes
 def __init__(self, name, age):
     self.name = name
     self.age = age
 # instance method
 def description(self):
     return "{} is {} years old".format(self.name, self.age)
 # instance method
 def speak(self, sound):
     return "{} says {}".format(self.name, sound)
# Instantiate the Dog object
razer = Dog("Razer", 6)
# call our instance methods
print(razer.description())
print(razer.speak("Woof Woof"))

"""Exercise 2: Write a class of Dog, each dog must be of species type mammal. Each dog has its name 
and age. The class can have method for description () and sound () which dog produces. Now this 
time you need to create two sub classes of Dogs one is Bull Dog and other is Russell Terrier Create 
few objects and perform some operations including the inheritance. """

# Parent class
class Dog:
 # Class attribute
 species = 'mammal'
 # Initializer / Instance attributes
 def __init__(self, name, age):
     self.name = name
     self.age = age
 # instance method
 def description(self):
     return "{} is {} years old".format(self.name, self.age)
 # instance method
 def speak(self, sound):
     return "{} says {}".format(self.name, sound)
# Child class (inherits from Dog class)
class RussellTerrier(Dog):
 def run(self, speed):
     return "{} runs {}".format(self.name, speed)
# Child class (inherits from Dog class)
class Bulldog(Dog):
 def run(self, speed):
     return "{} runs {}".format(self.name, speed)

# Child classes inherit attributes and
# behaviors from the parent class
thunder = Bulldog("Thunder", 9)
print(thunder.description())
# Child classes have specific attributes
# and behaviors as well
print(thunder.run("slowly"))
spinter = Bulldog("Spinter", 12)
print(spinter.description())
print(spinter.run("fast"))
roger = RussellTerrier("Roger", 5)


"""Exercise 3: Extending question number 2, now we need to check that either the different dog 
classes and their objects link with each other or not. In this case we need to create a method to
find either it’s an instance of each other objects or not. """

# Parent class
class Dog:
 # Class attribute
 species = 'mammal'
 # Initializer / Instance attributes
 def __init__(self, name, age):
     self.name = name
     self.age = age
 # instance method
 def description(self):
     return "{} is {} years old".format(self.name, self.age)
 # instance method
 def speak(self, sound):
     return "{} says {}".format(self.name, sound)
# Child class (inherits from Dog() class)
class RussellTerrier(Dog):
 def run(self, speed):
     return "{} runs {}".format(self.name, speed)
# Child class (inherits from Dog() class)
class Bulldog(Dog):
 def run(self, speed):
     return "{} runs {}".format(self.name, speed)
# Child classes inherit attributes and
# behaviors from the parent class
thunder = Bulldog("Thunder", 9)
print(thunder.description())
# Child classes have specific attributes
# and behaviors as well
print(thunder.run("slowly"))
# Is thunder an instance of Dog()?
print(isinstance(thunder, Dog))
# Is thunder_kid an instance of Dog()?
thunder_kid = Dog("ThunderKid", 2)
print(isinstance(thunder, Dog))
# Is Kate an instance of Bulldog()
Kate = RussellTerrier("Kate", 4)
print(isinstance(Kate, Dog))
# Is thunder_kid and instance of kate?
#print(isinstance(thunder_kid,Kate))
print("Thanks for understanding the concept of OOPs")
