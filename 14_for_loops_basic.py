# Python for Loops (Basic) - Complete Reference
# Iterate over sequences and collections

# === ITERATING OVER LISTS ===
print("=== ITERATING OVER LISTS ===")
fruits = ["apple", "banana", "cherry", "date"]

for fruit in fruits:
    print(f"Fruit: {fruit}")

# Accessing index and value with enumerate (covered more in enumerate file)
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")


# === ITERATING OVER STRINGS ===
print("\n=== ITERATING OVER STRINGS ===")
word = "Python"

for char in word:
    print(f"Character: {char}")

# Count vowels
vowel_count = 0
vowels = "aeiou"
for char in word.lower():
    if char in vowels:
        vowel_count += 1
print(f"Vowels in '{word}': {vowel_count}")


# === ITERATING OVER TUPLES ===
print("\n=== ITERATING OVER TUPLES ===")
coordinates = (10, 20, 30, 40, 50)

for coord in coordinates:
    print(f"Coordinate: {coord}")

# Iterating over tuple of tuples (pairs)
points = ((1, 2), (3, 4), (5, 6))
for x, y in points:
    print(f"Point: ({x}, {y})")


# === ITERATING OVER DICTIONARIES ===
print("\n=== ITERATING OVER DICTIONARIES ===")
person = {"name": "Alice", "age": 30, "city": "New York"}

# Iterate over keys (default behavior)
for key in person:
    print(f"Key: {key}")

# Iterate over keys explicitly
for key in person.keys():
    print(f"Key: {key}")

# Iterate over values
for value in person.values():
    print(f"Value: {value}")

# Iterate over key-value pairs (items)
for key, value in person.items():
    print(f"{key}: {value}")


# === ITERATING OVER SETS ===
print("\n=== ITERATING OVER SETS ===")
unique_numbers = {1, 2, 3, 4, 5}

for num in unique_numbers:
    print(f"Number: {num}")

# Note: Set iteration order is arbitrary (not guaranteed)
# Sets are unordered collections


# === ITERATING OVER NESTED LISTS ===
print("\n=== ITERATING OVER NESTED LISTS ===")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in matrix:
    print(f"Row: {row}")
    for element in row:
        print(f"  Element: {element}")


# === MODIFYING LIST WHILE ITERATING (DANGEROUS) ===
print("\n=== MODIFYING LIST WHILE ITERATING ===")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Safe way: create a new list
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
print(f"Original: {numbers}")
print(f"Evens: {evens}")

# Unsafe way (don't do this):
# for num in numbers:
#     if num % 2 == 0:
#         numbers.remove(num)  # Modifies list being iterated


# === USING BREAK IN FOR LOOPS ===
print("\n=== USING BREAK ===")
# Exit loop early when condition is met
search_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
target = 55

for num in search_list:
    if num == target:
        print(f"Found {target}!")
        break
else:
    # This else block executes if loop completes without break
    print(f"{target} not found in list")


# === USING CONTINUE IN FOR LOOPS ===
print("\n=== USING CONTINUE ===")
# Skip current iteration and continue with next
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Odd numbers:")
for num in numbers:
    if num % 2 == 0:
        continue  # Skip even numbers
    print(f"  {num}")


# === BASIC LIST COMPREHENSIONS ===
print("\n=== BASIC LIST COMPREHENSIONS ===")
# Create new list by transforming each element
original = [1, 2, 3, 4, 5]
squared = [x**2 for x in original]
print(f"Original: {original}")
print(f"Squared: {squared}")

# Filter with if condition
evens = [x for x in original if x % 2 == 0]
print(f"Evens: {evens}")

# Transform and filter
odd_cubes = [x**3 for x in original if x % 2 != 0]
print(f"Odd cubes: {odd_cubes}")


# === ITERATING OVER MULTIPLE SEQUENCES WITH ZIP ===
print("\n=== ITERATING WITH ZIP ===")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "London", "Paris"]

for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}")

# Zip stops at shortest sequence
short_list = [1, 2]
long_list = ['a', 'b', 'c', 'd']
print("\nZip with different lengths:")
for num, letter in zip(short_list, long_list):
    print(f"{num}: {letter}")


# === ITERATING WITH INDEX USING ENUMERATE ===
print("\n=== ITERATING WITH ENUMERATE ===")
colors = ["red", "green", "blue", "yellow"]

for index, color in enumerate(colors):
    print(f"Index {index}: {color}")

# Start enumeration from different number
for index, color in enumerate(colors, start=1):
    print(f"Position {index}: {color}")


# === ITERATING BACKWARDS ===
print("\n=== ITERATING BACKWARDS ===")
numbers = [1, 2, 3, 4, 5]

# Using reversed()
for num in reversed(numbers):
    print(f"Reversed: {num}")

# Using slicing (creates a copy)
for num in numbers[::-1]:
    print(f"Sliced reversed: {num}")


# === ITERATING OVER RANGE OBJECT (preview of next file) ===
print("\n=== ITERATING OVER RANGE OBJECT ===")
# range() creates a sequence of numbers
for i in range(5):
    print(f"Range value: {i}")


# === NESTED FOR LOOPS (SIMPLE) ===
print("\n=== NESTED FOR LOOPS ===")
# Outer loop
for i in range(3):
    print(f"Outer loop i = {i}")
    # Inner loop
    for j in range(2):
        print(f"  Inner loop j = {j}, i + j = {i + j}")


# === FOR LOOP WITH ELSE CLAUSE ===
print("\n=== FOR LOOP WITH ELSE CLAUSE ===")
# else block runs if loop completes without break
numbers = [1, 2, 3, 4, 5]
target = 3

for num in numbers:
    if num == target:
        print(f"Found {target}!")
        break
else:
    print(f"{target} not found")

# Example where else runs
target = 10
for num in numbers:
    if num == target:
        print(f"Found {target}!")
        break
else:
    print(f"{target} not found (else block executed)")
