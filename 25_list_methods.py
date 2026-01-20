# Python List Methods - Complete Reference
# All key built-in list methods with examples

# Methods covered:
# append, extend, insert, remove, pop, clear, index, count, sort, reverse, copy

# === APPEND() ===
print("=== APPEND() ===")
fruits = ["apple", "banana"]
fruits.append("cherry")
print(f"After append: {fruits}")  # ['apple', 'banana', 'cherry']

# Append adds a single element (even if that element is a list)
fruits.append(["date", "elderberry"])  # Adds as nested list
print(f"After appending list: {fruits}")  # ['apple','banana','cherry',['date','elderberry']]


# === EXTEND() ===
print("\n=== EXTEND() ===")
fruits = ["apple", "banana"]
fruits.extend(["cherry", "date"])
print(f"After extend with list: {fruits}")  # ['apple','banana','cherry','date']

# Extend adds each element from the iterable
fruits.extend("xyz")  # Adds each character as separate element
print(f"After extend with string: {fruits}")  # ['apple','banana','cherry','date','x','y','z']


# === INSERT() ===
print("\n=== INSERT() ===")
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "apricot")  # Insert at index 1
print(f"After insert(1, 'apricot'): {fruits}")

# Insert at beginning
fruits.insert(0, "start")
print(f"After insert(0, 'start'): {fruits}")

# Insert at end (equivalent to append)
fruits.insert(len(fruits), "end")
print(f"After insert(len, 'end'): {fruits}")


# === REMOVE() ===
print("\n=== REMOVE() ===")
fruits = ["apple", "banana", "cherry", "banana"]
print(f"Original: {fruits}")
fruits.remove("banana")  # Removes first occurrence
print(f"After remove('banana'): {fruits}")

# Removing non-existing element raises ValueError
# fruits.remove("mango")  # Uncomment to see ValueError


# === POP() ===
print("\n=== POP() ===")
numbers = [10, 20, 30, 40, 50]
print(f"Original: {numbers}")

last = numbers.pop()  # Remove and return last element
print(f"Popped last: {last}, Remaining: {numbers}")

second = numbers.pop(1)  # Remove and return element at index 1
print(f"Popped index 1: {second}, Remaining: {numbers}")

# Popping out of range raises IndexError
# numbers.pop(100)  # Uncomment to see error


# === CLEAR() ===
print("\n=== CLEAR() ===")
items = [1, 2, 3, 4]
print(f"Before clear: {items}")
items.clear()
print(f"After clear(): {items}")  # []


# === INDEX() ===
print("\n=== INDEX() ===")
fruits = ["apple", "banana", "cherry", "banana", "date"]
print(f"fruits: {fruits}")
print(f"fruits.index('banana'): {fruits.index('banana')}")  # First occurrence

# index(value, start, end)
print(f"fruits.index('banana', 2): {fruits.index('banana', 2)}")  # Start search at index 2

# ValueError if not found
# fruits.index("mango")  # Uncomment to see error


# === COUNT() ===
print("\n=== COUNT() ===")
numbers = [1, 2, 2, 3, 2, 4, 2, 5]
print(f"numbers: {numbers}")
print(f"numbers.count(2): {numbers.count(2)}")   # 4
print(f"numbers.count(99): {numbers.count(99)}") # 0


# === SORT() ===
print("\n=== SORT() ===")
numbers = [5, 2, 9, 1, 5, 6]
print(f"Original: {numbers}")

# Sort in-place ascending
numbers.sort()
print(f"After sort(): {numbers}")

# Sort descending
numbers.sort(reverse=True)
print(f"After sort(reverse=True): {numbers}")

# Sort with key function
words = ["banana", "apple", "cherry", "date"]
print(f"\nWords: {words}")
words.sort(key=len)  # Sort by length
print(f"After sort(key=len): {words}")

# Using sorted() (returns new list, original unchanged)
numbers = [3, 1, 4, 1, 5, 9]
sorted_numbers = sorted(numbers)
print(f"\nOriginal numbers: {numbers}")
print(f"sorted(numbers): {sorted_numbers}")
print(f"sorted(numbers, reverse=True): {sorted(numbers, reverse=True)}")

# Custom key: sort words by last character
words = ["apple", "banana", "cherry", "date"]
words.sort(key=lambda x: x[-1])
print(f"\nSort by last character: {words}")


# === REVERSE() ===
print("\n=== REVERSE() ===")
numbers = [1, 2, 3, 4, 5]
print(f"Original: {numbers}")

numbers.reverse()  # In-place reverse
print(f"After reverse(): {numbers}")

# reversed() built-in returns an iterator (non-destructive)
numbers = [1, 2, 3, 4, 5]
rev_iter = reversed(numbers)
print(f"list(reversed(numbers)): {list(rev_iter)}")
print(f"Original unchanged: {numbers}")


# === COPY() ===
print("\n=== COPY() ===")
original = [1, 2, 3]
shallow_copy = original.copy()
print(f"Original: {original}")
print(f"Copy: {shallow_copy}")
print(f"original is shallow_copy: {original is shallow_copy}")
print(f"original == shallow_copy: {original == shallow_copy}")

# With nested lists (shallow copy)
nested_original = [[1, 2], [3, 4]]
nested_copy = nested_original.copy()
print(f"\nNested original: {nested_original}")
print(f"Nested copy: {nested_copy}")
nested_original[0][0] = 99
print("After nested_original[0][0] = 99:")
print(f"Nested original: {nested_original}")
print(f"Nested copy (also changed due to shallow copy): {nested_copy}")


# === COMBINED USAGE EXAMPLES ===

print("\n=== COMBINED: BUILDING AND CLEANING A LIST ===")
data = []
print(f"Start: {data}")

# Collect items
for i in range(1, 6):
    data.append(i)
print(f"After append 1..5: {data}")

# Extend with more
data.extend([6, 7, 8])
print(f"After extend [6,7,8]: {data}")

# Remove specific value
data.remove(3)
print(f"After remove(3): {data}")

# Pop last two
last = data.pop()
second_last = data.pop()
print(f"Popped: {last}, {second_last}, Remaining: {data}")

# Insert at front
data.insert(0, 99)
print(f"After insert(0, 99): {data}")

# Count and index
print(f"Count of 2: {data.count(2)}")
if 2 in data:
    print(f"Index of 2: {data.index(2)}")

# Sort then reverse
data.sort()
print(f"After sort(): {data}")
data.reverse()
print(f"After reverse(): {data}")

# Clear everything
data.clear()
print(f"After clear(): {data}")


print("\n=== PRACTICAL: UNIQUE SORTED WORDS ===")
sentence = "banana apple cherry banana date apple"
words = sentence.split()
print(f"Words: {words}")

# Unique with set, then back to list
unique_words = list(set(words))
print(f"Unique words (unordered): {unique_words}")

# Sort alphabetically
unique_words.sort()
print(f"Unique sorted words: {unique_words}")


print("\n=== PRACTICAL: STABLE SORT WITH KEY ===")
students = [
    ("Alice", 25),
    ("Bob", 20),
    ("Charlie", 25),
    ("Dave", 23),
]

print(f"Original students: {students}")

# Sort by age, stable (keeps relative order of same-age entries)
students.sort(key=lambda s: s[1])
print(f"Sorted by age: {students}")

# Sort by name then by age separately
students.sort(key=lambda s: s[0])  # By name
print(f"Sorted by name: {students}")
