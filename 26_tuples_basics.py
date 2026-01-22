# Python Tuples - Basic Concepts Reference
# Ordered, immutable sequences

# === TUPLE CREATION ===
print("=== TUPLE CREATION ===")

# Empty tuple
empty_tuple = ()
print(f"Empty tuple: {empty_tuple}, type: {type(empty_tuple)}")

# Single-element (singleton) tuple (note the trailing comma)
single = (42,)
print(f"Single element tuple: {single}, type: {type(single)}")

# Without comma it's just an int, not a tuple
not_tuple = (42)
print(f"(42) is type: {type(not_tuple)}")

# Multiple elements
numbers = (1, 2, 3, 4)
print(f"Numbers tuple: {numbers}")

# Mixed types
mixed = (1, "hello", 3.14, True, None)
print(f"Mixed tuple: {mixed}")

# Nested tuples
nested = ((1, 2), (3, 4), (5, 6))
print(f"Nested tuple: {nested}")

# Tuples can be created without parentheses using commas (tuple packing)
packed = 10, 20, "python"
print(f"Packed tuple (implicit): {packed}, type: {type(packed)}")


# === TUPLE FROM OTHER ITERABLES ===
print("\n=== TUPLE FROM OTHER ITERABLES ===")

# From list
lst = [1, 2, 3]
t_from_list = tuple(lst)
print(f"From list {lst} -> {t_from_list}")

# From string
s = "hello"
t_from_string = tuple(s)
print(f"From string '{s}' -> {t_from_string}")

# From range
r = range(5)
t_from_range = tuple(r)
print(f"From range(5) -> {t_from_range}")

# From set (order is not guaranteed)
set_obj = {3, 1, 2}
t_from_set = tuple(set_obj)
print(f"From set {set_obj} -> {t_from_set}")


# === TUPLE INDEXING ===
print("\n=== TUPLE INDEXING ===")
fruits = ("apple", "banana", "cherry", "date")

print(f"fruits[0]: {fruits[0]}")      # First element
print(f"fruits[1]: {fruits[1]}")      # Second element
print(f"fruits[-1]: {fruits[-1]}")    # Last element
print(f"fruits[-2]: {fruits[-2]}")    # Second to last

# Nested indexing
matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(f"matrix[0][0]: {matrix[0][0]}")
print(f"matrix[1][2]: {matrix[1][2]}")


# === TUPLE SLICING ===
print("\n=== TUPLE SLICING ===")
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

print(f"numbers[2:5]: {numbers[2:5]}")      # Elements 2, 3, 4
print(f"numbers[:5]: {numbers[:5]}")        # First 5 elements
print(f"numbers[5:]: {numbers[5:]}")        # From index 5 to end
print(f"numbers[:]: {numbers[:]}")          # Copy of entire tuple
print(f"numbers[::2]: {numbers[::2]}")      # Every second element
print(f"numbers[1::2]: {numbers[1::2]}")    # Every second element from index 1
print(f"numbers[::-1]: {numbers[::-1]}")    # Reversed tuple
print(f"numbers[-3:]: {numbers[-3:]}")      # Last 3 elements
print(f"numbers[:-3]: {numbers[:-3]}")      # All except last 3


# === TUPLES ARE IMMUTABLE ===
print("\n=== TUPLES ARE IMMUTABLE ===")
t = (1, 2, 3)
print(f"Original tuple: {t}")
# The following would raise TypeError if uncommented:
# t[0] = 10
# t.append(4)
print("You cannot change, add, or remove elements from a tuple directly.")

# But if a tuple contains mutable objects, those objects can change
t2 = ([1, 2], [3, 4])
print(f"\nTuple with lists: {t2}")
t2[0].append(99)  # Modifying the list inside the tuple
print(f"After t2[0].append(99): {t2}  # Tuple identity same, inner list changed")


# === TUPLE LENGTH AND MEMBERSHIP ===
print("\n=== LENGTH AND MEMBERSHIP ===")
fruits = ("apple", "banana", "cherry")

print(f"len(fruits): {len(fruits)}")
print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'mango' in fruits: {'mango' in fruits}")
print(f"'banana' not in fruits: {'banana' not in fruits}")


