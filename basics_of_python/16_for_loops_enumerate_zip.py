# Python enumerate() and zip() - Complete Reference
# Advanced iteration techniques for parallel and indexed loops

# === ENUMERATE() BASICS ===
# enumerate() adds a counter to an iterable
print("=== ENUMERATE() BASICS ===")
fruits = ["apple", "banana", "cherry", "date"]

# Without enumerate
index = 0
for fruit in fruits:
    print(f"Index {index}: {fruit}")
    index += 1

# With enumerate (cleaner)
print("\nWith enumerate():")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# enumerate() returns an enumerate object
enum_obj = enumerate(fruits)
print(f"\nenumerate(fruits): {enum_obj}")
print(f"type(enumerate(fruits)): {type(enum_obj)}")
print(f"list(enumerate(fruits)): {list(enumerate(fruits))}")


# === ENUMERATE WITH CUSTOM START INDEX ===
# Start counting from a different number
print("\n=== ENUMERATE WITH CUSTOM START ===")
for index, fruit in enumerate(fruits, start=1):
    print(f"Position {index}: {fruit}")

# Start from 10
for index, fruit in enumerate(fruits, start=10):
    print(f"Item {index}: {fruit}")


# === ZIP() BASICS ===
# zip() combines multiple iterables into pairs/tuples
print("\n=== ZIP() BASICS ===")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

# Without zip
for i in range(len(names)):
    print(f"{names[i]} is {ages[i]} years old")

# With zip (more Pythonic)
print("\nWith zip():")
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# zip() stops at the shortest iterable
short_list = [1, 2]
long_list = ['a', 'b', 'c', 'd']
print(f"\nzip(short, long): {list(zip(short_list, long_list))}")


# === ZIP MULTIPLE ITERABLES ===
# zip() can combine more than two iterables
print("\n=== ZIP MULTIPLE ITERABLES ===")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "London", "Paris"]
countries = ["USA", "UK", "France"]

for name, age, city, country in zip(names, ages, cities, countries):
    print(f"{name}, {age}, from {city}, {country}")


# === ZIP WITH DIFFERENT LENGTHS ===
# zip() stops at the shortest iterable
print("\n=== ZIP WITH DIFFERENT LENGTHS ===")
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
list3 = [10, 20]

zipped = zip(list1, list2, list3)
print(f"list(zip(list1, list2, list3)): {list(zipped)}")
print("Note: zip stops at the shortest iterable (length 2)")


# === ZIP LONGEST (ITERTOOLS) ===
# For completeness, zip longest fills missing values
from itertools import zip_longest

print("\n=== ZIP LONGEST (ITERTOOLS) ===")
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']

zipped_longest = zip_longest(list1, list2, fillvalue=None)
print(f"zip_longest with fillvalue=None: {list(zipped_longest)}")

zipped_longest = zip_longest(list1, list2, fillvalue="N/A")
print(f"zip_longest with fillvalue='N/A': {list(zipped_longest)}")


# === COMBINING ENUMERATE AND ZIP ===
# Powerful pattern for indexed parallel iteration
print("\n=== ENUMERATE + ZIP ===")
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for index, (name, score) in enumerate(zip(names, scores)):
    print(f"Rank {index + 1}: {name} - {score} points")

# Alternative: enumerate each list separately
for i, name in enumerate(names):
    score = scores[i]
    print(f"Student {i}: {name} - {score}")


# === UNPACKING ZIP RESULTS ===
# zip() produces tuples that can be unpacked
print("\n=== UNPACKING ZIP RESULTS ===")
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]

# Manual unpacking
for pair in pairs:
    first, second = pair
    print(f"{first} -> {second}")

# Direct unpacking in loop
for first, second in pairs:
    print(f"{first} -> {second}")


# === PRACTICAL EXAMPLES ===

# 1. Parallel processing of multiple lists
print("\n=== PRACTICAL: PARALLEL PROCESSING ===")
prices = [10.0, 20.0, 30.0, 40.0]
quantities = [2, 3, 1, 4]
tax_rates = [0.08, 0.05, 0.10, 0.07]

total_cost = 0
for price, qty, tax_rate in zip(prices, quantities, tax_rates):
    subtotal = price * qty
    tax = subtotal * tax_rate
    total = subtotal + tax
    total_cost += total
    print(f"Item: ${price} × {qty} + {tax_rate*100}% tax = ${total:.2f}")

print(f"Total cost: ${total_cost:.2f}")

# 2. Creating dictionaries from parallel lists
print("\n=== PRACTICAL: DICT FROM ZIP ===")
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']

person_dict = dict(zip(keys, values))
print(f"dict(zip(keys, values)): {person_dict}")

# 3. Enumerating files with line numbers
print("\n=== PRACTICAL: ENUMERATE FILES ===")
files = ["file1.txt", "file2.txt", "file3.txt"]

for file_index, filename in enumerate(files, start=1):
    print(f"Processing file {file_index}: {filename}")
    # Simulate reading lines
    lines = [f"line {i}" for i in range(1, 4)]
    for line_index, line in enumerate(lines, start=1):
        print(f"  Line {line_index}: {line}")

# 4. Pairwise iteration
print("\n=== PRACTICAL: PAIRWISE ITERATION ===")
data = [1, 2, 3, 4, 5, 6]

# Process pairs
for i, (a, b) in enumerate(zip(data[::2], data[1::2])):
    print(f"Pair {i}: ({a}, {b}) -> Sum: {a + b}")
