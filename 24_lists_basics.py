# Python Lists - Complete Basics Reference
# Ordered, mutable collections of items

# === LIST CREATION ===
print("=== LIST CREATION ===")
empty_list = []
print(f"Empty list: {empty_list}")

numbers = [1, 2, 3, 4, 5]
print(f"Numbers: {numbers}")

mixed = [1, "hello", 3.14, True, None]
print(f"Mixed types: {mixed}")

nested = [[1, 2], [3, 4], [5, 6]]
print(f"Nested: {nested}")

# Using list() constructor
from_list = list([10, 20, 30])
print(f"From list: {from_list}")

from_string = list("hello")
print(f"From string: {from_string}")

from_range = list(range(5))
print(f"From range: {from_range}")


# === LIST INDEXING ===
print("\n=== LIST INDEXING ===")
fruits = ["apple", "banana", "cherry", "date"]

print(f"fruits[0]: {fruits[0]}")      # First element
print(f"fruits[1]: {fruits[1]}")      # Second element
print(f"fruits[-1]: {fruits[-1]}")    # Last element
print(f"fruits[-2]: {fruits[-2]}")    # Second to last

# Indexing nested lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"matrix[0][0]: {matrix[0][0]}")  # First row, first column
print(f"matrix[1][2]: {matrix[1][2]}")  # Second row, third column


# === LIST SLICING ===
print("\n=== LIST SLICING ===")
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"numbers[2:5]: {numbers[2:5]}")      # Elements 2, 3, 4
print(f"numbers[:5]: {numbers[:5]}")        # First 5 elements
print(f"numbers[5:]: {numbers[5:]}")        # Elements from index 5 to end
print(f"numbers[:]: {numbers[:]}")          # Copy of entire list
print(f"numbers[::2]: {numbers[::2]}")      # Every second element
print(f"numbers[1::2]: {numbers[1::2]}")    # Every second element starting at 1
print(f"numbers[::-1]: {numbers[::-1]}")    # Reversed list
print(f"numbers[-3:]: {numbers[-3:]}")      # Last 3 elements
print(f"numbers[:-3]: {numbers[:-3]}")      # All except last 3


# === LIST MODIFICATION (MUTABLE) ===
print("\n=== LIST MODIFICATION ===")
fruits = ["apple", "banana", "cherry"]
print(f"Original: {fruits}")

# Change element
fruits[0] = "apricot"
print(f"After fruits[0] = 'apricot': {fruits}")

# Change slice
fruits[1:3] = ["blueberry", "blackberry"]
print(f"After slice assignment: {fruits}")

# Replace with more elements
fruits[1:2] = ["x", "y", "z"]
print(f"Replace one with three: {fruits}")

# Replace with fewer elements
fruits[1:4] = ["single"]
print(f"Replace three with one: {fruits}")


# === LIST CONCATENATION ===
print("\n=== LIST CONCATENATION ===")
list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined = list1 + list2
print(f"list1 + list2: {combined}")

# In-place concatenation
list1 += list2
print(f"list1 += list2: {list1}")


# === LIST REPETITION ===
print("\n=== LIST REPETITION ===")
original = [1, 2]
repeated = original * 3
print(f"[1, 2] * 3: {repeated}")

# In-place repetition
original *= 2
print(f"After *= 2: {original}")


# === LIST LENGTH ===
print("\n=== LIST LENGTH ===")
fruits = ["apple", "banana", "cherry"]
print(f"len(fruits): {len(fruits)}")

empty = []
print(f"len(empty): {len(empty)}")

nested = [[1, 2], [3, 4]]
print(f"len(nested): {len(nested)}")  # Number of sublists, not total elements


# === LIST MEMBERSHIP ===
print("\n=== LIST MEMBERSHIP ===")
fruits = ["apple", "banana", "cherry"]

print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'mango' in fruits: {'mango' in fruits}")
print(f"'banana' not in fruits: {'banana' not in fruits}")


# === LIST COPYING (SHALLOW) ===
print("\n=== LIST COPYING ===")
original = [1, 2, 3]

