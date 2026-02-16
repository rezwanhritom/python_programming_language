# Python Functions Basics - Definition, Calling, Return Values

print("=== BASIC FUNCTION DEFINITION AND CALLING ===")

# Define a simple function
def greet():
    """Print a simple greeting."""
    print("Hello from greet()!")

# Call the function
greet()
greet()


print("\n=== FUNCTION WITH PARAMETERS ===")

def greet_person(name):
    """Greet a person by name."""
    print(f"Hello, {name}!")

greet_person("Alice")
greet_person("Bob")


print("\n=== FUNCTION WITH MULTIPLE PARAMETERS ===")

def add(a, b):
    """Return the sum of two numbers."""
    return a + b  # return sends value back to caller[web:60][web:63][web:66][web:69][web:72]

# Call function and store result
result = add(5, 3)
print(f"5 + 3 = {result}")

# Call directly inside print
print("10 + 20 =", add(10, 20))


print("\n=== RETURN VALUES AND None ===")

def no_return():
    """Function without explicit return returns None."""
    print("Doing something, but not returning explicitly.")

def return_example():
    """Function with explicit return."""
    return 42

x = no_return()
y = return_example()
print("Result of no_return():", x)           # None
print("Result of return_example():", y)     # 42
print("Type of no_return() result:", type(x))
print("Type of return_example() result:", type(y))


print("\n=== RETURNING MULTIPLE VALUES ===")

def divide_and_remainder(a, b):
    """Return quotient and remainder of a // b."""
    q = a // b
    r = a % b
    return q, r  # Actually returns a tuple (q, r)[web:63][web:69]

quot, rem = divide_and_remainder(17, 5)
print(f"17 // 5 = {quot}, 17 % 5 = {rem}")

# You can also capture the tuple directly
pair = divide_and_remainder(20, 6)
print("As tuple:", pair)


print("\n=== POSITIONAL AND KEYWORD ARGUMENTS (BASICS) ===")

def describe_person(name, age, city):
    """Print a simple description of a person."""
    print(f"{name} is {age} years old and lives in {city}.")

# Positional arguments
describe_person("Alice", 30, "New York")

# Keyword arguments (order can change)
describe_person(age=25, name="Bob", city="London")


print("\n=== DEFAULT PARAMETER VALUES ===")

def power(base, exponent=2):
    """Raise base to exponent (default exponent is 2)."""
    return base ** exponent

print("power(3):", power(3))          # Uses default exponent=2
print("power(3, 3):", power(3, 3))    # Override default

# Be careful with mutable defaults (lists, dicts), but that's for a later file.


print("\n=== SCOPE: LOCAL VS GLOBAL VARIABLES (BASICS) ===")

x = 10  # Global variable

def show_scope():
    y = 5  # Local variable
    print("Inside function - x (global):", x)
    print("Inside function - y (local):", y)

show_scope()
print("Outside function - x (global):", x)
# print(y)  # NameError: y is not defined (y is local to show_scope)


print("\n=== MODIFYING GLOBAL VARIABLES INSIDE FUNCTIONS ===")

counter = 0  # Global

def increment_counter():
    global counter  # Declare that we want to use the global 'counter'
    counter += 1

print("counter before:", counter)
increment_counter()
increment_counter()
print("counter after:", counter)


print("\n=== DOCUMENTING FUNCTIONS WITH DOCSTRINGS ===")

def area_of_circle(radius):
    """
    Compute area of a circle with given radius.

    Args:
        radius (float): Radius of the circle.

    Returns:
        float: Area of the circle (pi * r^2).
    """
    pi = 3.141592653589793
    return pi * radius * radius

print("Area of circle (r=2):", area_of_circle(2.0))
print("Docstring for area_of_circle:")
print(area_of_circle.__doc__)


print("\n=== FUNCTIONS CALLING OTHER FUNCTIONS ===")

def square(n):
    """Return n squared."""
    return n * n

def sum_of_squares(a, b):
    """Return a^2 + b^2 using square()."""
    return square(a) + square(b)

print("square(4):", square(4))
print("sum_of_squares(3, 4):", sum_of_squares(3, 4))


print("\n=== INLINE / ANONYMOUS FUNCTIONS (LAMBDA) (PREVIEW) ===")

# Lambdas are small anonymous functions; full details will be in a later file.
double = lambda x: x * 2
print("double(5):", double(5))

# Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print("Original numbers:", numbers)
print("Doubled via map+lambda:", doubled)


print("\n=== SIMPLE FUNCTION EXAMPLES ===")

def greet_user():
    """Ask for user's name and greet them."""
    name = input("Enter your name: ")
    print(f"Nice to meet you, {name}!")

# Uncomment to test:
# greet_user()


def is_even(n):
    """Return True if n is even, False otherwise."""
    return n % 2 == 0

print("is_even(4):", is_even(4))
print("is_even(5):", is_even(5))


print("\n=== MAIN GUARD PATTERN (OPTIONAL) ===")

def main():
    """Main entry point for script (optional pattern)."""
    print("Running main()...")
    print("3 + 4 =", add(3, 4))
    print("Area of circle (r=3):", area_of_circle(3))

# This code runs only when file is executed directly, not when imported.
if __name__ == "__main__":
    main()
