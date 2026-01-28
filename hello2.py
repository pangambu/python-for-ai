# Basic Inheritance Example

# Parent class (Base class)
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def eat(self):
        print(f"{self.name} is eating.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")
    
    def make_sound(self):
        print(f"{self.name} makes a sound.")


# Child class (Derived class) - inherits from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        # Call parent class constructor
        super().__init__(name, "Canine")
        self.breed = breed
    
    # Override parent method
    def make_sound(self):
        print(f"{self.name} barks: Woof! Woof!")
    
    # Add new method specific to Dog
    def fetch(self):
        print(f"{self.name} is fetching the ball!")


# Another child class
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Feline")
        self.color = color
    
    # Override parent method
    def make_sound(self):
        print(f"{self.name} meows: Meow!")
    
    # Add new method specific to Cat
    def climb(self):
        print(f"{self.name} is climbing a tree!")


# Create instances and demonstrate inheritance
print("=== Dog Example ===")
jerry = Dog("Jerry", "Golden Retriever")
print(f"Name: {jerry.name}")
print(f"Species: {jerry.species}")
print(f"Breed: {jerry.breed}")

# Methods from parent class
jerry.eat()
jerry.sleep()

# Overridden method
jerry.make_sound()

# Dog-specific method
jerry.fetch()

print("\n=== Cat Example ===")
whiskers = Cat("Whiskers", "Orange")
print(f"Name: {whiskers.name}")
print(f"Species: {whiskers.species}")
print(f"Color: {whiskers.color}")

# Methods from parent class
whiskers.eat()
whiskers.sleep()

# Overridden method
whiskers.make_sound()

# Cat-specific method for climbing trees
whiskers.climb()    
