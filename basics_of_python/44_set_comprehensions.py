# Python Set Comprehensions - Syntax and Examples

print("=== BASIC SET COMPREHENSION ===")
# {expression for item in iterable}

numbers = [1, 2, 2, 3, 4, 4, 5]
squares_set = {n * n for n in numbers}
print("numbers:", numbers)
print("squares_set:", squares_set)
# Note: set has unique elements, order is not guaranteed.


print("\n=== SET COMPREHENSION WITH CONDITION ===")
# {expression for item in iterable if condition}

numbers = range(10)
even_squares = {n * n for n in numbers if n % 2 == 0}
print("numbers:", list(numbers))
print("even_squares:", even_squares)

# Unique vowels from a string
text = "set comprehensions are cool"
vowels = {ch for ch in text if ch in "aeiou"}
print("text:", text)
print("vowels set:", vowels)


print("\n=== SET COMPREHENSION FROM DICT DATA ===")

prices = {"apple": 1.2, "banana": 0.5, "cherry": 2.0, "date": 3.5}
# Get set of fruits with price >= 1.0
expensive_fruits = {name for name, price in prices.items() if price >= 1.0}
print("prices:", prices)
print("expensive_fruits:", expensive_fruits)

# Set of price buckets (e.g., floor of price)
buckets = {int(price) for price in prices.values()}
print("price buckets:", buckets)


print("\n=== SET COMPREHENSIONS TO REMOVE DUPLICATES ===")

items = ["apple", "banana", "apple", "cherry", "banana", "date"]
unique_items = {item for item in items}
print("items:", items)
print("unique_items:", unique_items)


print("\n=== NESTED SET COMPREHENSIONS (PAIR GENERATION) ===")

rows = [1, 2, 3]
cols = ["A", "B", "C"]

pairs_set = {(r, c) for r in rows for c in cols}
print("rows:", rows)
print("cols:", cols)
print("pairs_set:", pairs_set)

# Filter pairs with even row only
even_row_pairs = {(r, c) for r in rows for c in cols if r % 2 == 0}
print("even_row_pairs:", even_row_pairs)


print("\n=== USING SET COMPREHENSIONS FOR MEMBERSHIP PRECOMPUTATION ===")

words = ["apple", "banana", "cherry", "date", "elderberry"]
short_word_first_letters = {w[0] for w in words if len(w) <= 5}
print("words:", words)
print("short_word_first_letters:", short_word_first_letters)

# Later: quick membership test
print("'a' in short_word_first_letters:", "a" in short_word_first_letters)
print("'e' in short_word_first_letters:", "e" in short_word_first_letters)


print("\n=== SET VS LIST COMPREHENSION ===")

numbers = [1, 2, 2, 3, 3, 3]
list_comp = [n * n for n in numbers]   # keeps duplicates
set_comp = {n * n for n in numbers}    # removes duplicates

print("list_comp (keeps duplicates):", list_comp)
print("set_comp (unique):           ", set_comp)


print("\n=== SUMMARY ===")
print("Set comprehensions use {expr for item in iterable} syntax,")
print("similar to list comprehensions but produce sets (unique elements).")
print("They are ideal for deduplicating, building lookup sets,")
print("and performing simple transformations with optional filtering.")