# === TUPLE ITERATION ===
print("\n=== TUPLE ITERATION ===")
colors = ("red", "green", "blue")

print("For loop:")
for color in colors:
    print(f"  {color}")

print("\nWith index:")
for i in range(len(colors)):
    print(f"  colors[{i}] = {colors[i]}")

print("\nWith enumerate:")
for index, color in enumerate(colors):
    print(f"  Index {index}: {color}")


# === TUPLE PACKING AND UNPACKING ===
print("\n=== PACKING AND UNPACKING ===")

# Packing: assigning multiple values to a tuple in one go
point = (10, 20)
print(f"Packed point: {point}")

# Unpacking: assigning tuple elements to variables
x, y = point
print(f"Unpacked: x={x}, y={y}")

# Multiple values
person = ("Alice", 30, "New York")
name, age, city = person
print(f"Name: {name}, Age: {age}, City: {city}")

# Extended unpacking
t = (1, 2, 3, 4, 5)
first, *middle, last = t
print(f"first: {first}, middle: {middle}, last: {last}")

# Ignore unwanted values with _
a, _, c = (10, 20, 30)
print(f"a: {a}, c: {c}")


# === SWAPPING VARIABLES WITH TUPLES ===
print("\n=== SWAPPING VARIABLES ===")
a = 5
b = 10
print(f"Before swap: a={a}, b={b}")
a, b = b, a  # Tuple packing/unpacking
print(f"After swap: a={a}, b={b}")


# === TUPLE CONCATENATION AND REPETITION ===
print("\n=== CONCATENATION AND REPETITION ===")
t1 = (1, 2, 3)
t2 = (4, 5, 6)

concat = t1 + t2
print(f"t1 + t2: {concat}")

repeat = t1 * 3
print(f"t1 * 3: {repeat}")


# === TUPLE COMPARISON ===
print("\n=== TUPLE COMPARISON ===")
t1 = (1, 2, 3)
t2 = (1, 2, 3)
t3 = (1, 2, 4)
t4 = (0, 99)

print(f"t1 == t2: {t1 == t2}")  # True
print(f"t1 == t3: {t1 == t3}")  # False
print(f"t1 < t3: {t1 < t3}")    # True (compares element-wise)
print(f"t1 > t4: {t1 > t4}")    # True (1 > 0 at first position)


# === TUPLES IN BOOLEAN CONTEXT ===
print("\n=== BOOLEAN CONTEXT ===")
empty = ()
non_empty = (1, 2, 3)

print(f"bool(()) -> {bool(empty)}")
print(f"bool((1,2,3)) -> {bool(non_empty)}")

if non_empty:
    print("Tuple has elements")
else:
    print("Tuple is empty")


# === TUPLES AS DICTIONARY KEYS ===
print("\n=== TUPLES AS DICTIONARY KEYS ===")
# Tuples are hashable (if all elements are hashable) and can be used as dict keys
locations = {
    (23.5, 90.3): "City A",
    (24.0, 89.9): "City B",
}

coord = (23.5, 90.3)
print(f"Location at {coord}: {locations[coord]}")


# === RETURNING MULTIPLE VALUES FROM FUNCTIONS ===
print("\n=== FUNCTIONS RETURNING TUPLES ===")
def min_max(values):
    """Return minimum and maximum of an iterable as a tuple."""
    return min(values), max(values)

nums = [3, 1, 4, 1, 5, 9]
mn, mx = min_max(nums)
print(f"Numbers: {nums}")
print(f"Min: {mn}, Max: {mx}")


# === PRACTICAL USE CASES ===
print("\n=== PRACTICAL USE CASES ===")

# 1. Coordinate pairs
points = [(0, 0), (1, 2), (3, 4)]
for x, y in points:
    print(f"Point: x={x}, y={y}")

# 2. Enumerating with tuple unpacking
students = [("Alice", 25), ("Bob", 22), ("Charlie", 27)]
for name, age in students:
    print(f"{name} is {age} years old")

# 3. Using tuples to protect data from modification
config = ("localhost", 8080, "https")
host, port, protocol = config
print(f"Config: host={host}, port={port}, protocol={protocol}")
print("config cannot be accidentally modified since it's a tuple")
