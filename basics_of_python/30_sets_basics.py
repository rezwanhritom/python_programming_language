# Python Sets - Complete Basics Reference
# Unordered collections of unique, hashable elements

# === SET CREATION ===
print("=== SET CREATION ===")

# Empty set (must use set(), {} is an empty dict)
empty_set = set()
print(f"Empty set: {empty_set}, type: {type(empty_set)}")

# Set literal with curly braces
numbers = {1, 2, 3, 4, 5}
print(f"Numbers set: {numbers}")

# Automatic removal of duplicates
duplicates = {1, 2, 2, 3, 3, 3}
print(f"Duplicates removed: {duplicates}")

# Mixed types (all must be hashable)
mixed = {1, "hello", 3.14, True, (1, 2)}
print(f"Mixed set: {mixed}")

# Using set() constructor from list/tuple/string
from_list = set([1, 2, 2, 3, 4])
print(f"From list: {from_list}")

from_tuple = set((1, 2, 3, 3, 4))
print(f"From tuple: {from_tuple}")

from_string = set("banana")
print(f"From string 'banana': {from_string}")

from_range = set(range(5))
print(f"From range(5): {from_range}")


# === BASIC PROPERTIES ===
print("\n=== BASIC PROPERTIES ===")
s = {1, 2, 3, 4, 5}
print(f"Set: {s}")

# Unordered: iteration order is not guaranteed
print("Iterating over set:")
for item in s:
    print(f"  {item}")

# Unique elements only
s = {1, 1, 2, 2, 3, 3}
print(f"Unique elements only: {s}")

# Mutable: can add/remove elements
# But elements themselves must be immutable (hashable)


# === SET LENGTH ===
print("\n=== SET LENGTH ===")
s = {1, 2, 3, 4, 5}
print(f"Set: {s}")
print(f"len(s): {len(s)}")

empty = set()
print(f"len(empty): {len(empty)}")


# === SET MEMBERSHIP ===
print("\n=== SET MEMBERSHIP ===")
fruits = {"apple", "banana", "cherry"}

print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'mango' in fruits: {'mango' in fruits}")
print(f"'banana' not in fruits: {'banana' not in fruits}")

# Membership is O(1) average case (hash table)
large_set = set(range(1000000))
print(f"999999 in large_set: {999999 in large_set}")
print(f"1000000 in large_set: {1000000 in large_set}")


# === ADDING ELEMENTS ===
print("\n=== ADDING ELEMENTS ===")
s = {1, 2, 3}
print(f"Original: {s}")

# add() adds a single element
s.add(4)
print(f"After add(4): {s}")

# Adding existing element has no effect
s.add(3)
print(f"After add(3) again: {s}")

# update() adds multiple elements from any iterable
s.update([5, 6], {7, 8}, (9, 10))
print(f"After update([5, 6], {{7, 8}}, (9, 10)): {s}")

# update() with string (adds each character)
letters = set("ab")
letters.update("bcd")
print(f"Letters set after update('bcd'): {letters}")


# === REMOVING ELEMENTS ===
print("\n=== REMOVING ELEMENTS ===")
s = {1, 2, 3, 4, 5}
print(f"Original: {s}")

# remove() removes element, raises KeyError if not present
s.remove(3)
print(f"After remove(3): {s}")

# discard() removes element if present, does nothing if not
s.discard(2)
print(f"After discard(2): {s}")
s.discard(99)  # No error
print(f"After discard(99) (non-existent): {s}")

# pop() removes and returns an arbitrary element
popped = s.pop()
print(f"Popped element: {popped}")
print(f"After pop(): {s}")

# clear() removes all elements
s.clear()
print(f"After clear(): {s}")


# === SET COPY ===
print("\n=== SET COPY ===")
original = {1, 2, 3}
copy1 = original.copy()
print(f"Original: {original}")
print(f"Copy: {copy1}")
print(f"Same object: {original is copy1}")
print(f"Same values: {original == copy1}")

# Modify copy
copy1.add(4)
print(f"After copy1.add(4):")
print(f"Original: {original}")
print(f"Copy: {copy1}")


# === FROZENSET (IMMUTABLE SET) ===
print("\n=== FROZENSET (IMMUTABLE SET) ===")
# frozenset is an immutable version of set

s = {1, 2, 3}
fs = frozenset(s)
print(f"Set: {s}, type: {type(s)}")
print(f"Frozenset: {fs}, type: {type(fs)}")

# Cannot modify frozenset
# fs.add(4)       # AttributeError: 'frozenset' object has no attribute 'add'
# fs.remove(1)    # AttributeError

# frozenset can be used as dict keys or set elements
d = {fs: "immutable set as key"}
print(f"Dict with frozenset key: {d}")

set_of_frozensets = {frozenset([1, 2]), frozenset([3, 4])}
print(f"Set of frozensets: {set_of_frozensets}")


# === SET BOOLEAN CONTEXT ===
print("\n=== SET BOOLEAN CONTEXT ===")
empty = set()
non_empty = {1, 2, 3}

print(f"bool(empty set): {bool(empty)}")
print(f"bool(non_empty set): {bool(non_empty)}")

if non_empty:
    print("Set has elements")
else:
    print("Set is empty")


# === SET TYPE CHECKING ===
print("\n=== SET TYPE CHECKING ===")
s = {1, 2, 3}
fs = frozenset([1, 2, 3])

