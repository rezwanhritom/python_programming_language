# Python break Statement - Complete Reference
# break exits the nearest enclosing loop immediately

# === BREAK IN FOR LOOP (LINEAR SEARCH) ===
print("=== BREAK IN FOR LOOP (LINEAR SEARCH) ===")
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
target = 55

for num in numbers:
    if num == target:
        print(f"Found {target}!")
        break
    print(f"Checking {num}")
else:
    # This else block executes if loop completes WITHOUT break
    print(f"{target} not found in list")

print("Loop finished")


# === BREAK IN WHILE LOOP (PASSWORD ATTEMPTS) ===
print("\n=== BREAK IN WHILE LOOP (PASSWORD ATTEMPTS) ===")
correct_password = "secret123"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    password = input(f"Enter password (attempt {attempts + 1}/{max_attempts}): ")
    if password == correct_password:
        print("Access granted!")
        break
    print("Incorrect password")
    attempts += 1
else:
    print("Maximum attempts reached. Account locked.")

print("Authentication process finished")


# === BREAK IN NESTED LOOPS ===
print("\n=== BREAK IN NESTED LOOPS ===")
# break only exits the innermost loop
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            print(f"Breaking at i={i}, j={j}")
            break
        print(f"i={i}, j={j}")
    print(f"Finished inner loop for i={i}")


# === BREAK WITH FLAG VARIABLE ===
print("\n=== BREAK WITH FLAG VARIABLE ===")
# Sometimes you need to break out of multiple loops
found = False
for i in range(5):
    for j in range(5):
        if i * j == 12:
            print(f"Found 12 = {i} × {j}")
            found = True
            break
    if found:
        break


# === BREAK IN INFINITE LOOP ===
print("\n=== BREAK IN INFINITE LOOP ===")
count = 0
while True:
    print(f"Count: {count}")
    count += 1
    if count >= 5:
        print("Breaking infinite loop")
        break
print("Loop ended")


# === BREAK IN LIST COMPREHENSION (NOT DIRECTLY POSSIBLE) ===
print("\n=== BREAK IN LIST COMPREHENSION ALTERNATIVE ===")
# You cannot use break in list comprehensions
# Instead, use a regular loop with break

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Find first even number greater than 5
result = None
for num in numbers:
    if num > 5 and num % 2 == 0:
        result = num
        break
print(f"First even > 5: {result}")


# === BREAK WITH TRY/EXCEPT ===
print("\n=== BREAK WITH TRY/EXCEPT ===")
data = ["10", "20", "thirty", "40"]
for item in data:
    try:
        num = int(item)
        print(f"Parsed: {num}")
        if num > 25:
            print("Found number > 25, stopping")
            break
    except ValueError:
        print(f"Cannot parse '{item}', skipping")
        continue


# === PRACTICAL: FIND FIRST PRIME ===
print("\n=== PRACTICAL: FIND FIRST PRIME ===")
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [4, 6, 8, 9, 10, 11, 12, 13, 14, 15]
first_prime = None

for num in numbers:
    if is_prime(num):
        first_prime = num
        print(f"First prime found: {num}")
        break

if first_prime is None:
    print("No prime numbers found")


# === BREAK IN GENERATOR FUNCTIONS ===
print("\n=== BREAK IN GENERATOR FUNCTIONS ===")
def number_generator():
    n = 0
    while True:
        yield n
        n += 1

gen = number_generator()
for i in range(5):
    print(f"Generated: {next(gen)}")

# Using break with generator
print("Using break with generator:")
for num in number_generator():
    if num >= 5:
        break
    print(f"Number: {num}")


# === MULTIPLE BREAK CONDITIONS ===
print("\n=== MULTIPLE BREAK CONDITIONS ===")
for i in range(10):
    for j in range(10):
        product = i * j
        if product > 50:
            print(f"Product {product} > 50 at i={i}, j={j}")
            break
        if i + j > 10:
            print(f"Sum {i+j} > 10 at i={i}, j={j}")
            break
        print(f"i={i}, j={j}, product={product}")
    else:
        continue  # Continue outer loop if inner loop completed normally
    break  # Break outer loop if inner loop was broken

print("Loop finished")


# === BREAK VS RETURN ===
print("\n=== BREAK VS RETURN ===")
def find_target(numbers, target):
    for num in numbers:
        if num == target:
            print(f"Found {target}")
            return True  # Exits function entirely
    print(f"{target} not found")
    return False

numbers = [1, 2, 3, 4, 5]
result = find_target(numbers, 3)
print(f"Result: {result}")

# Note: break only exits loop, return exits function
