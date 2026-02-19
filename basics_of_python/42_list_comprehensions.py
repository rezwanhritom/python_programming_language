# Python List Comprehensions - Syntax and Conditional Usage

print("=== BASIC LIST COMPREHENSION SYNTAX ===")
# [expression for item in iterable]

numbers = [1, 2, 3, 4, 5]
squares = [x * x for x in numbers]
print("numbers:", numbers)
print("squares:", squares)

# Equivalent loop
squares_loop = []
for x in numbers:
    squares_loop.append(x * x)
print("squares via loop:", squares_loop)


print("\n=== LIST COMPREHENSION WITH IF CONDITION (FILTERING) ===")
# [expression for item in iterable if condition]

numbers = list(range(10))
evens = [n for n in numbers if n % 2 == 0]
odds = [n for n in numbers if n % 2 != 0]

print("numbers:", numbers)
print("evens:  ", evens)
print("odds:   ", odds)

# Strings: filter only vowels
text = "python list comprehensions"
vowels = [ch for ch in text if ch in "aeiou"]
print("text:", text)
print("vowels:", vowels)


print("\n=== LIST COMPREHENSION WITH IF-ELSE EXPRESSION ===")
# [expr_if_true if condition else expr_if_false for item in iterable]
# NOTE: conditional expression goes BEFORE 'for', not after.

numbers = [-2, -1, 0, 1, 2]
labels = ["negative" if n < 0 else "zero" if n == 0 else "positive" for n in numbers]
print("numbers:", numbers)
print("labels: ", labels)

# Example: square positives, keep negatives as-is
mixed = [n if n < 0 else n * n for n in numbers]
print("square positives, keep negatives:", mixed)


print("\n=== NESTED LOOPS IN LIST COMPREHENSIONS ===")
# [expression for item1 in iter1 for item2 in iter2]

rows = [1, 2, 3]
cols = ["A", "B", "C"]

pairs = [(r, c) for r in rows for c in cols]
print("rows:", rows)
print("cols:", cols)
print("pairs:", pairs)

# Equivalent nested loops
pairs_loop = []
for r in rows:
    for c in cols:
        pairs_loop.append((r, c))
print("pairs via loop:", pairs_loop)


print("\n=== FLATTENING A NESTED LIST ===")
# nested list: list of lists -> single flat list

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

flat = [elem for row in matrix for elem in row]
print("matrix:", matrix)
print("flat:", flat)

# Filter during flatten
even_flat = [elem for row in matrix for elem in row if elem % 2 == 0]
print("even_flat:", even_flat)


print("\n=== LIST COMPREHENSIONS WITH FUNCTIONS ===")

def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squares_func = [square(n) for n in numbers]
print("squares via function:", squares_func)

# Complex expressions
import math
roots = [math.sqrt(n) for n in [1, 4, 9, 16, 25]]
print("square roots:", roots)


print("\n=== USING ENUMERATE IN COMPREHENSIONS ===")

names = ["Alice", "Bob", "Charlie"]
indexed = [f"{i}: {name}" for i, name in enumerate(names, start=1)]
print("indexed:", indexed)


print("\n=== DICTIONARY TO LIST USING COMPREHENSIONS (PREVIEW) ===")

person = {"name": "Alice", "age": 30, "city": "Paris"}
keys_list = [k for k in person]
values_list = [v for v in person.values()]
items_strings = [f"{k}={v}" for k, v in person.items()]

print("person:", person)
print("keys_list:", keys_list)
print("values_list:", values_list)
print("items_strings:", items_strings)


print("\n=== CONDITIONAL CHAINING AND READABILITY ===")

# It's possible to cram a lot into a single comprehension, but readability suffers.
# Prefer breaking complex logic into smaller pieces or regular loops.

data = [1, -2, 3, -4, 0, 5]
# Complex one-liner:
processed = [
    (n, "neg" if n < 0 else "zero" if n == 0 else "pos")
    for n in data
    if n != -4
]
print("data:", data)
print("processed (skip -4, classify sign):", processed)


print("\n=== LIST COMPREHENSION VS map/filter ===")

numbers = [1, 2, 3, 4, 5]

# Using map/filter + lambda
import math
squared_evens_map = list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, numbers)))
print("squared_evens via map/filter:", squared_evens_map)

# Using comprehension (often clearer)
squared_evens_comp = [x * x for x in numbers if x % 2 == 0]
print("squared_evens via comprehension:", squared_evens_comp)


print("\n=== SUMMARY ===")
print("List comprehensions provide a concise way to create lists from iterables.")
print("You can add an 'if' at the end for filtering, and an inline 'if-else' before 'for' for expressions.")
print("Keep comprehensions readable; use normal loops if logic gets too complex.")
