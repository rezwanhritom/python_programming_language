# Python Nested while Loops - Complete Reference
# while loops inside while loops

# === BASIC NESTED WHILE LOOPS ===
print("=== BASIC NESTED WHILE LOOPS ===")
i = 0
while i < 3:
    print(f"Outer loop: i = {i}")
    j = 0
    while j < 2:
        print(f"  Inner loop: j = {j}, i + j = {i + j}")
        j += 1
    i += 1


# === PYRAMID WITH WHILE LOOPS ===
print("\n=== PYRAMID WITH WHILE LOOPS ===")
height = 5
i = 1
while i <= height:
    # Print spaces
    spaces = height - i
    while spaces > 0:
        print(" ", end="")
        spaces -= 1
    
    # Print stars
    stars = 2 * i - 1
    while stars > 0:
        print("*", end="")
        stars -= 1
    
    print()
    i += 1


# === MATRIX PROCESSING WITH WHILE ===
print("\n=== MATRIX PROCESSING WITH WHILE ===")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

row_idx = 0
while row_idx < len(matrix):
    col_idx = 0
    row_sum = 0
    while col_idx < len(matrix[row_idx]):
        row_sum += matrix[row_idx][col_idx]
        col_idx += 1
    print(f"Row {row_idx} sum: {row_sum}")
    row_idx += 1


# === USER AUTHENTICATION SIMULATION ===
print("\n=== USER AUTHENTICATION SIMULATION ===")
valid_users = {"alice": "password123", "bob": "secret456"}
max_attempts = 3
attempts = 0
authenticated = False

while attempts < max_attempts and not authenticated:
    username = input(f"Enter username (attempt {attempts + 1}/{max_attempts}): ")
    password = input("Enter password: ")
    
    if username in valid_users and valid_users[username] == password:
        print("Authentication successful!")
        authenticated = True
    else:
        print("Invalid credentials")
        attempts += 1

if not authenticated:
    print("Account locked after maximum attempts")


# === MENU WITH NESTED WHILE ===
print("\n=== MENU WITH NESTED WHILE ===")
main_choice = None
while main_choice != "3":
    print("\nMain Menu:")
    print("1. Settings")
    print("2. Reports")
    print("3. Exit")
    main_choice = input("Enter choice: ")
    
    if main_choice == "1":
        settings_choice = None
        while settings_choice != "2":
            print("\nSettings Menu:")
            print("1. Change password")
            print("2. Back to main")
            settings_choice = input("Enter choice: ")
            
            if settings_choice == "1":
                new_password = input("Enter new password: ")
                print("Password changed (simulation)")
    elif main_choice == "2":
        print("Generating reports... (simulation)")
    elif main_choice == "3":
        print("Goodbye!")
    else:
        print("Invalid choice")


# === SEARCH IN 2D ARRAY WITH WHILE ===
print("\n=== SEARCH IN 2D ARRAY ===")
grid = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
target = 7
found = False

row_idx = 0
while row_idx < len(grid) and not found:
    col_idx = 0
    while col_idx < len(grid[row_idx]) and not found:
        if grid[row_idx][col_idx] == target:
            print(f"Found {target} at row {row_idx}, col {col_idx}")
            found = True
        col_idx += 1
    row_idx += 1

if not found:
    print(f"{target} not found in grid")


# === BREAK IN NESTED WHILE ===
print("\n=== BREAK IN NESTED WHILE ===")
i = 0
while i < 5:
    j = 0
    while j < 5:
        if i == 2 and j == 2:
            print(f"Breaking inner loop at i={i}, j={j}")
            break
        print(f"i={i}, j={j}")
        j += 1
    print(f"Finished inner loop for i={i}")
    i += 1


# === CONTINUE IN NESTED WHILE ===
print("\n=== CONTINUE IN NESTED WHILE ===")
i = 0
while i < 3:
    j = 0
    while j < 3:
        if i == 1 and j == 1:
            print(f"Continuing at i={i}, j={j}")
            j += 1
            continue
        print(f"i={i}, j={j}")
        j += 1
    i += 1


# === FLAG VARIABLE PATTERN ===
print("\n=== FLAG VARIABLE PATTERN ===")
found = False
i = 0
while i < 10 and not found:
    j = 0
    while j < 10 and not found:
        if i * j == 42:
            found = True
            print(f"Found 42 = {i} × {j}")
        j += 1
    i += 1


# === PERFORMANCE COMPARISON ===
print("\n=== PERFORMANCE NOTE ===")
# Nested while loops are generally slower than nested for loops
# Use for loops when iteration count is known