print(f"type(s): {type(s)}")
print(f"isinstance(s, set): {isinstance(s, set)}")
print(f"isinstance(s, (set, frozenset)): {isinstance(s, (set, frozenset))}")

print(f"type(fs): {type(fs)}")
print(f"isinstance(fs, frozenset): {isinstance(fs, frozenset)}")
print(f"isinstance(fs, set): {isinstance(fs, set)}")  # False


# === ELEMENT HASHABILITY (VALID SET ELEMENTS) ===
print("\n=== ELEMENT HASHABILITY (VALID SET ELEMENTS) ===")
valid_set = {1, 2.5, "hello", (1, 2), True, None}
print(f"Valid set elements: {valid_set}")

# Invalid elements (unhashable types) cause TypeError
# invalid_set = {[1, 2], {3, 4}}  # TypeError: unhashable type: 'list'/'set'
# s.add([1, 2])                   # TypeError: unhashable type: 'list'

# But tuple containing only hashable elements is fine
s = set()
s.add((1, 2))
print(f"Set with tuple element: {s}")


# === BASIC SET OPERATIONS (PREVIEW) ===
print("\n=== BASIC SET OPERATIONS (PREVIEW) ===")
# Full details will be in 31_set_operations.py

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(f"a: {a}")
print(f"b: {b}")

# Union (| or union())
print(f"a | b: {a | b}")
print(f"a.union(b): {a.union(b)}")

# Intersection (& or intersection())
print(f"a & b: {a & b}")
print(f"a.intersection(b): {a.intersection(b)}")

# Difference (- or difference())
print(f"a - b: {a - b}")
print(f"a.difference(b): {a.difference(b)}")

# Symmetric difference (^ or symmetric_difference())
print(f"a ^ b: {a ^ b}")
print(f"a.symmetric_difference(b): {a.symmetric_difference(b)}")


# === SUBSET / SUPERSET / DISJOINT (PREVIEW) ===
print("\n=== SUBSET / SUPERSET / DISJOINT (PREVIEW) ===")
a = {1, 2}
b = {1, 2, 3, 4}
c = {5, 6}

print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")

# Subset / superset
print(f"a <= b (a is subset of b): {a <= b}")
print(f"b >= a (b is superset of a): {b >= a}")

# Proper subset / superset
print(f"a < b (a is proper subset of b): {a < b}")
print(f"b > a (b is proper superset of a): {b > a}")

# Disjoint sets
print(f"a.isdisjoint(c): {a.isdisjoint(c)}")
print(f"a.isdisjoint(b): {a.isdisjoint(b)}")


# === ITERATING OVER SETS ===
print("\n=== ITERATING OVER SETS ===")
s = {"apple", "banana", "cherry"}

print("For loop:")
for item in s:
    print(f"  {item}")

print("\nEnumerate over set:")
for index, item in enumerate(s):
    print(f"  Index {index}: {item}")


# === SET COMPREHENSIONS (BASICS) ===
print("\n=== SET COMPREHENSIONS (BASICS) ===")
numbers = [1, 2, 2, 3, 4, 4, 5]

# Create set of squares
squares = {n**2 for n in numbers}
print(f"Numbers: {numbers}")
print(f"Squares set: {squares}")

# Filter with condition
even_squares = {n**2 for n in numbers if n % 2 == 0}
print(f"Even squares set: {even_squares}")


# === COMMON USE CASES ===
print("\n=== COMMON USE CASES ===")

# 1. Removing duplicates from a list
print("\n1) Removing duplicates from list:")
items = [1, 2, 2, 3, 4, 4, 5]
unique_items = list(set(items))
print(f"Original: {items}")
print(f"Unique (order not preserved): {unique_items}")

# If you want to preserve order (use dict or loop)
seen = set()
ordered_unique = []
for x in items:
    if x not in seen:
        seen.add(x)
        ordered_unique.append(x)
print(f"Unique (order preserved): {ordered_unique}")

# 2. Fast membership checks
print("\n2) Fast membership checks:")
allowed = {"yes", "y", "ok", "true"}
user_input = "yes"
print(f"'{user_input}' in allowed: {user_input in allowed}")

# 3. Set operations for categories
print("\n3) Category operations:")
frontend = {"HTML", "CSS", "JavaScript"}
backend = {"Python", "JavaScript", "SQL"}

print(f"Frontend: {frontend}")
print(f"Backend: {backend}")
print(f"Full stack (union): {frontend | backend}")
print(f"Common skills (intersection): {frontend & backend}")
print(f"Frontend-only: {frontend - backend}")
print(f"Backend-only: {backend - frontend}")


# === PERFORMANCE NOTES ===
print("\n=== PERFORMANCE NOTES ===")
print("Set operations and membership are O(1) average case (hash table)")
print("Great for:")
print("  - De-duplicating data")
print("  - Membership tests")
print("  - Mathematical set operations (union, intersection, etc.)")
print("Not ordered (before Python 3.7) and no indexing like lists (s[0] is invalid)")

# Trying to index set raises TypeError
s = {1, 2, 3}
# print(s[0])  # TypeError: 'set' object is not subscriptable


# === FINAL SUMMARY ===
print("\n=== FINAL SUMMARY ===")
print("Sets are unordered, mutable collections of UNIQUE elements")
print("Use them when you care about membership and uniqueness, not order")
print("Elements must be hashable (immutable types typically)")
print("frozenset is the immutable version, usable as dict keys or set elements")
