# Python List Methods - Complete Reference
# All built-in list methods with examples

# === APPEND() ===
print("=== APPEND() ===")
fruits = ["apple", "banana"]
fruits.append("cherry")
print(f"After append: {fruits}")

# Append adds a single element
fruits.append(["date", "elderberry"])  # Adds as nested list
print(f"After appending list: {fruits}")


# === EXTEND() ===
print("\n=== EXTEND() ===")
fruits = ["apple", "banana"]
fruits.extend(["cherry", "date"])
print(f"After extend: {fruits}")

# Extend adds multiple elements (unpacks iterable)
fruits.extend("xyz")  # Adds each character as separate element
print(f"After extend string: {fruits}")


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
fruits.remove("banana")  # Removes first occurrence
print(f"After remove('banana'): {fruits}")

# Remove raises ValueError if not found
# fruits.remove("mango")  # ValueError: list.remove(x): x not in list


# === POP() ===
print("\n=== POP() ===")
fruits = ["apple", "banana", "cherry"]
last = fruits.pop()  # Remove and return last element
print(f"Popped: {last}, List: {fruits}")

# Pop from specific index
first = fruits.pop(0)  # Remove and return first element
print(f"Popped index 0: {first}, List: {fruits}")

# Pop from empty list raises IndexError
# empty = []
# empty.pop()  # IndexError: pop from empty list


# === CLEAR() ===
print("\n=== CLEAR() ===")
fruits = ["apple", "banana", "cherry"]
print(f"Before clear: {fruits}")
fruits.clear()
print(f"After clear(): {fruits}")

# Alternative clear method
fruits = ["apple", "banana", "cherry"]
del fruits[:]  # Delete all elements via slice assignment
print(f"After del[:]: {fruits}")


# === INDEX() ===
print("\n=== INDEX() ===")
fruits = ["apple", "banana", "cherry", "banana"]
print(f"fruits: {fruits}")
print(f"fruits.index('banana'): {fruits.index('banana')}")  # First occurrence
print(f"fruits.index('banana', 2): {fruits.index('banana', 2)}")  # Start from index 2
print(f"fruits.index('banana', 0, 3): {fruits.index('banana', 0, 3)}")  # Search in range

# Index raises ValueError if not found
# print(fruits.index("mango"))  # ValueError: 'mango' is not in list


# === COUNT() ===
print("\n=== COUNT() ===")
numbers = [1, 2, 2, 3, 2, 4, 5, 2]
print(f"numbers: {numbers}")
print(f"numbers.count(2): {numbers.count(2)}")
print(f"numbers.count(99): {numbers.count(99)}")


# === SORT() ===
print("\n=== SORT() ===")
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {numbers}")
numbers.sort()
print(f"After sort(): {numbers}")  # In-place sort

# Sort in reverse
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort(reverse=True)
print(f"After sort(reverse=True): {numbers}")

# Sort with key function
words = ["apple", "banana", "cherry", "date"]
words.sort(key=len)  # Sort by length
print(f"Sorted by length: {words}")

# Sort case-insensitive
mixed_case = ["Apple", "banana", "Cherry", "date"]
mixed_case.sort(key=str.lower)
print(f"Case-insensitive sort: {mixed_case}")


# === REVERSE() ===
print("\n=== REVERSE() ===")
numbers = [1, 2, 3, 4, 5]
print(f"Original: {numbers}")
numbers.reverse()
print(f"After reverse(): {numbers}")  # In-place reverse


# === COPY() ===
print("\n=== COPY() ===")
original = [1, 2, 3]
copy = original.copy()
print(f"Original: {original}")
print(f"Copy: {copy}")
print(f"Are same object: {original is copy}")
print(f"Have same values: {original == copy}")

# Modify copy
copy[0] = 99
print(f"After modifying copy[0] = 99:")
print(f"Original: {original}")
print(f"Copy: {copy}")


# === EXTEND() VS APPEND() COMPARISON ===
print("\n=== EXTEND() VS APPEND() ===")
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Append adds as single element
list1_append = [1, 2, 3]
list1_append.append([4, 5, 6])
print(f"After append: {list1_append}")  # [1, 2, 3, [4, 5, 6]]

