# Python if Statements - Complete Reference
# Control flow based on boolean conditions

# === BASIC IF STATEMENT ===
# Executes block if condition is True
print("=== BASIC IF STATEMENT ===")
age = 18

if age >= 18:
    print(f"Age {age} is 18 or older")
    print("This line is also part of the if block")

# This line is outside the if block (always executes)
print("This line always executes")


# === IF-ELSE STATEMENT ===
# Executes one block if True, another if False
print("\n=== IF-ELSE STATEMENT ===")
temperature = 25

if temperature > 30:
    print(f"{temperature}°C is hot")
else:
    print(f"{temperature}°C is not hot")


# === IF-ELIF-ELSE STATEMENT ===
# Checks multiple conditions sequentially
print("\n=== IF-ELIF-ELSE STATEMENT ===")
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score {score} -> Grade: {grade}")


# === MULTIPLE ELIF BRANCHES ===
print("\n=== MULTIPLE ELIF BRANCHES ===")
day = "Wednesday"

if day == "Monday":
    activity = "Team meeting"
elif day == "Tuesday":
    activity = "Code review"
elif day == "Wednesday":
    activity = "Sprint planning"
elif day == "Thursday":
    activity = "Development"
elif day == "Friday":
    activity = "Deployment"
else:
    activity = "Weekend"

print(f"{day}: {activity}")


# === INDENTATION RULES ===
# Python uses indentation to define blocks (typically 4 spaces)
print("\n=== INDENTATION RULES ===")
x = 10

if x > 5:
    print("x is greater than 5")      # 4 spaces indent
    if x > 8:
        print("x is also greater than 8")  # 8 spaces indent (nested)
    print("Back to first if block")   # 4 spaces indent

# This is outside all if blocks
print("Outside all if statements")


# === THE PASS STATEMENT ===
# 'pass' is a placeholder that does nothing
print("\n=== THE PASS STATEMENT ===")
value = 5

if value > 10:
    pass  # TODO: implement this case later
else:
    print(f"Value {value} is not greater than 10")

# pass can be used in empty functions or classes
def placeholder_function():
    pass

class PlaceholderClass:
    pass


# === TRUTHY AND FALSY VALUES IN CONDITIONS ===
# Any value can be used in an if condition
print("\n=== TRUTHY/FALSY IN CONDITIONS ===")

# Falsy values evaluate to False
falsy_examples = [0, 0.0, "", [], (), {}, None, False]

for val in falsy_examples:
    if val:
        print(f"{val} is truthy")  # Won't print for falsy values
    else:
        print(f"{val} is falsy")

# Truthy values evaluate to True
truthy_examples = [42, -1, "hello", [1], (1,), {"key": "value"}, True]

print("\nTruth values:")
for val in truthy_examples:
    if val:
        print(f"{val} is truthy")
    else:
        print(f"{val} is falsy")  # Won't print for truthy values


# === NESTED IF STATEMENTS (SIMPLE) ===
print("\n=== SIMPLE NESTED IF ===")
num = 15

if num > 10:
    print(f"{num} is greater than 10")
    if num % 2 == 0:
        print(f"{num} is also even")
    else:
        print(f"{num} is odd")


# === COMPLEX CONDITIONS ===
print("\n=== COMPLEX CONDITIONS ===")
age = 25
has_license = True
has_insurance = False

# Using 'and', 'or', 'not'
if age >= 18 and has_license:
    print("Can drive")
    if not has_insurance:
        print("But needs insurance!")
else:
    print("Cannot drive")


# === TERNARY-STYLE IF (EXPRESSION) ===
# Python's conditional expression: value_if_true if condition else value_if_false
print("\n=== TERNARY-STYLE IF ===")
status = "adult" if age >= 18 else "minor"
print(f"Age {age} -> Status: {status}")

# More complex example
result = "pass" if score >= 60 else "fail"
print(f"Score {score} -> Result: {result}")
