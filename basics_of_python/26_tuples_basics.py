# Python Tuples - Complete Basics Reference
# Ordered, immutable collections of items

# === TUPLE CREATION ===
print("=== TUPLE CREATION ===")
empty_tuple = ()
print(f"Empty tuple: {empty_tuple}, type: {type(empty_tuple)}")

single = (1,)  # Comma required for single-element tuple
print(f"Single element: {single}, type: {type(single)}")

# Without comma, it is not a tuple
not_a_tuple = (1)
print(f"(1) without comma: {not_a_tuple}, type: {type(not_a_tuple)}")

# Multiple elements
numbers = (1, 2, 3, 4, 5)
print(f"Numbers tuple: {numbers}")

# Mixed types
mixed = (1, "hello", 3.14, True, None)
print(f"Mixed types: {mixed}")

# Nested tuples
nested = ((1, 2), (3, 4), (5, 6))
print(f"Nested: {nested}")

# Using tuple() constructor
from_list = tuple([10, 20, 30])
print(f"From list: {from_list}")

from_string = tuple("hello")
print(f"From string: {from_string}")

from_range = tuple(range(5))
print(f"From range: {from_range}")


# === TUPLE INDEXING ===
print("\n=== TUPLE INDEXING ===")
fruits = ("apple", "banana", "cherry", "date")

print(f"fruits[0]: {fruits[0]}")
print(f"fruits[1]: {fruits[1]}")
print(f"fruits[-1]: {fruits[-1]}")
print(f"fruits[-2]: {fruits[-2]}")

# Nested indexing
nested = ((1, 2), (3, 4))
print(f"nested[0][1]: {nested[0][1]}")


# === TUPLE SLICING ===
print("\n=== TUPLE SLICING ===")
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

print(f"numbers[2:5]: {numbers[2:5]}")
print(f"numbers[:5]: {numbers[:5]}")
print(f"numbers[5:]: {numbers[5:]}")
print(f"numbers[:]: {numbers[:]}")
print(f"numbers[::2]: {numbers[::2]}")
print(f"numbers[::-1]: {numbers[::-1]}")


# === TUPLE IMMUTABILITY ===
print("\n=== TUPLE IMMUTABILITY ===")
fruits = ("apple", "banana", "cherry")
print(f"Original: {fruits}")

# Cannot modify elements
# fruits[0] = "apricot"  # TypeError: 'tuple' object does not support item assignment

# Cannot modify slices
# fruits[1:3] = ("x", "y")  # TypeError: 'tuple' object does not support item assignment

# But can replace entire tuple
fruits = ("apricot", "blueberry", "cherry")
print(f"Reassigned: {fruits}")

# Tuples can contain mutable objects
mutable_tuple = ([1, 2], [3, 4])
print(f"Original: {mutable_tuple}")
mutable_tuple[0].append(3)  # Modifying list inside tuple
print(f"After modifying inner list: {mutable_tuple}")


# === TUPLE CONCATENATION ===
print("\n=== TUPLE CONCATENATION ===")
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

combined = tuple1 + tuple2
print(f"tuple1 + tuple2: {combined}")

# In-place concatenation not allowed (tuples are immutable)
# tuple1 += tuple2  # This creates a new tuple and reassigns


# === TUPLE REPETITION ===
print("\n=== TUPLE REPETITION ===")
original = (1, 2)
repeated = original * 3
print(f"(1, 2) * 3: {repeated}")

# In-place repetition not allowed
# original *= 2  # Creates new tuple and reassigns


# === TUPLE LENGTH ===
print("\n=== TUPLE LENGTH ===")
fruits = ("apple", "banana", "cherry")
print(f"len(fruits): {len(fruits)}")

empty = ()
print(f"len(empty): {len(empty)}")


# === TUPLE MEMBERSHIP ===
print("\n=== TUPLE MEMBERSHIP ===")
fruits = ("apple", "banana", "cherry")

print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'mango' in fruits: {'mango' in fruits}")
print(f"'banana' not in fruits: {'banana' not in fruits}")


# === TUPLE UNPACKING ===
print("\n=== TUPLE UNPACKING ===")
point = (10, 20)
x, y = point
print(f"Point: {point} -> x={x}, y={y}")

# Extended unpacking
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(f"First: {first}, Middle: {middle}, Last: {last}")

# Ignoring values
_, important, _ = (10, 20, 30)
print(f"Important value: {important}")


# === NAMED TUPLES ===
print("\n=== NAMED TUPLES ===")
from collections import namedtuple

# Create named tuple type
Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(f"Named tuple: {p}")
print(f"p.x: {p.x}, p.y: {p.y}")

# Named tuple with field names
Person = namedtuple("Person", ["name", "age", "city"])
alice = Person("Alice", 30, "New York")
print(f"Person: {alice}")
print(f"Name: {alice.name}, Age: {alice.age}, City: {alice.city}")


# === TUPLE COMPARISON ===
print("\n=== TUPLE COMPARISON ===")
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)
tuple3 = (3, 2, 1)

print(f"tuple1 == tuple2: {tuple1 == tuple2}")  # True
print(f"tuple1 == tuple3: {tuple1 == tuple3}")  # False
print(f"tuple1 is tuple2: {tuple1 is tuple2}")  # False (different objects)


# === TUPLE AS DICTIONARY KEYS ===
print("\n=== TUPLE AS DICTIONARY KEYS ===")
# Tuples can be dictionary keys if all elements are hashable
coordinates = {}
points = [(1, 2), (3, 4), (5, 6)]

