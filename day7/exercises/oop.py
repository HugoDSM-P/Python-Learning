class Character:
    pass
harry_potter = Character()

class Dinosaur:
    pass
velociraptor = Dinosaur()
trex = Dinosaur()

class Cube:
    faces = 6
    def __init__(self, colour):
        self.colour = colour
red_cube = Cube("red")

class Character:
    real = False
    def __init__(self, specie, magic, age):
        self.specie = specie
        self.magic = magic
        self.age = age
harry_potter = Character("Human", "True", 17)

class Mage:
    def throw_spell(self):
        print("¡Fireball!")
        
merlin = Mage()
merlin.throw_spell()

class Mascota:
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")

class Player:
    alive = False   
    @classmethod
    def revive(cls):
        cls.alive = True

class Archer:
    def __init__(self, arrow_count):
        self.arrow_count = arrow_count
    def throw_arrow(self):
        self.arrow_count = self.arrow_count-1
    
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Student(Person):
    pass

class Pet:
    def __init__(self, age, name, paws):
        self.age = age
        self.name = name
        self.paws = paws
class Dog(Mascota):
    pass

class Vehicle:
    def accelerate(self):
        pass
    def brake(self):
        pass
class Car(Vehicle):
    pass

class Vertebrate:
    vertebrate = True
class Bird(Vertebrate):
    has_beak = True
    def lay_eggs(self):
        print("Laying eggs")
class Reptil(Vertebrate):
    venomous = True
class Fish(Vertebrate):
    def swim(self):
        print("Swimming")
    def lay_eggs(self):
        print("Laying eggs")
class Mammal(Vertebrate):
    def walk(self):
        print("Walking")
class Platypus(Mammal, Fish, Reptil, Bird):
    pass

class Book():
    def __init__(self, title, autor, pages):
        self.title = title
        self.autor = autor
        self.pages = pages
    def __len__(self):
        return self.pages
    
class Book2():
    def __init__(self, title, autor, pages):
        self.title = title
        self.autor = autor
        self.pages = pages

    def __del__(self):
        print(f"Book deleted")