# Python Lambda Functions - Syntax and Common Usage
# Lambdas are small anonymous functions defined with the 'lambda' keyword.

print("=== BASIC LAMBDA SYNTAX ===")

# Regular function
def square_def(x):
    return x * x

# Equivalent lambda function assigned to a variable
square_lambda = lambda x: x * x   # lambda parameters: expression

print("square_def(5):   ", square_def(5))
print("square_lambda(5):", square_lambda(5))

# Lambda with multiple parameters
add = lambda a, b: a + b
print("add(3, 4):", add(3, 4))

# Lambda with no parameters
get_pi = lambda: 3.14159
print("get_pi():", get_pi())


print("\n=== LAMBDAS VS REGULAR FUNCTIONS ===")

def multiply_def(a, b):
    return a * b

multiply_lambda = lambda a, b: a * b

print("multiply_def(2, 3):   ", multiply_def(2, 3))
print("multiply_lambda(2, 3):", multiply_lambda(2, 3))

# Rule of thumb: use lambda for short, simple functions, especially as arguments
# to other functions (map, filter, sorted, etc.).[web:79][web:88]


print("\n=== USING LAMBDA WITH map() ===")
# map(func, iterable) applies func to each element and returns an iterator.

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, numbers))
print("numbers:", numbers)
print("squares via map+lambda:", squares)

# Equivalent list comprehension (often preferred)
squares_comp = [x * x for x in numbers]
print("squares via comprehension:", squares_comp)


print("\n=== USING LAMBDA WITH filter() ===")
# filter(func, iterable) keeps elements where func(element) is True.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

evens = list(filter(lambda x: x % 2 == 0, numbers))
print("numbers:", numbers)
print("evens via filter+lambda:", evens)

# Equivalent list comprehension
evens_comp = [x for x in numbers if x % 2 == 0]
print("evens via comprehension:", evens_comp)


print("\n=== USING LAMBDA WITH sorted() (key=) ===")
# sorted(iterable, key=func) uses func(element) to extract a sort key.

words = ["banana", "apple", "cherry", "date"]
print("words:", words)

# Sort by length
by_length = sorted(words, key=lambda w: len(w))
print("sorted by length:", by_length)

# Sort by last character
by_last_char = sorted(words, key=lambda w: w[-1])
print("sorted by last char:", by_last_char)


print("\n=== SORTING OBJECTS / DICTS WITH LAMBDA KEY ===")

students = [
    {"name": "Alice", "score": 88},
    {"name": "Bob", "score": 95},
    {"name": "Charlie", "score": 79},
]

# Sort by score ascending
by_score = sorted(students, key=lambda s: s["score"])
print("sorted by score asc:", by_score)

# Sort by score descending
by_score_desc = sorted(students, key=lambda s: s["score"], reverse=True)
print("sorted by score desc:", by_score_desc)

# Sort by name
by_name = sorted(students, key=lambda s: s["name"])
print("sorted by name:", by_name)


print("\n=== LAMBDA INSIDE HIGHER-ORDER FUNCTIONS ===")

def apply_twice(func, x):
    """Apply a function to x twice: func(func(x))."""
    return func(func(x))

result1 = apply_twice(lambda v: v + 1, 5)   # ((5 + 1) + 1) = 7
print("apply_twice(lambda v: v + 1, 5):", result1)

result2 = apply_twice(lambda v: v * 2, 3)   # ((3 * 2) * 2) = 12
print("apply_twice(lambda v: v * 2, 3):", result2)


print("\n=== CONDITIONAL EXPRESSIONS IN LAMBDAS ===")

# Lambda with conditional expression (like inline if-else)
sign = lambda x: "positive" if x > 0 else ("zero" if x == 0 else "negative")

for n in [-3, 0, 5]:
    print(f"{n} is {sign(n)}")


print("\n=== USING LAMBDA WITH max() AND min() (key=) ===")

points = [(1, 2), (3, 1), (0, 5), (4, 4)]

# Point with largest y-coordinate
max_y = max(points, key=lambda p: p[1])
print("points:", points)
print("point with max y:", max_y)

# Point with largest (x + y)
max_sum = max(points, key=lambda p: p[0] + p[1])
print("point with max x+y:", max_sum)


print("\n=== AVOID OVERUSING LAMBDAS ===")

# This is too complex for a lambda; use def instead for readability:

# BAD (hard to read):
# process = lambda x: (x * 2 if x % 2 == 0 else x * 3) / (x + 1)

# BETTER:
def process(x):
    """Process x with different formulas depending on parity."""
    if x % 2 == 0:
        return (x * 2) / (x + 1)
    else:
        return (x * 3) / (x + 1)

print("process(4):", process(4))
print("process(5):", process(5))


print("\n=== SUMMARY ===")
print("Use lambdas for small, anonymous functions, especially as arguments to map, filter, and sorted.")
print("Prefer regular def functions for complex logic or when reuse and readability matter.")
