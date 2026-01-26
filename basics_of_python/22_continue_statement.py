# Python continue Statement - Complete Reference
# continue skips the rest of current iteration and continues with next

# === CONTINUE IN FOR LOOP ===
print("=== CONTINUE IN FOR LOOP ===")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Skipping even numbers:")
for num in numbers:
    if num % 2 == 0:
        continue  # Skip rest of loop for even numbers
    print(f"Odd number: {num}")


# === CONTINUE IN WHILE LOOP ===
print("\n=== CONTINUE IN WHILE LOOP ===")
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue  # Skip even numbers
    print(f"Odd number: {i}")


# === CONTINUE WITH MULTIPLE CONDITIONS ===
print("\n=== CONTINUE WITH MULTIPLE CONDITIONS ===")
for num in range(1, 21):
    if num % 2 == 0:
        continue  # Skip evens
    if num % 3 == 0:
        continue  # Skip multiples of 3
    if num > 15:
        continue  # Skip numbers > 15
    print(f"Number passes all filters: {num}")


# === CONTINUE IN NESTED LOOPS ===
print("\n=== CONTINUE IN NESTED LOOPS ===")
# continue only affects the innermost loop
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            print(f"Continuing at i={i}, j={j}")
            continue
        print(f"i={i}, j={j}")


# === CONTINUE IN TRY/EXCEPT ===
print("\n=== CONTINUE IN TRY/EXCEPT ===")
data = ["10", "20", "thirty", "40", "50"]

for item in data:
    try:
        num = int(item)
        print(f"Parsed: {num}")
        if num > 30:
            print("Number > 30, continuing to next")
            continue
        print(f"Processing {num}")
    except ValueError:
        print(f"Cannot parse '{item}', skipping to next")
        continue


# === CONTINUE IN LIST COMPREHENSION (NOT DIRECTLY POSSIBLE) ===
print("\n=== CONTINUE ALTERNATIVE IN LIST COMPREHENSION ===")
# List comprehension has implicit continue (filters)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Equivalent to:
# for num in numbers:
#     if num % 2 != 0:  # Continue if even
#         process(num)
odd_squares = [num**2 for num in numbers if num % 2 != 0]
print(f"Odd squares: {odd_squares}")


# === CONTINUE WITH ELSE CLAUSE ===
print("\n=== CONTINUE WITH ELSE CLAUSE ===")
for i in range(5):
    if i == 2:
        continue  # This doesn't prevent else from executing
    print(f"i = {i}")
else:
    print("Loop completed without break")  # This WILL execute

# Compare with break
for i in range(5):
    if i == 2:
        break
    print(f"i = {i}")
else:
    print("This won't print because of break")  # This WON'T execute


# === PRACTICAL: PROCESSING FILES WITH ERRORS ===
print("\n=== PRACTICAL: FILE PROCESSING WITH ERRORS ===")
# Simulate processing lines that might have errors
lines = ["data1", "data2", "ERROR", "data3", "data4"]

for line_num, line in enumerate(lines, 1):
    if line == "ERROR":
        print(f"Error at line {line_num}, skipping")
        continue
    print(f"Processing line {line_num}: {line}")


# === PRACTICAL: FILTERING DATA ===
print("\n=== PRACTICAL: FILTERING DATA ===")
data = [10, 15, 20, 25, 30, 35, 40, 45, 50]

print("Processing valid data:")
for value in data:
    if value < 20:
        print(f"Skipping {value} (too small)")
        continue
    if value > 40:
        print(f"Skipping {value} (too large)")
        continue
    if value % 10 != 0:
        print(f"Skipping {value} (not multiple of 10)")
        continue
    print(f"Valid data: {value}")


# === CONTINUE WITH FLAG VARIABLES ===
print("\n=== CONTINUE WITH FLAG VARIABLES ===")
found_valid = False
for num in range(1, 20):
    if num % 2 == 0:
        continue
    
    if num % 3 == 0:
        continue
    
    print(f"First valid number: {num}")
    found_valid = True
    break

if not found_valid:
    print("No valid numbers found")


# === CONTINUE VS PASS ===
print("\n=== CONTINUE VS PASS ===")
# continue: skip rest of loop, go to next iteration
# pass: do nothing, continue with rest of loop

print("With continue:")
for i in range(3):
    if i == 1:
        continue
    print(f"i = {i}")

print("\nWith pass:")
for i in range(3):
    if i == 1:
        pass  # Does nothing, but loop continues
    print(f"i = {i}")


# === MULTIPLE CONTINUE CONDITIONS ===
print("\n=== MULTIPLE CONTINUE CONDITIONS ===")
for i in range(10):
    for j in range(10):
        if i == j:
            continue  # Skip diagonal
        if i + j > 10:
            continue  # Skip high sums
        if i * j % 2 == 0:
            continue  # Skip even products
        print(f"i={i}, j={j}, product={i*j}")
