# Python Dictionary Comprehensions - From Lists and Dicts

print("=== BASIC DICT COMPREHENSION FROM RANGE ===")
# {key_expr: value_expr for item in iterable}

squares = {n: n * n for n in range(5)}
print("squares dict:", squares)


print("\n=== DICT COMPREHENSION FROM LIST OF TUPLES ===")

pairs = [("a", 1), ("b", 2), ("c", 3)]
d = {key: value for key, value in pairs}
print("pairs:", pairs)
print("dict from pairs:", d)


print("\n=== SWAPPING KEYS AND VALUES ===")

original = {"a": 1, "b": 2, "c": 3}
swapped = {value: key for key, value in original.items()}
print("original:", original)
print("swapped:", swapped)

# Note: if values are not unique, later keys will overwrite earlier ones.


print("\n=== FILTERING ITEMS IN DICT COMPREHENSION ===")

prices = {"apple": 1.2, "banana": 0.5, "cherry": 2.0, "date": 3.5}
# Filter items with price >= 1.0
expensive = {fruit: price for fruit, price in prices.items() if price >= 1.0}
print("prices:", prices)
print("expensive (>= 1.0):", expensive)


print("\n=== TRANSFORMING VALUES IN DICT COMPREHENSION ===")

# Add tax to each price
TAX_RATE = 0.1
with_tax = {fruit: round(price * (1 + TAX_RATE), 2) for fruit, price in prices.items()}
print("with_tax:", with_tax)

# Normalize string keys (e.g., upper-case)
mixed_case = {"Apple": 1, "banana": 2, "CHERRY": 3}
upper_keys = {k.upper(): v for k, v in mixed_case.items()}
print("mixed_case:", mixed_case)
print("upper_keys:", upper_keys)


print("\n=== IF-ELSE IN VALUE EXPRESSION ===")
# {k: (expr_if_true if condition else expr_if_false) for ...}

scores = {"Alice": 85, "Bob": 72, "Charlie": 90, "Diana": 60}
grade = {
    name: ("A" if score >= 80 else "B" if score >= 70 else "C")
    for name, score in scores.items()
}
print("scores:", scores)
print("grade:", grade)


print("\n=== DICT COMPREHENSION FROM LIST WITH INDEX ===")

names = ["Alice", "Bob", "Charlie"]
index_map = {i: name for i, name in enumerate(names, start=1)}
print("names:", names)
print("index_map:", index_map)


print("\n=== NESTED DICT COMPREHENSIONS ===")

# Create multiplication table as nested dict: table[i][j] = i * j
table = {
    i: {j: i * j for j in range(1, 4)}
    for i in range(1, 4)
}
print("multiplication table (1..3 x 1..3):")
for i, row in table.items():
    print(i, "->", row)


print("\n=== DICT COMPREHENSION FROM TWO LISTS ===")

keys = ["name", "age", "city"]
values = ["Alice", 30, "Paris"]

combined = {k: v for k, v in zip(keys, values)}
print("keys:", keys)
print("values:", values)
print("combined:", combined)


print("\n=== FILTERING EXISTING DICT BY KEYS ===")

config = {
    "host": "localhost",
    "port": 8080,
    "debug": True,
    "timeout": 30,
    "retries": 3,
}

# Keep only certain keys
selected_keys = {"host", "port", "timeout"}
filtered_config = {k: v for k, v in config.items() if k in selected_keys}
print("config:", config)
print("filtered_config:", filtered_config)


print("\n=== COMPOSING DICT COMPREHENSIONS WITH CONDITIONS ===")

data = {"a": 1, "b": -2, "c": 3, "d": -4, "e": 0}
# Keep only positive values and square them
positive_squares = {k: v * v for k, v in data.items() if v > 0}
print("data:", data)
print("positive_squares:", positive_squares)


print("\n=== SUMMARY ===")
print("Dictionary comprehensions create dicts from iterables or existing dicts.")
print("You can transform keys and values, filter with an 'if' at the end,")
print("and use inline if-else expressions in the value part when needed.")
