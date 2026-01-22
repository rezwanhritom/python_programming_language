# Python Tuple Methods - Focused Reference
# Built-in methods: count(), index()
# Plus common patterns that behave like "methods" in practice.

# === REMINDER: TUPLES ARE IMMUTABLE ===
print("=== REMINDER: TUPLES ARE IMMUTABLE ===")
t = (1, 2, 3, 2, 4, 2)
print(f"Tuple: {t}")
print("Tuples do NOT have methods like append, extend, insert, remove, pop, clear, sort, or reverse.")
print("They only have count() and index().")


# === COUNT() METHOD ===
print("\n=== count() METHOD ===")
# Syntax: tuple.count(value)
# Returns the number of times 'value' appears in the tuple. [web:57][web:59]

numbers = (1, 2, 2, 3, 2, 4, 2, 5)
print(f"numbers: {numbers}")

count_2 = numbers.count(2)
print(f"numbers.count(2): {count_2}")  # 4

count_3 = numbers.count(3)
print(f"numbers.count(3): {count_3}")  # 1

count_99 = numbers.count(99)
print(f"numbers.count(99): {count_99}")  # 0

# Works with any hashable type
mixed = ("apple", "banana", "apple", "cherry", "apple")
print(f"\nmixed: {mixed}")
print(f"mixed.count('apple'): {mixed.count('apple')}")
print(f"mixed.count('banana'): {mixed.count('banana')}")
print(f"mixed.count('x'): {mixed.count('x')}")


# === index() METHOD ===
print("\n=== index() METHOD ===")
# Syntax: tuple.index(value[, start[, end]]) [web:58][web:60]
# Returns the index of the FIRST occurrence of value.
# Raises ValueError if value not found.

t = (10, 20, 30, 20, 40, 20, 50)
print(f"t: {t}")

idx_20 = t.index(20)
print(f"t.index(20): {idx_20}")  # 1 (first 20)

idx_20_from_2 = t.index(20, 2)  # Search from index 2
print(f"t.index(20, 2): {idx_20_from_2}")  # 3

# With start and end range
idx_20_range = t.index(20, 2, 5)  # Search in slice t[2:5]
print(f"t.index(20, 2, 5): {idx_20_range}")  # 3

# ValueError example (commented)
# t.index(99)  # Would raise ValueError: tuple.index(x): x not in tuple


# === COMBINING count() AND index() ===
print("\n=== COMBINING count() AND index() ===")
t = (1, 2, 2, 3, 2, 4, 2)
print(f"t: {t}")
value = 2

total = t.count(value)
print(f"{value} appears {total} times")

# Get all indices of value using index in a loop
indices = []
start = 0
while True:
    try:
        pos = t.index(value, start)
        indices.append(pos)
        start = pos + 1
    except ValueError:
        break

print(f"Indices of {value}: {indices}")


# === SEARCHING SUBRANGE WITH index() ===
print("\n=== SEARCHING SUBRANGE ===")
letters = ("a", "b", "c", "d", "e", "b", "f")
print(f"letters: {letters}")

# Find 'b' in first half
idx_first_half = letters.index("b", 0, len(letters)//2)
print(f"Index of 'b' in first half: {idx_first_half}")

# Find 'b' in second half
idx_second_half = letters.index("b", len(letters)//2)
print(f"Index of 'b' in second half: {idx_second_half}")


# === PATTERN: FIND ALL POSITIONS OF VALUE ===
print("\n=== FIND ALL POSITIONS OF VALUE ===")
t = ("apple", "banana", "apple", "cherry", "apple", "banana")
value = "banana"
print(f"t: {t}")
print(f"Value to find: {value}")

positions = [i for i, v in enumerate(t) if v == value]
print(f"All positions of '{value}': {positions}")


# === PATTERN: CHECK EXISTENCE BEFORE index() ===
print("\n=== CHECK EXISTENCE BEFORE index() ===")
t = (1, 3, 5, 7)
print(f"t: {t}")

x = 5
if x in t:
    print(f"{x} found at index {t.index(x)}")
else:
    print(f"{x} not found")

y = 10
if y in t:
    print(f"{y} found at index {t.index(y)}")
else:
    print(f"{y} not found")


# === METHOD-LIKE OPERATIONS (NOT METHODS) ===
print("\n=== COMMON OPERATIONS (NOT METHODS) ===")
t = (0, 1, 2, 3, 4, 5, 6)

# Length
print(f"len(t): {len(t)}")

# Membership
print(f"3 in t: {3 in t}")
print(f"99 in t: {99 in t}")

# Slicing
print(f"t[2:5]: {t[2:5]}")

# Concatenation and repetition [web:56][web:44]
t1 = (1, 2, 3)
t2 = (4, 5)
print(f"t1 + t2: {t1 + t2}")
print(f"t1 * 3: {t1 * 3}")

# min, max, sum
nums = (3, 1, 4, 1, 5)
print(f"\nnums: {nums}")
print(f"min(nums): {min(nums)}")
print(f"max(nums): {max(nums)}")
print(f"sum(nums): {sum(nums)}")

# Sorted (returns list)
print(f"sorted(nums): {sorted(nums)}")


# === TUPLE AS RETURN TYPE WITH METHODS-LIKE BEHAVIOR ===
print("\n=== TUPLE AS RETURN TYPE ===")
def find_min_max_positions(values):
    """Return (min_value, min_index, max_value, max_index)."""
    min_val = min(values)
    max_val = max(values)
    min_idx = values.index(min_val)
    max_idx = values.index(max_val)
    return (min_val, min_idx, max_val, max_idx)

values = (5, 2, 9, 1, 9, 3)
result = find_min_max_positions(values)
print(f"values: {values}")
print(f"(min_val, min_idx, max_val, max_idx): {result}")


# === PRACTICAL EXAMPLES ===

print("\n=== PRACTICAL: FREQUENCY TABLE ===")
data = ("red", "blue", "red", "green", "blue", "red")
unique_colors = set(data)
for color in unique_colors:
    print(f"{color}: {data.count(color)} time(s)")


print("\n=== PRACTICAL: SAFE index() WRAPPER ===")
def safe_index(tup, value, start=0, end=None):
    """Return index of value or -1 if not found."""
    if end is None:
        end = len(tup)
    try:
        return tup.index(value, start, end)
    except ValueError:
        return -1

t = ("a", "b", "c", "b", "d")
print(f"t: {t}")
print(f"safe_index(t, 'b'): {safe_index(t, 'b')}")
print(f"safe_index(t, 'b', 2): {safe_index(t, 'b', 2)}")
print(f"safe_index(t, 'x'): {safe_index(t, 'x')}")

print("\n=== SUMMARY ===")
print("Tuple methods are minimal by design: only count() and index().")
print("Most other behavior comes from generic sequence operations (len, slicing, +, *, in).")
print("Use tuples when you need fixed, ordered data that should not change.")