for i, point in enumerate(points):
    coordinates[point] = f"Point {i}"

print(f"Dictionary with tuple keys: {coordinates}")
print(f"coordinates[(1, 2)]: {coordinates[(1, 2)]}")


# === TUPLE AS SET ELEMENTS ===
print("\n=== TUPLE AS SET ELEMENTS ===")
# Tuples can be set elements if all elements are hashable
set_of_tuples = {(1, 2), (3, 4), (1, 2)}  # Duplicate will be removed
print(f"Set of tuples: {set_of_tuples}")


# === TUPLE METHODS ===
print("\n=== TUPLE METHODS ===")
fruits = ("apple", "banana", "cherry", "banana")

print(f"fruits.count('banana'): {fruits.count('banana')}")
print(f"fruits.index('cherry'): {fruits.index('cherry')}")
print(f"fruits.index('banana', 2): {fruits.index('banana', 2)}")


# === TUPLE TO LIST CONVERSION ===
print("\n=== TUPLE TO LIST CONVERSION ===")
tuple_fruits = ("apple", "banana", "cherry")
list_fruits = list(tuple_fruits)
print(f"Tuple: {tuple_fruits}")
print(f"List: {list_fruits}")
print(f"Type of list: {type(list_fruits)}")


# === LIST TO TUPLE CONVERSION ===
print("\n=== LIST TO TUPLE CONVERSION ===")
list_numbers = [1, 2, 3, 4, 5]
tuple_numbers = tuple(list_numbers)
print(f"List: {list_numbers}")
print(f"Tuple: {tuple_numbers}")
print(f"Type of tuple: {type(tuple_numbers)}")


# === TUPLE PERFORMANCE ===
print("\n=== TUPLE PERFORMANCE ===")
print("Tuples are faster than lists for:")
print("- Creation: tuple() is faster than list()")
print("- Iteration: Slightly faster due to immutability")
print("- Memory: More memory efficient")
print("- Hashing: Can be used as dict keys and set elements")


# === TUPLE BEST PRACTICES ===
print("\n=== TUPLE BEST PRACTICES ===")
# Use tuples for fixed collections of items
# Use tuples as records (e.g., coordinates, database rows)
# Use tuples for function arguments that shouldn't change
# Use tuples for dictionary keys when needed
# Use tuples for multiple return values from functions


# === PACKING AND UNPACKING ===
print("\n=== PACKING AND UNPACKING ===")
# Packing: creating tuple from values
packed = 1, 2, 3  # Same as (1, 2, 3)
print(f"Packed: {packed}")

# Unpacking: extracting values from tuple
a, b, c = packed
print(f"Unpacked: a={a}, b={b}, c={c}")

# Swapping values using tuple packing/unpacking
x = 10
y = 20
print(f"Before swap: x={x}, y={y}")
x, y = y, x  # Tuple packing/unpacking
print(f"After swap: x={x}, y={y}")


# === TUPLE AS FUNCTION ARGUMENTS ===
print("\n=== TUPLE AS FUNCTION ARGUMENTS ===")
def process_coordinates(point):
    x, y = point
    return x * 2, y * 2

coordinates = (5, 10)
result = process_coordinates(coordinates)
print(f"Input: {coordinates}, Output: {result}")


# === TUPLE AS RETURN VALUES ===
print("\n=== TUPLE AS RETURN VALUES ===")
def get_min_max(numbers):
    return min(numbers), max(numbers)

data = [3, 1, 4, 1, 5, 9, 2]
min_val, max_val = get_min_max(data)
print(f"Data: {data}")
print(f"Min: {min_val}, Max: {max_val}")


# === ADVANCED: UNPACKING IN LOOPS ===
print("\n=== UNPACKING IN LOOPS ===")
points = [(1, 2), (3, 4), (5, 6)]

for x, y in points:
    print(f"Point: ({x}, {y}) -> Sum: {x + y}")


# === TUPLE IMMUTABILITY DEMONSTRATION ===
print("\n=== IMMUTABILITY DEMONSTRATION ===")
def try_modify(tup):
    try:
        tup[0] = 999
    except TypeError as e:
        print(f"Cannot modify tuple: {e}")

original = (1, 2, 3)
print(f"Original: {original}")
try_modify(original)
print(f"After function call: {original}")  # Unchanged


# === TUPLE IN FUNCTION DEFINITIONS ===
print("\n=== TUPLE IN FUNCTION DEFINITIONS ===")
def func_with_tuple_args(*args):
    """*args collects positional arguments as a tuple"""
    print(f"args type: {type(args)}")
    print(f"args value: {args}")
    return sum(args)

result = func_with_tuple_args(1, 2, 3, 4, 5)
print(f"Sum: {result}")


# === TUPLE COMPREHENSION (GENERATOR EXPRESSION) ===
print("\n=== TUPLE COMPREHENSION ===")
# Tuples don't have comprehensions like lists
# Use generator expression and convert to tuple
numbers = [1, 2, 3, 4, 5]
squares_tuple = tuple(x**2 for x in numbers)
print(f"Original: {numbers}")
print(f"Squares tuple: {squares_tuple}")
print(f"Type: {type(squares_tuple)}")


# === FINAL SUMMARY ===
print("\n=== FINAL SUMMARY ===")
print("Tuples are immutable, ordered sequences")
print("Use them for fixed data, records, keys, and return values")
print("They are more memory-efficient and faster than lists")
print("Immutability makes them hashable (usable as dict keys)")
