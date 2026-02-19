# Python Classes - Definition, __init__, Instance Attributes, Methods

print("=== BASIC CLASS DEFINITION AND INSTANCE CREATION ===")

class Person:
    """
    Simple Person class with instance attributes and methods.
    __init__ initializes new instances; self refers to the instance.[web:108][web:111][web:114][web:117]
    """
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    # Instance method (first parameter must be self)
    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create instances (objects)
alice = Person("Alice", 30)
bob = Person("Bob", 25)

alice.say_hello()
bob.say_hello()


print("\n=== ACCESSING AND MODIFYING INSTANCE ATTRIBUTES ===")

print("Alice's age:", alice.age)
alice.age += 1
print("Alice's age after birthday:", alice.age)

# You can add new attributes dynamically to an instance
alice.city = "Paris"
print("Alice's city:", alice.city)

# But Bob does not automatically get that attribute
print("Does Bob have 'city'? ->", hasattr(bob, "city"))


print("\n=== CLASS ATTRIBUTES VS INSTANCE ATTRIBUTES ===")

class Counter:
    # Class attribute (shared across all instances)
    total_count = 0

    def __init__(self, name):
        # Instance attribute (per-instance)
        self.name = name
        Counter.total_count += 1

c1 = Counter("first")
c2 = Counter("second")

print("c1.name:", c1.name)
print("c2.name:", c2.name)
print("Counter.total_count:", Counter.total_count)
print("c1.total_count:", c1.total_count)  # Access class attribute via instance
print("c2.total_count:", c2.total_count)


print("\n=== __str__ AND __repr__ FOR STRING REPRESENTATION ===")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Human-readable representation (print, f-strings)
    def __str__(self):
        return f"Point({self.x}, {self.y})"

    # Unambiguous representation (for debugging, repr())
    def __repr__(self):
        return f"Point(x={self.x!r}, y={self.y!r})"

p = Point(3, 4)
print("print(p):", p)
print("repr(p):", repr(p))


print("\n=== INSTANCE METHODS USING self ===")

class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Add amount to balance."""
        self.balance += amount

    def withdraw(self, amount):
        """Subtract amount from balance if sufficient funds."""
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount

    def show_balance(self):
        print(f"{self.owner}'s balance: {self.balance:.2f}")

acct = BankAccount("Charlie", 100.0)
acct.show_balance()
acct.deposit(50)
acct.show_balance()
acct.withdraw(200)
acct.withdraw(75)
acct.show_balance()


print("\n=== USING METHODS AS BEHAVIORS ===")

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Return area of rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return perimeter of rectangle."""
        return 2 * (self.width + self.height)

rect = Rectangle(3, 4)
print("Rectangle area:", rect.area())
print("Rectangle perimeter:", rect.perimeter())


print("\n=== MAIN GUARD FOR DEMO CODE ===")

def demo():
    print("Demo running from 49_classes_basics.py")
    p = Person("DemoUser", 99)
    p.say_hello()

if __name__ == "__main__":
    demo()
