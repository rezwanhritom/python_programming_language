# Python Inheritance - Single Inheritance, super(), Method Overriding

print("=== BASIC SINGLE INHERITANCE ===")

class Animal:
    """Base class (parent)."""
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Some generic animal sound")

    def info(self):
        print(f"Animal name: {self.name}")

class Dog(Animal):
    """Dog inherits from Animal (child class)."""
    def __init__(self, name, breed):
        # Call parent's __init__ to initialize shared attributes.[web:109][web:115][web:118]
        super().__init__(name)
        self.breed = breed

    # Override speak()
    def speak(self):
        print(f"{self.name} says: Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says: Meow!")

dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers")

dog.info()
dog.speak()
print("Dog breed:", dog.breed)

cat.info()
cat.speak()


print("\n=== METHOD OVERRIDING AND USING super() TO EXTEND PARENT BEHAVIOR ===")

class Logger:
    def log(self, message):
        print(f"[LOG] {message}")

class TimestampLogger(Logger):
    def log(self, message):
        import datetime
        timestamp = datetime.datetime.now().isoformat(timespec="seconds")
        # Extend parent behavior using super().log()[web:109][web:112][web:118]
        super().log(f"{timestamp} - {message}")

base_logger = Logger()
ts_logger = TimestampLogger()

base_logger.log("Base logger message")
ts_logger.log("Timestamped logger message")


print("\n=== OVERRIDING __init__ IN CHILD CLASS ===")

class Vehicle:
    def __init__(self, brand, wheels):
        self.brand = brand
        self.wheels = wheels

    def describe(self):
        print(f"{self.brand} vehicle with {self.wheels} wheels.")

class Car(Vehicle):
    def __init__(self, brand, model):
        # Vehicle has wheels, but car fixes wheels=4
        super().__init__(brand, wheels=4)
        self.model = model

    # Override describe()
    def describe(self):
        # Optionally call parent describe then add more info
        super().describe()
        print(f"Model: {self.model}")

car = Car("Tesla", "Model 3")
car.describe()


print("\n=== USING isinstance() AND issubclass() ===")

print("isinstance(dog, Dog):", isinstance(dog, Dog))
print("isinstance(dog, Animal):", isinstance(dog, Animal))
print("isinstance(dog, Cat):", isinstance(dog, Cat))

print("issubclass(Dog, Animal):", issubclass(Dog, Animal))
print("issubclass(Cat, Animal):", issubclass(Cat, Animal))
print("issubclass(Animal, Dog):", issubclass(Animal, Dog))


print("\n=== ANOTHER OVERRIDE EXAMPLE ===")

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

shapes = [Circle(2), Square(3)]
for s in shapes:
    print(f"{s.__class__.__name__} area:", s.area())


print("\n=== METHOD RESOLUTION ORDER (MRO) NOTE ===")
# In single inheritance, MRO is straightforward: Child -> Parent -> object.
# In multiple inheritance, Python uses C3 linearization to determine method lookup order.[web:109][web:118]
print("Dog MRO:", Dog.__mro__)
print("Cat MRO:", Cat.__mro__)


print("\n=== MAIN GUARD DEMO ===")

def main():
    print("Running main() from 50_inheritance.py")
    d = Dog("Rex", "Shepherd")
    d.speak()
    v = Vehicle("Generic", 3)
    v.describe()

if __name__ == "__main__":
    main()
