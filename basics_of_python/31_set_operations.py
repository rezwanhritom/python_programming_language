# Python Set Operations - Complete Reference
# Mathematical set operations for sets and frozensets

# === UNION OPERATION ===
print("=== UNION OPERATION ===")
# Union: all unique elements from both sets (| or union())

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = {7, 8}

print(f"set1: {set1}")
print(f"set2: {set2}")
print(f"set1 | set2: {set1 | set2}")
print(f"set1.union(set2): {set1.union(set2)}")

# Union with multiple sets
print(f"set1 | set2 | set3: {set1 | set2 | set3}")
print(f"set1.union(set2, set3): {set1.union(set2, set3)}")

# union() returns new set (original unchanged)
print(f"set1 unchanged: {set1}")

# update() modifies in-place
set1.update(set2)
print(f"After set1.update(set2): {set1}")


# === INTERSECTION OPERATION ===
print("\n=== INTERSECTION OPERATION ===")
# Intersection: common elements (& or intersection())

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
set3 = {5, 6, 7, 8}

print(f"set1: {set1}")
print(f"set2: {set2}")
print(f"set1 & set2: {set1 & set2}")
print(f"set1.intersection(set2): {set1.intersection(set2)}")

# Multiple intersection
print(f"set1 & set2 & set3: {set1 & set2 & set3}")
print(f"set1.intersection(set2, set3): {set1.intersection(set2, set3)}")

# intersection_update() modifies in-place
set1 = {1, 2, 3, 4, 5}
set1.intersection_update(set2)
print(f"After intersection_update(set2): {set1}")


# === DIFFERENCE OPERATION ===
print("\n=== DIFFERENCE OPERATION ===")
# Difference: elements in first set but not in second (- or difference())

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
set3 = {5, 6}

print(f"set1: {set1}")
print(f"set2: {set2}")
print(f"set1 - set2: {set1 - set2}")
print(f"set1.difference(set2): {set1.difference(set2)}")

# Order matters for difference
print(f"set2 - set1: {set2 - set1}")

# Multiple difference
print(f"set1 - set2 - set3: {set1 - set2 - set3}")
print(f"set1.difference(set2, set3): {set1.difference(set2, set3)}")

# difference_update() modifies in-place
set1 = {1, 2, 3, 4, 5}
set1.difference_update(set2)
print(f"After difference_update(set2): {set1}")


# === SYMMETRIC DIFFERENCE OPERATION ===
print("\n=== SYMMETRIC DIFFERENCE OPERATION ===")
# Symmetric difference: elements in exactly one set (^ or symmetric_difference())

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(f"set1: {set1}")
print(f"set2: {set2}")
print(f"set1 ^ set2: {set1 ^ set2}")
print(f"set1.symmetric_difference(set2): {set1.symmetric_difference(set2)}")

# symmetric_difference_update() modifies in-place
set1 = {1, 2, 3, 4}
set1.symmetric_difference_update(set2)
print(f"After symmetric_difference_update(set2): {set1}")


# === SUBSET CHECKING ===
print("\n=== SUBSET CHECKING ===")
# subset: all elements of set are in another (<= or issubset())

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
set3 = {4, 5, 6}

print(f"set1: {set1}")
print(f"set2: {set2}")
print(f"set3: {set3}")
print(f"set1 <= set2 (subset): {set1 <= set2}")
print(f"set1.issubset(set2): {set1.issubset(set2)}")

print(f"set2 <= set1: {set2 <= set1}")  # False

# Proper subset (<)
print(f"set1 < set2 (proper subset): {set1 < set2}")  # True (set1 is strict subset)
print(f"set1 < set1: {set1 < set1}")  # False (not proper)

# Multiple sets in issubset()
set1 = {1, 2}
set2 = {1, 2, 3}
set3 = {1, 2, 3, 4}
print(f"set1.issubset(set2, set3): {set1.issubset(set2, set3)}")


# === SUPERSET CHECKING ===
print("\n=== SUPERSET CHECKING ===")
# superset: contains all elements of another (>= or issuperset())

set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}

print(f"set1: {set1}")
print(f"set2: {set2}")
print(f"set1 >= set2 (superset): {set1 >= set2}")
print(f"set1.issuperset(set2): {set1.issuperset(set2)}")

# Proper superset (>)
print(f"set1 > set2 (proper superset): {set1 > set2}")  # True (set1 is strict superset)
print(f"set1 > set1: {set1 > set1}")  # False (not proper)

# Check multiple sets
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2}
set3 = {3, 4}
print(f"set1.issuperset(set2, set3): {set1.issuperset(set2, set3)}")


# === DISJOINT CHECKING ===
print("\n=== DISJOINT CHECKING ===")
# disjoint: have no elements in common (isdisjoint())

set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = {3, 4, 5}

print(f"set1: {set1}")
print(f"set2: {set2}")
print(f"set3: {set3}")
print(f"set1.isdisjoint(set2): {set1.isdisjoint(set2)}")  # True (no common elements)
print(f"set1.isdisjoint(set3): {set1.isdisjoint(set3)}")  # False (3 is common)

# Empty set is disjoint with any set
print(f"set1.isdisjoint(set()): {set1.isdisjoint(set())}")  # True

# Check multiple sets
set1 = {1, 2}
set2 = {3, 4}
set3 = {5, 6}
print(f"set1.isdisjoint(set2, set3): {set1.isdisjoint(set2, set3)}")


