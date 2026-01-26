# Python while Loops - Complete Reference
# Repeat block while condition is True

# === BASIC WHILE LOOP ===
print("=== BASIC WHILE LOOP ===")
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

print(f"Loop finished. Final count: {count}")


# === WHILE WITH ELSE CLAUSE ===
# else block executes if loop completes without break
print("\n=== WHILE WITH ELSE ===")
count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1
else:
    print("Loop completed successfully")

# Example where else doesn't execute
count = 0
while count < 5:
    print(f"Count: {count}")
    if count == 2:
        print("Breaking early")
        break
    count += 1
else:
    print("This won't print because of break")


# === INFINITE WHILE LOOP ===
print("\n=== INFINITE LOOP WITH BREAK ===")
# count = 0
# while True:
#     print(f"Count: {count}")
#     count += 1
#     if count >= 3:
#         print("Breaking infinite loop")
#         break


# === WHILE WITH CONTINUE ===
# Skip current iteration and continue with next
print("\n=== WHILE WITH CONTINUE ===")
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue  # Skip even numbers
    print(f"Odd number: {num}")


# === COUNTER PATTERNS ===
print("\n=== COUNTER PATTERNS ===")

# Count up
i = 0
while i < 5:
    print(f"Up: {i}")
    i += 1

# Count down
j = 5
while j > 0:
    print(f"Down: {j}")
    j -= 1

# Count by step
k = 0
while k < 20:
    print(f"Step 2: {k}")
    k += 2

# Count down by step
m = 20
while m > 0:
    print(f"Step -3: {m}")
    m -= 3


# === USER INPUT VALIDATION ===
print("\n=== USER INPUT VALIDATION ===")
# valid_input = False
# while not valid_input:
#     user_input = input("Enter a number between 1 and 10: ")
#     if user_input.isdigit():
#         num = int(user_input)
#         if 1 <= num <= 10:
#             print(f"Valid input: {num}")
#             valid_input = True
#         else:
#             print("Number out of range")
#     else:
#         print("Invalid input")


# === MENU SYSTEM ===
print("\n=== MENU SYSTEM SIMULATION ===")
choice = None
while choice != "3":
    print("\nMenu:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Exit")
    
    # choice = input("Enter choice: ")
    
    # For demonstration, simulate choices
    if not 'choice_counter' in locals():
        choice_counter = 0
    choices = ["1", "2", "3"]
    choice = choices[choice_counter]
    choice_counter += 1
    
    if choice == "1":
        print("You selected option 1")
    elif choice == "2":
        print("You selected option 2")
    elif choice == "3":
        print("Exiting...")
    else:
        print("Invalid choice")


# === WHILE LOOP WITH FLAG VARIABLE ===
print("\n=== FLAG VARIABLE PATTERN ===")
running = True
attempts = 0
max_attempts = 3

while running:
    print(f"Attempt {attempts + 1}")
    attempts += 1
    
    if attempts >= max_attempts:
        running = False
        print("Max attempts reached")

print("Loop ended via flag")


# === COMPARING FOR AND WHILE ===
print("\n=== FOR vs WHILE ===")

# For loop (when you know iterations)
print("For loop:")
for i in range(5):
    print(f"i = {i}")

# Equivalent while loop
print("\nEquivalent while:")
i = 0
while i < 5:
    print(f"i = {i}")
    i += 1


# === WHILE LOOP PERFORMANCE ===
# While loops are slightly slower than for loops for known iterations
print("\n=== PERFORMANCE NOTE ===")
# For simple counting, for loops are more Pythonic and slightly faster
# Use while when you don't know how many iterations you need


# === BREAK VS CONTINUE IN WHILE ===
print("\n=== BREAK VS CONTINUE ===")
# Break exits the entire loop
# Continue skips to next iteration

num = 0
while num < 10:
    num += 1
    if num == 3:
        print(f"Skipping {num} with continue")
        continue
    if num == 7:
        print(f"Breaking at {num}")
        break
    print(f"Processing {num}")


# === WHILE WITH MULTIPLE CONDITIONS ===
print("\n=== MULTIPLE CONDITIONS ===")
x = 0
y = 10

while x < 5 and y > 5:
    print(f"x = {x}, y = {y}")
    x += 1
    y -= 1


# === INFINITE LOOP PATTERNS ===
print("\n=== INFINITE LOOP PATTERNS ===")

# Pattern 1: Server loop
# while True:
#     # Wait for client request
#     request = get_request()
#     if request == "shutdown":
#         break
#     process_request(request)

# Pattern 2: Game loop
# running = True
# while running:
#     handle_input()
#     update_game_state()
#     render()
#     if game_over:
#         running = False
