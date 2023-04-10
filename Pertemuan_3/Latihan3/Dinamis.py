class Animal:
    def make_sound(self):
        print("The animal makes a sound")
class Goat(Animal):
    def make_sound(self):
        print("The goat mbeee")
class Chicken(Animal):
    def make_sound(self):
        print("The chicken crowed")
class Chihuahua():
    def make_sound(self):
        print("The chihuahua yaps")
class Sheep(Goat):
    def make_sound(self):
        print("The Sheep mbee")
def animal_sound(animal):
        animal.make_sound()
# Instantiate objects of each class
animal = Animal()
goat = Goat()
chicken = Chicken()
chihuahua = Chihuahua()
sheep = Sheep()
# Call the animal_sound function for each object
animal_sound(animal) # Output: The animal makes a sound
animal_sound(goat) # Output: The goat mbeee
animal_sound(chicken) # Output: The chicken crowed 
animal_sound(chihuahua) # Output: The chihuahua yaps
animal_sound(sheep) # Output: The Sheep mbee