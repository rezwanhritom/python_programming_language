# Python for Loops with range() - Complete Reference
# range() generates sequences of numbers for iteration

# === BASIC RANGE() ===
# range(stop) generates numbers from 0 to stop-1
print("=== BASIC RANGE(stop) ===")
for i in range(5):
    print(f"i = {i}")

# Equivalent to: for i in [0, 1, 2, 3, 4]:


# === RANGE WITH START AND STOP ===
# range(start, stop) generates numbers from start to stop-1
print("\n=== RANGE(start, stop) ===")
for i in range(3, 8):
    print(f"i = {i}")

# Equivalent to: for i in [3, 4, 5, 6, 7]:


# === RANGE WITH STEP ===
# range(start, stop, step) generates numbers with custom step
print("\n=== RANGE(start, stop, step) ===")
for i in range(0, 10, 2):
    print(f"i = {i}")

# Equivalent to: for i in [0, 2, 4, 6, 8]:


# === RANGE WITH NEGATIVE STEP ===
# Counting backwards
print("\n=== RANGE WITH NEGATIVE STEP ===")
for i in range(10, 0, -1):
    print(f"i = {i}")

# Equivalent to: for i in [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]:


# === RANGE WITH NEGATIVE STEP (DECREMENTING) ===
print("\n=== COUNTING DOWN ===")
for i in range(5, -1, -1):
    print(f"Countdown: {i}")


# === CREATING RANGE OBJECTS ===
# range() returns a range object (not a list)
print("\n=== RANGE OBJECTS ===")
r = range(5)
print(f"range(5): {r}")
print(f"type(range(5)): {type(r)}")

# Convert to list to see contents
print(f"list(range(5)): {list(r)}")


# === RANGE ATTRIBUTES ===
# range objects have start, stop, step attributes (Python 3.3+)
r = range(2, 10, 2)
print(f"\nrange(2, 10, 2).start: {r.start}")
print(f"range(2, 10, 2).stop: {r.stop}")
print(f"range(2, 10, 2).step: {r.step}")


# === RANGE LENGTH ===
# len() works on range objects
print(f"\nlen(range(5)): {len(range(5))}")
print(f"len(range(10, 20)): {len(range(10, 20))}")
print(f"len(range(0, 10, 2)): {len(range(0, 10, 2))}")


# === INDEXING RANGE OBJECTS ===
# Range objects support indexing (like sequences)
r = range(5)
print(f"\nrange(5)[0]: {r[0]}")
print(f"range(5)[-1]: {r[-1]}")
print(f"range(5)[2]: {r[2]}")


# === SLICING RANGE OBJECTS ===
# Range objects support slicing
r = range(10)
print(f"\nlist(range(10)): {list(r)}")
print(f"list(range(10)[2:5]): {list(r[2:5])}")
print(f"list(range(10)[::2]): {list(r[::2])}")
print(f"list(range(10)[::-1]): {list(r[::-1])}")


# === RANGE MEMBERSHIP TESTING ===
# 'in' and 'not in' work with range objects (very efficient)
r = range(0, 100, 5)
print(f"\n50 in range(0, 100, 5): {50 in r}")      # True
print(f"51 in range(0, 100, 5): {51 in r}")      # False
print(f"100 in range(0, 100, 5): {100 in r}")    # False (stop is exclusive)
print(f"-5 in range(0, 100, 5): {-5 in r}")      # False


# === PRACTICAL EXAMPLES ===

# 1. Sum of first N numbers
print("\n=== SUM OF FIRST N NUMBERS ===")
n = 10
total = 0
for i in range(1, n + 1):
    total += i
print(f"Sum of 1 to {n}: {total}")
print(f"Verification: {n} * ({n} + 1) / 2 = {n * (n + 1) // 2}")

# 2. Print multiplication table
print("\n=== MULTIPLICATION TABLE ===")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i * j:2d}", end=" ")
    print()  # New line

# 3. List comprehension with range
print("\n=== LIST COMPREHENSION WITH RANGE ===")
squares = [x**2 for x in range(1, 6)]
print(f"Squares 1-5: {squares}")

# 4. Reverse iteration
print("\n=== REVERSE ITERATION WITH RANGE ===")
for i in range(10, 0, -1):
    print(f"Countdown: {i}")

# 5. Step patterns
print("\n=== STEP PATTERNS ===")
print("Even numbers 0-10:", list(range(0, 11, 2)))
print("Odd numbers 1-10:", list(range(1, 11, 2)))
print("Multiples of 3 (0-30):", list(range(0, 31, 3)))


# 6. Simulating while loop with range
print("\n=== SIMULATING WHILE LOOP ===")
# Instead of: while x < 10: ...
for x in range(10):
    if x == 5:
        print(f"Breaking at x = {x}")
        break
    print(f"x = {x}")


# 7. Range with variables
print("\n=== RANGE WITH VARIABLES ===")
start = 5
stop = 15
step = 3
print(f"range({start}, {stop}, {step}): {list(range(start, stop, step))}")


# 8. Empty range cases
print("\n=== EMPTY RANGE CASES ===")
print(f"range(5, 5): {list(range(5, 5))}")          # Empty (start == stop)
print(f"range(5, 0): {list(range(5, 0))}")          # Empty (start > stop, step positive)
print(f"range(5, 0, -1): {list(range(5, 0, -1))}")  # Not empty (negative step)


# 9. Range equality
print("\n=== RANGE EQUALITY ===")
r1 = range(0, 10, 2)
r2 = range(0, 10, 2)
r3 = range(0, 11, 2)
print(f"range(0, 10, 2) == range(0, 10, 2): {r1 == r2}")  # True
print(f"range(0, 10, 2) == range(0, 11, 2): {r1 == r3}")  # False (different stop)