# === OPERATION WITH FROZENSET ===
print("\n=== OPERATION WITH FROZENSET ===")
# Regular sets can operate with frozensets

regular = {1, 2, 3, 4}
frozen = frozenset([3, 4, 5, 6])

print(f"Regular set: {regular}")
print(f"Frozen set: {frozen}")

union = regular | frozen
print(f"union: {union}")
print(f"type: {type(union)}")  # Returns regular set

# Intersection
intersection = regular & frozen
print(f"intersection: {intersection}")
print(f"type: {type(intersection)}")

# Cannot modify frozen set
# frozen.add(7)  # AttributeError: 'frozenset' object has no attribute 'add'


# === OPERATION WITH ITERABLES (NON-SET) ===
print("\n=== OPERATION WITH ITERABLES ===")
# Most set operations work with any iterable

set1 = {1, 2, 3}
list1 = [2, 3, 4]
tuple1 = (3, 4, 5)

print(f"set1: {set1}")
print(f"list1: {list1}")
print(f"tuple1: {tuple1}")

# Union with list
union_list = set1.union(list1)
print(f"set1.union(list1): {union_list}")

# Intersection with tuple
intersection_tuple = set1.intersection(tuple1)
print(f"set1.intersection(tuple1): {intersection_tuple}")

# Difference with list
difference_list = set1.difference(list1)
print(f"set1.difference(list1): {difference_list}")

# Note: | operator requires both operands to be sets
# union_list_operator = set1 | list1  # TypeError: unsupported operand type(s) for |: 'set' and 'list'


# === CHAINING OPERATIONS ===
print("\n=== CHAINING SET OPERATIONS ===")
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = {5, 6, 7, 8}

# Chain operations
result = (a | b) & c
print(f"(a | b) & c: {result}")

# Equivalent using methods
result = a.union(b).intersection(c)
print(f"a.union(b).intersection(c): {result}")

# Complex chain
result = (a - b) | (b - c)
print(f"(a - b) | (b - c): {result}")


# === OPERATION VS UPDATE METHODS ===
print("\n=== OPERATION VS UPDATE METHODS ===")
# Operations (|, &, -, ^) return NEW sets
# Update methods modify the set in-place

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Operation returns new set
union_result = set1 | set2
print(f"Original set1: {set1}")
print(f"Union result: {union_result}")
print(f"set1 unchanged: {set1}")

# Update modifies in-place
set1.update(set2)
print(f"After set1.update(set2): {set1}")
print(f"set1 is modified: {set1}")


# === PRACTICAL EXAMPLES ===

# 1. Find common followers
print("\n=== PRACTICAL: COMMON FOLLOWERS ===")
alice_follows = {"Bob", "Charlie", "David", "Eve"}
bob_follows = {"Charlie", "Eve", "Frank", "Grace"}

common = alice_follows & bob_follows
print(f"Alice follows: {alice_follows}")
print(f"Bob follows: {bob_follows}")
print(f"Common followers: {common}")

# 2. Find unique items
print("\n=== PRACTICAL: UNIQUE ITEMS ===")
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

unique_to_list1 = set(list1) - set(list2)
unique_to_list2 = set(list2) - set(list1)
print(f"List1: {list1}")
print(f"List2: {list2}")
print(f"Unique to list1: {unique_to_list1}")
print(f"Unique to list2: {unique_to_list2}")

# 3. Validate categories
print("\n=== PRACTICAL: VALIDATE CATEGORIES ===")
valid_categories = {"electronics", "books", "clothing", "food"}
user_categories = {"books", "food", "toys"}

is_valid = user_categories.issubset(valid_categories)
print(f"Valid categories: {valid_categories}")
print(f"User categories: {user_categories}")
print(f"All user categories valid: {is_valid}")

# 4. Find exclusive items
print("\n=== PRACTICAL: EXCLUSIVE ITEMS ===")
store_a = {"apple", "banana", "cherry", "date"}
store_b = {"banana", "cherry", "elderberry", "fig"}

exclusive_a = store_a - store_b
exclusive_b = store_b - store_a
print(f"Store A exclusive: {exclusive_a}")
print(f"Store B exclusive: {exclusive_b}")
print(f"Shared items: {store_a & store_b}")

# 5. Partition data
print("\n=== PRACTICAL: PARTITION DATA ===")
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even = {n for n in numbers if n % 2 == 0}
odd = numbers - even
print(f"Numbers: {numbers}")
print(f"Even: {even}")
print(f"Odd: {odd}")
print(f"Disjoint: {even.isdisjoint(odd)}")


# === PERFORMANCE CHARACTERISTICS ===
print("\n=== PERFORMANCE CHARACTERISTICS ===")
print("Set operations are O(min(len(s1), len(s2))) on average")
print("Union: O(n + m) where n and m are set sizes")
print("Intersection: O(min(n, m))")
print("Difference: O(n) where n is size of first set")
print("Symmetric difference: O(n + m)")


# === FINAL SUMMARY ===
print("\n=== FINAL SUMMARY ===")
print("Set operations:")
print("  Union: | or union()")
print("  Intersection: & or intersection()")
print("  Difference: - or difference()")
print("  Symmetric difference: ^ or symmetric_difference()")
print("  Subset: <= or issubset()")
print("  Superset: >= or issuperset()")
print("  Disjoint: isdisjoint()")
print("All operations have in-place update versions (update, intersection_update, etc.)")
