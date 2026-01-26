# Python Mixed Nested Loops - Complete Reference
# Combining for and while loops in nested structures

# === FOR INSIDE WHILE ===
print("=== FOR INSIDE WHILE ===")
counter = 0
while counter < 3:
    print(f"While loop: counter = {counter}")
    for i in range(2):
        print(f"  For loop: i = {i}, counter + i = {counter + i}")
    counter += 1


# === WHILE INSIDE FOR ===
print("\n=== WHILE INSIDE FOR ===")
for i in range(3):
    print(f"For loop: i = {i}")
    j = 0
    while j < 2:
        print(f"  While loop: j = {j}, i * j = {i * j}")
        j += 1


# === FOR INSIDE WHILE INSIDE FOR ===
print("\n=== FOR INSIDE WHILE INSIDE FOR ===")
for outer in range(2):
    print(f"Outer for: outer = {outer}")
    middle = 0
    while middle < 2:
        print(f"  Middle while: middle = {middle}")
        for inner in range(2):
            print(f"    Inner for: inner = {inner}, sum = {outer + middle + inner}")
        middle += 1


# === WHILE INSIDE FOR INSIDE WHILE ===
print("\n=== WHILE INSIDE FOR INSIDE WHILE ===")
outer = 0
while outer < 2:
    print(f"Outer while: outer = {outer}")
    for middle in range(2):
        print(f"  Middle for: middle = {middle}")
        inner = 0
        while inner < 2:
            print(f"    Inner while: inner = {inner}, product = {outer * middle * (inner + 1)}")
            inner += 1
    outer += 1


# === SEARCH WITH MIXED LOOPS ===
print("\n=== SEARCH WITH MIXED LOOPS ===")
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
target = 7
found = False

for row_idx, row in enumerate(matrix):
    col_idx = 0
    while col_idx < len(row) and not found:
        if row[col_idx] == target:
            print(f"Found {target} at row {row_idx}, col {col_idx}")
            found = True
        col_idx += 1


# === MENU WITH SUB-MENUS ===
print("\n=== MENU WITH SUB-MENUS (MIXED) ===")
main_choice = None
while main_choice != "3":
    print("\nMain Menu:")
    print("1. View items")
    print("2. Settings")
    print("3. Exit")
    main_choice = input("Enter choice: ")
    
    if main_choice == "1":
        items = ["Item A", "Item B", "Item C"]
        for idx, item in enumerate(items):
            print(f"{idx + 1}. {item}")
        
        sub_choice = input("Select item number or 'b' to go back: ")
        while sub_choice != 'b':
            if sub_choice.isdigit() and 1 <= int(sub_choice) <= len(items):
                selected = items[int(sub_choice) - 1]
                print(f"You selected: {selected}")
            else:
                print("Invalid selection")
            sub_choice = input("Select another or 'b' to go back: ")
    
    elif main_choice == "2":
        print("Settings:")
        options = ["Option 1", "Option 2"]
        for option in options:
            print(f"- {option}")
        
        confirm = ""
        while confirm.lower() not in ['y', 'n']:
            confirm = input("Apply changes? (y/n): ")
        print(f"Changes {'applied' if confirm == 'y' else 'cancelled'}")


# === FILE PROCESSING SIMULATION ===
print("\n=== FILE PROCESSING SIMULATION ===")
files = ["file1.txt", "file2.txt", "file3.txt"]
for filename in files:
    print(f"Processing {filename}")
    line_num = 1
    
    # Simulate reading lines until EOF
    import random
    num_lines = random.randint(3, 6)
    while line_num <= num_lines:
        print(f"  Line {line_num}: Content of line {line_num}")
        
        # Simulate error check
        if "error" in f"line {line_num}":
            print("    Error found!")
            break
        line_num += 1
    else:
        print(f"  {filename} processed successfully")


# === TIMED OPERATIONS (COMPLETED) ===
print("\n=== TIMED OPERATIONS ===")
import time
start_time = time.time()
max_duration = 2  # seconds

outer = 0
while time.time() - start_time < max_duration:
    print(f"Outer iteration {outer}")
    
    for inner in range(3):
        current_time = time.time()
        elapsed = current_time - start_time
        
        if elapsed >= max_duration:
            print(f"Time limit reached at outer={outer}, inner={inner}")
            break
        
        print(f"  Inner {inner} at t={elapsed:.2f}s")
        time.sleep(0.5)  # Sleep for 0.5 seconds
    else:
        # This else runs if inner loop completes without break
        print(f"  Completed inner loop for outer={outer}")
    
    outer += 1
else:
    # This else runs if while loop completes naturally (time limit reached)
    print(f"Finished all iterations within time limit. Total outer loops: {outer}")


# === PRACTICAL: RETRY MECHANISM ===
print("\n=== PRACTICAL: RETRY MECHANISM ===")
max_retries = 3
for attempt in range(max_retries):
    print(f"Attempt {attempt + 1}/{max_retries}")
    
    success = False
    retry_delay = 1
    while not success and retry_delay <= 4:
        print(f"  Trying with delay {retry_delay}s...")
        # Simulate operation
        import random
        if random.random() > 0.7 or retry_delay == 4:
            print("  Success!")
            success = True
        else:
            print("  Failed, retrying...")
            time.sleep(retry_delay)
            retry_delay *= 2
    
    if success:
        print("Operation completed")
        break
else:
    print("All attempts failed")


# === COMPLEX DATA STRUCTURE TRAVERSAL ===
print("\n=== COMPLEX DATA STRUCTURE TRAVERSAL ===")
data = {
    "level1": {
        "level2a": [1, 2, 3],
        "level2b": {
            "level3a": ["a", "b"],
            "level3b": ["c", "d"]
        }
    },
    "level1b": [4, 5, 6]
}

for key, value in data.items():
    print(f"Top level: {key}")
    
    if isinstance(value, dict):
        level = 0
        while level < 2:  # Limit depth for demo
            for subkey, subvalue in value.items():
                print(f"  {subkey}: {subvalue}")
            level += 1
    else:
        for item in value:
            print(f"  Item: {item}")


# === FINAL SUMMARY ===
print("\n=== SUMMARY ===")
print("Mixed nested loops combine the flexibility of while loops")
print("with the iteration control of for loops.")
print("Use them when you have different iteration patterns at different levels.")
