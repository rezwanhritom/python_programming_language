# Python Tuple Methods - Complete Reference
# Tuples have only 2 built-in methods: count() and index()

# === COUNT() METHOD ===
print("=== TUPLE COUNT() METHOD ===")
# count() returns the number of times a specified value appears in the tuple

fruits = ("apple", "banana", "cherry", "apple", "banana", "apple")
print(f"Tuple: {fruits}")
print(f"fruits.count('apple'): {fruits.count('apple')}")
print(f"fruits.count('banana'): {fruits.count('banana')}")
print(f"fruits.count('cherry'): {fruits.count('cherry')}")
print(f"fruits.count('mango'): {fruits.count('mango')}")  # Returns 0 if not found

# Count with nested tuples
nested = ((1, 2), (3, 4), (1, 2), (5, 6))
print(f"\nNested tuple: {nested}")
print(f"nested.count((1, 2)): {nested.count((1, 2))}")

# Count with mixed types
mixed = (1, "hello", 3.14, 1, "hello", 1)
print(f"\nMixed tuple: {mixed}")
print(f"mixed.count(1): {mixed.count(1)}")  # Counts integer 1 only
print(f"mixed.count('hello'): {mixed.count('hello')}")
print(f"mixed.count(3.14): {mixed.count(3.14)}")


# === INDEX() METHOD ===
print("\n=== TUPLE INDEX() METHOD ===")
# index() returns the index of the first occurrence of a specified value

fruits = ("apple", "banana", "cherry", "date", "banana")
print(f"Tuple: {fruits}")
print(f"fruits.index('apple'): {fruits.index('apple')}")
print(f"fruits.index('banana'): {fruits.index('banana')}")  # First occurrence
print(f"fruits.index('date'): {fruits.index('date')}")

# Index with start parameter
print(f"\nfruits.index('banana', 2): {fruits.index('banana', 2)}")  # Start searching from index 2

# Index with start and end parameters
print(f"fruits.index('banana', 1, 4): {fruits.index('banana', 1, 4)}")  # Search between indices 1 and 4


# === INDEX() ERROR HANDLING ===
print("\n=== INDEX() ERROR HANDLING ===")
fruits = ("apple", "banana", "cherry")

try:
    index = fruits.index("mango")
    print(f"Index of 'mango': {index}")
except ValueError as e:
    print(f"ValueError: {e}")  # 'mango' is not in tuple

try:
    index = fruits.index("banana", 3)  # Start beyond where banana exists
    print(f"Index: {index}")
except ValueError as e:
    print(f"ValueError: {e}")  # 'banana' is not in tuple


# === BUILT-IN FUNCTIONS THAT WORK WITH TUPLES ===
print("\n=== BUILT-IN FUNCTIONS WITH TUPLES ===")
# While not methods, these are commonly used with tuples

numbers = (3, 1, 4, 1, 5, 9, 2, 6)

print(f"Tuple: {numbers}")
print(f"len(numbers): {len(numbers)}")
print(f"min(numbers): {min(numbers)}")
print(f"max(numbers): {max(numbers)}")
print(f"sum(numbers): {sum(numbers)}")
print(f"sorted(numbers): {sorted(numbers)}")  # Returns list
print(f"tuple(sorted(numbers)): {tuple(sorted(numbers))}")  # Convert back to tuple


# === ANY() AND ALL() WITH TUPLES ===
print("\n=== ANY() AND ALL() WITH TUPLES ===")
mixed = (0, 1, "", "hello", False, True)

print(f"Tuple: {mixed}")
print(f"any(mixed): {any(mixed)}")  # True if at least one element is truthy
print(f"all(mixed): {all(mixed)}")  # True if all elements are truthy

# With all truthy values
all_true = (1, 2, 3, "hello", True)
print(f"\nall_true: {all_true}")
print(f"any(all_true): {any(all_true)}")
print(f"all(all_true): {all(all_true)}")


# === ENUMERATE() WITH TUPLES ===
print("\n=== ENUMERATE() WITH TUPLES ===")
fruits = ("apple", "banana", "cherry")

for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")


# === ZIP() WITH TUPLES ===
print("\n=== ZIP() WITH TUPLES ===")
names = ("Alice", "Bob", "Charlie")
ages = (25, 30, 35)

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Create tuple of tuples
zipped_tuple = tuple(zip(names, ages))
print(f"Zipped tuple: {zipped_tuple}")


