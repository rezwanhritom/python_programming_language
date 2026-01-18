# Python Nested for Loops - Complete Reference
# for loops inside for loops

# === BASIC NESTED FOR LOOPS ===
print("=== BASIC NESTED FOR LOOPS ===")
# Outer loop
for i in range(3):
    print(f"Outer loop: i = {i}")
    # Inner loop
    for j in range(2):
        print(f"  Inner loop: j = {j}, i + j = {i + j}")


# === MATRIX PATTERNS ===
print("\n=== MATRIX PATTERN (RECTANGULAR) ===")
rows = 3
cols = 4

for row in range(rows):
    for col in range(cols):
        print(f"({row}, {col})", end=" ")
    print()  # New line after each row


# === SQUARE MATRIX ===
print("\n=== SQUARE MATRIX ===")
size = 5
matrix = []
for i in range(size):
    row = []
    for j in range(size):
        row.append(i * j)
    matrix.append(row)

print("Matrix:")
for row in matrix:
    print(row)


# === TRIANGLE PATTERNS ===
print("\n=== RIGHT TRIANGLE PATTERN ===")
height = 5
for i in range(1, height + 1):
    for j in range(i):
        print("*", end="")
    print()

print("\n=== INVERTED RIGHT TRIANGLE ===")
for i in range(height, 0, -1):
    for j in range(i):
        print("*", end="")
    print()


# === PYRAMID PATTERN ===
print("\n=== PYRAMID PATTERN ===")
height = 5
for i in range(1, height + 1):
    # Print spaces
    for j in range(height - i):
        print(" ", end="")
    # Print stars
    for j in range(2 * i - 1):
        print("*", end="")
    print()


# === DIAMOND PATTERN ===
print("\n=== DIAMOND PATTERN ===")
height = 5
# Top half
for i in range(1, height + 1):
    for j in range(height - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()
# Bottom half
for i in range(height - 1, 0, -1):
    for j in range(height - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()


# === MULTIPLICATION TABLE ===
print("\n=== MULTIPLICATION TABLE ===")
size = 10
for i in range(1, size + 1):
    for j in range(1, size + 1):
        product = i * j
        print(f"{product:4d}", end="")
    print()


# === PROCESSING 2D LISTS ===
print("\n=== PROCESSING 2D LISTS ===")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original matrix:")
for row in matrix:
    print(row)

# Sum all elements
total = 0
for row in matrix:
    for element in row:
        total += element
print(f"Sum of all elements: {total}")

# Find max in each row
print("\nMax in each row:")
for i, row in enumerate(matrix):
    row_max = row[0]
    for element in row:
        if element > row_max:
            row_max = element
    print(f"Row {i}: max = {row_max}")

# Transpose matrix (complete the cut-off section)
print("\nTransposed matrix:")
transposed = []
for col_idx in range(len(matrix[0])):
    new_row = []
    for row_idx in range(len(matrix)):
        new_row.append(matrix[row_idx][col_idx])
    transposed.append(new_row)

for row in transposed:
    print(row)


# === PROCESSING 3D STRUCTURES ===
print("\n=== PROCESSING 3D STRUCTURES ===")
cube = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
    [[9, 10], [11, 12]]
]

print("3D array structure:")
for layer_idx, layer in enumerate(cube):
    print(f"Layer {layer_idx}:")
    for row_idx, row in enumerate(layer):
        print(f"  Row {row_idx}: {row}")
        for col_idx, value in enumerate(row):
            print(f"    Column {col_idx}: {value}")


# === COMBINING NESTED LOOPS WITH BREAK/CONTINUE ===
print("\n=== BREAK IN NESTED LOOPS ===")
# Break only exits the innermost loop
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            print(f"Breaking at i={i}, j={j}")
            break
        print(f"i={i}, j={j}")
    print(f"Finished inner loop for i={i}")


print("\n=== CONTINUE IN NESTED LOOPS ===")
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            print(f"Continuing at i={i}, j={j}")
            continue
        print(f"i={i}, j={j}")


# === REAL-WORLD: FINDING COORDINATES ===
print("\n=== REAL-WORLD: FINDING COORDINATES ===")
grid = [
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 0]
]

target = 1
found_positions = []

for row_idx, row in enumerate(grid):
    for col_idx, cell in enumerate(row):
        if cell == target:
            found_positions.append((row_idx, col_idx))

print(f"Found {target} at positions: {found_positions}")


# === PERFORMANCE CONSIDERATIONS ===
print("\n=== PERFORMANCE NOTE ===")
# Nested loops have O(n*m) complexity
# For large datasets, consider vectorized operations or different algorithms