# Copy with slice
copy1 = original[:]
print(f"Copy with slice: {copy1}")

# Copy with list()
copy2 = list(original)
print(f"Copy with list(): {copy2}")

# Copy with copy() method
copy3 = original.copy()
print(f"Copy with copy(): {copy3}")

# Verify they are different objects
print(f"original is copy1: {original is copy1}")
print(f"original == copy1: {original == copy1}")

# Modify copy
copy1[0] = 99
print(f"After modifying copy1[0] = 99:")
print(f"original: {original}")
print(f"copy1: {copy1}")


# === SHALLOW VS DEEP COPY ===
print("\n=== SHALLOW VS DEEP COPY ===")
import copy

original = [[1, 2], [3, 4]]
shallow = original.copy()
deep = copy.deepcopy(original)

print(f"Original: {original}")
print(f"Shallow: {shallow}")
print(f"Deep: {deep}")

# Modify original sublist
original[0][0] = 99
print(f"\nAfter original[0][0] = 99:")
print(f"Original: {original}")
print(f"Shallow: {shallow}")  # Also changed (shallow copy)
print(f"Deep: {deep}")        # Unchanged (deep copy)


# === LIST ITERATION ===
print("\n=== LIST ITERATION ===")
fruits = ["apple", "banana", "cherry"]

print("For loop:")
for fruit in fruits:
    print(f"  {fruit}")

print("\nWhile loop:")
i = 0
while i < len(fruits):
    print(f"  {fruits[i]}")
    i += 1

print("\nList comprehension iteration:")
[print(f"  {fruit}") for fruit in fruits]


# === LIST COMPARISON ===
print("\n=== LIST COMPARISON ===")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [3, 2, 1]

print(f"list1 == list2: {list1 == list2}")  # True (same elements)
print(f"list1 == list3: {list1 == list3}")  # False (different order)
print(f"list1 is list2: {list1 is list2}")  # False (different objects)


# === NESTED LIST OPERATIONS ===
print("\n=== NESTED LIST OPERATIONS ===")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Access nested elements
print(f"matrix[0][0]: {matrix[0][0]}")
print(f"matrix[1][2]: {matrix[1][2]}")

# Modify nested elements
matrix[0][0] = 10
print(f"After matrix[0][0] = 10: {matrix}")

# Add row
matrix.append([10, 11, 12])
print(f"After append row: {matrix}")

# Add column (using comprehension)
for row in matrix:
    row.append(0)
print(f"After adding column of zeros: {matrix}")


# === LIST BOOLEAN CONTEXT ===
print("\n=== LIST BOOLEAN CONTEXT ===")
# Empty list is falsy, non-empty is truthy
empty = []
non_empty = [1, 2, 3]

print(f"bool([]): {bool(empty)}")
print(f"bool([1,2,3]): {bool(non_empty)}")

if non_empty:
    print("List has elements")
else:
    print("List is empty")


# === LIST TYPE CHECKING ===
print("\n=== LIST TYPE CHECKING ===")
fruits = ["apple", "banana", "cherry"]

print(f"type(fruits): {type(fruits)}")
print(f"isinstance(fruits, list): {isinstance(fruits, list)}")
print(f"isinstance(fruits, (list, tuple)): {isinstance(fruits, (list, tuple))}")


# === LIST FROM STRING SPLITTING ===
print("\n=== LIST FROM STRING SPLITTING ===")
text = "apple,banana,cherry"
fruits = text.split(",")
print(f"'{text}'.split(','): {fruits}")

text2 = "hello world python"
words = text2.split()
print(f"'{text2}'.split(): {words}")


# === LIST TO STRING JOINING ===
print("\n=== LIST TO STRING JOINING ===")
fruits = ["apple", "banana", "cherry"]
joined = ", ".join(fruits)
print(f"', '.join(fruits): {joined}")

words = ["hello", "world", "python"]
sentence = " ".join(words)
print(f"' '.join(words): {sentence}")


# === LIST DELETION ===
print("\n=== LIST DELETION ===")
numbers = [0, 1, 2, 3, 4, 5]