# Extend adds each element
list1_extend = [1, 2, 3]
list1_extend.extend([4, 5, 6])
print(f"After extend: {list1_extend}")  # [1, 2, 3, 4, 5, 6]


# === METHODS RETURN VALUES ===
print("\n=== METHODS RETURN VALUES ===")
fruits = ["apple", "banana", "cherry"]

# Some methods return values
popped = fruits.pop()
print(f"pop() returned: {popped}, list now: {fruits}")

count = fruits.count("banana")
print(f"count() returned: {count}")

index = fruits.index("banana")
print(f"index() returned: {index}")

# Some methods return None (modify in-place)
result = fruits.sort()
print(f"sort() returned: {result}, list now: {fruits}")

result = fruits.reverse()
print(f"reverse() returned: {result}, list now: {fruits}")

result = fruits.append("date")
print(f"append() returned: {result}, list now: {fruits}")


# === METHOD CHAINING ===
print("\n=== METHOD CHAINING ===")
# Some methods return None, so they can't be chained directly
# But you can chain operations

# Instead of chaining (doesn't work):
# fruits.append("x").append("y")  # AttributeError: 'NoneType' object has no attribute 'append'

# Do this:
fruits = ["apple", "banana"]
fruits.append("cherry")
fruits.append("date")
print(f"After sequential calls: {fruits}")

# Or use list comprehension for transformations
numbers = [1, 2, 3, 4, 5]
result = sorted([x * 2 for x in numbers], reverse=True)
print(f"Transformation and sort: {result}")


# === ALL LIST METHODS SUMMARY ===
print("\n=== ALL LIST METHODS SUMMARY ===")
fruits = ["apple", "banana", "cherry"]

print("Available methods:")
for method in dir(list):
    if not method.startswith('_'):
        print(f"  {method}")

print(f"\nTotal methods: {len([m for m in dir(list) if not m.startswith('_')])}")


# === PRACTICAL: COMMON OPERATIONS ===
print("\n=== PRACTICAL: COMMON OPERATIONS ===")

# 1. Remove all occurrences of an item
numbers = [1, 2, 3, 2, 4, 2, 5]
target = 2
while target in numbers:
    numbers.remove(target)
print(f"After removing all {target}: {numbers}")

# 2. Move item to end
fruits = ["apple", "banana", "cherry", "date"]
fruit_to_move = "banana"
if fruit_to_move in fruits:
    fruits.remove(fruit_to_move)
    fruits.append(fruit_to_move)
print(f"Moved '{fruit_to_move}' to end: {fruits}")

# 3. Insert at sorted position
numbers = [1, 3, 5, 7, 9]
new_num = 4
numbers.append(new_num)
numbers.sort()
print(f"Inserted {new_num} in sorted order: {numbers}")

# 4. Remove duplicates while preserving order
items = ["a", "b", "a", "c", "b", "d"]
unique = []
for item in items:
    if item not in unique:
        unique.append(item)
print(f"Original: {items}")
print(f"Unique (preserved order): {unique}")


# === PERFORMANCE COMPARISON ===
print("\n=== PERFORMANCE COMPARISON ===")
import time

# Append vs Insert at beginning
size = 10000

# Append (fast)
start = time.time()
lst = []
for i in range(size):
    lst.append(i)
append_time = time.time() - start

# Insert at beginning (slow)
start = time.time()
lst = []
for i in range(size):
    lst.insert(0, i)
insert_time = time.time() - start

print(f"Append {size} items: {append_time:.4f}s")
print(f"Insert at beginning {size} items: {insert_time:.4f}s")
print(f"Insert is {insert_time/append_time:.1f}x slower")


# === METHOD ALIASES AND ALTERNATIVES ===
print("\n=== METHOD ALIASES ===")
fruits = ["apple", "banana", "cherry"]

# Remove alternatives
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(f"After remove: {fruits}")

fruits = ["apple", "banana", "cherry"]
del fruits[1]  # Remove by index
print(f"After del fruits[1]: {fruits}")

fruits = ["apple", "banana", "cherry"]
popped = fruits.pop(1)  # Remove and return
print(f"Popped: {popped}, list: {fruits}")