# === PRACTICAL EXAMPLES ===

# 1. Using count() to analyze data
print("\n=== PRACTICAL: DATA ANALYSIS WITH COUNT() ===")
responses = ("yes", "no", "yes", "yes", "no", "maybe", "yes", "no")
print(f"Responses: {responses}")
print(f"'yes' count: {responses.count('yes')}")
print(f"'no' count: {responses.count('no')}")
print(f"'maybe' count: {responses.count('maybe')}")


# 2. Using index() to find positions
print("\n=== PRACTICAL: FINDING POSITIONS WITH INDEX() ===")
grades = ("A", "B", "C", "D", "F", "B", "A", "C")
target_grade = "C"
first_occurrence = grades.index(target_grade)
print(f"First '{target_grade}' at index: {first_occurrence}")

# Find all occurrences
print(f"All positions of '{target_grade}':")
for i, grade in enumerate(grades):
    if grade == target_grade:
        print(f"  Index {i}")


# 3. Finding duplicate elements
print("\n=== PRACTICAL: FINDING DUPLICATES ===")
numbers = (1, 2, 3, 2, 4, 5, 2, 3, 6)
duplicates = []

for num in set(numbers):
    count = numbers.count(num)
    if count > 1:
        duplicates.append((num, count))

print(f"Original tuple: {numbers}")
print(f"Duplicates (number, count): {duplicates}")


# 4. Tuple comparison using count()
print("\n=== PRACTICAL: TUPLE COMPARISON ===")
tuple1 = ("a", "b", "c", "a")
tuple2 = ("a", "b", "c", "d")

print(f"tuple1: {tuple1}")
print(f"tuple2: {tuple2}")
print(f"Both have same 'a' count: {tuple1.count('a') == tuple2.count('a')}")
print(f"Both have same 'b' count: {tuple1.count('b') == tuple2.count('b')}")
print(f"Both have same length: {len(tuple1) == len(tuple2)}")


# 5. Safe index lookup with try/except
print("\n=== PRACTICAL: SAFE INDEX LOOKUP ===")
def safe_index(tup, value, start=0, end=None):
    """Return index of value or -1 if not found"""
    try:
        if end is None:
            return tup.index(value, start)
        else:
            return tup.index(value, start, end)
    except ValueError:
        return -1

fruits = ("apple", "banana", "cherry")
print(f"fruits: {fruits}")
print(f"safe_index(fruits, 'banana'): {safe_index(fruits, 'banana')}")
print(f"safe_index(fruits, 'mango'): {safe_index(fruits, 'mango')}")
print(f"safe_index(fruits, 'banana', 2): {safe_index(fruits, 'banana', 2)}")


# === METHOD LIMITATIONS DUE TO IMMUTABILITY ===
print("\n=== IMMUTABILITY LIMITATIONS ===")
# Tuples don't have these methods (because they're immutable):
# append(), extend(), insert(), remove(), pop(), clear(), sort(), reverse()

print("Tuples are immutable, so they lack:")
print("  - append(), extend(), insert()")
print("  - remove(), pop(), clear()")
print("  - sort(), reverse()")

print("\nIf you need these operations, use a list instead:")
temp_list = list(fruits)
temp_list.append("date")
new_tuple = tuple(temp_list)
print(f"Converted to list, appended, converted back: {new_tuple}")


# === PERFORMANCE COMPARISON ===
print("\n=== PERFORMANCE COMPARISON ===")
import time

large_tuple = tuple(range(10000))

# count() performance
start = time.time()
count = large_tuple.count(5000)
count_time = time.time() - start
print(f"count() in large tuple: {count_time:.6f}s")

# index() performance
start = time.time()
try:
    index = large_tuple.index(5000)
    index_time = time.time() - start
    print(f"index() in large tuple: {index_time:.6f}s")
except:
    print("Element not found")

# Built-in functions performance
start = time.time()
length = len(large_tuple)
len_time = time.time() - start
print(f"len() in large tuple: {len_time:.6f}s")


# === FINAL SUMMARY ===
print("\n=== FINAL SUMMARY ===")
print("Tuple has only 2 methods:")
print("  1. count(value) - returns occurrence count")
print("  2. index(value, [start], [end]) - returns first index")
print("\nCommon built-in functions:")
print("  - len(), min(), max(), sum(), sorted()")
print("  - any(), all(), enumerate(), zip()")
print("\nTuples are immutable - no modification methods")