# Delete by index
del numbers[0]
print(f"After del numbers[0]: {numbers}")

# Delete slice
numbers = [0, 1, 2, 3, 4, 5]
del numbers[2:4]
print(f"After del numbers[2:4]: {numbers}")

# Delete entire list
temp = [1, 2, 3]
del temp
# print(temp)  # Would raise NameError


# === LIST SORTING (BASICS) ===
print("\n=== LIST SORTING (BASICS) ===")
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {numbers}")

# Sort in-place
numbers.sort()
print(f"After sort(): {numbers}")

# Sorted returns new list
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_numbers = sorted(numbers)
print(f"sorted(numbers): {sorted_numbers}")
print(f"Original unchanged: {numbers}")


# === LIST REVERSING (BASICS) ===
print("\n=== LIST REVERSING (BASICS) ===")
numbers = [1, 2, 3, 4, 5]
print(f"Original: {numbers}")

# Reverse in-place
numbers.reverse()
print(f"After reverse(): {numbers}")

# Reversed returns iterator
numbers = [1, 2, 3, 4, 5]
reversed_numbers = list(reversed(numbers))
print(f"list(reversed(numbers)): {reversed_numbers}")
print(f"Original unchanged: {numbers}")


# === LIST CLEAR ===
print("\n=== LIST CLEAR ===")
numbers = [1, 2, 3, 4, 5]
print(f"Before clear: {numbers}")

numbers.clear()
print(f"After clear(): {numbers}")

# Alternative clear
numbers = [1, 2, 3]
del numbers[:]  # Delete all elements via slice
print(f"After del[:]: {numbers}")


# === LIST COUNT ===
print("\n=== LIST COUNT ===")
numbers = [1, 2, 2, 3, 2, 4, 5, 2]
print(f"numbers: {numbers}")
print(f"numbers.count(2): {numbers.count(2)}")
print(f"numbers.count(99): {numbers.count(99)}")


# === LIST INDEX ===
print("\n=== LIST INDEX ===")
fruits = ["apple", "banana", "cherry", "banana"]
print(f"fruits: {fruits}")
print(f"fruits.index('banana'): {fruits.index('banana')}")  # First occurrence
print(f"fruits.index('banana', 2): {fruits.index('banana', 2)}")  # Start from index 2


# === LIST AS STACK (LIFO) ===
print("\n=== LIST AS STACK ===")
stack = []
print(f"Empty stack: {stack}")

# Push (append)
stack.append(1)
stack.append(2)
stack.append(3)
print(f"After pushes: {stack}")

# Pop
popped = stack.pop()
print(f"Popped: {popped}")
print(f"After pop: {stack}")


# === LIST AS QUEUE (FIFO) ===
print("\n=== LIST AS QUEUE ===")
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print(f"Queue: {queue}")

# Dequeue
dequeued = queue.popleft()
print(f"Dequeued: {dequeued}")
print(f"After dequeue: {queue}")


# === LIST PERFORMANCE CHARACTERISTICS ===
print("\n=== PERFORMANCE CHARACTERISTICS ===")
print("Indexing: O(1) - constant time")
print("Append: O(1) amortized")
print("Pop end: O(1)")
print("Pop middle: O(n)")
print("Insert: O(n)")
print("Remove: O(n)")
print("Search (in): O(n)")
print("Sort: O(n log n)")


# === LIST BEST PRACTICES ===
print("\n=== BEST PRACTICES ===")
# Use list comprehension for transformations
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(f"Squares via comprehension: {squares}")

# Use enumerate for index + value
for idx, val in enumerate(numbers):
    print(f"Index {idx}: {val}")

# Use zip for parallel iteration
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for n, c in zip(list1, list2):
    print(f"{n}: {c}")

# Don't modify list while iterating (use copy or comprehension)
numbers = [1, 2, 3, 4, 5]
# Bad: for x in numbers: numbers.remove(x)
# Good:
filtered = [x for x in numbers if x > 2]
print(f"Filtered safely: {filtered}")
