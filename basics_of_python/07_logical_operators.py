# Python Logical Operators - Complete Reference
# AND, OR, NOT with short-circuit evaluation

# === LOGICAL AND OPERATOR ===
# Returns True if BOTH operands are True
print("=== LOGICAL AND (and) ===")
print(f"True and True: {True and True}")
print(f"True and False: {True and False}")
print(f"False and True: {False and True}")
print(f"False and False: {False and False}")

# AND with truthy/falsy values
# Returns the FIRST FALSY value or the LAST value if all are truthy
print(f"\nTruthy/falsy behavior:")
print(f"5 and 10: {5 and 10}")          # Returns 10 (both truthy)
print(f"5 and 0: {5 and 0}")            # Returns 0 (falsy)
print(f"0 and 5: {0 and 5}")            # Returns 0 (first falsy)
print(f"0 and None: {0 and None}")      # Returns 0 (first falsy)

# Short-circuit evaluation: second operand not evaluated if first is falsy
def expensive_operation():
    print("Expensive operation called!")
    return True

print(f"\nShort-circuit demonstration:")
result = False and expensive_operation()  # expensive_operation() never called
print(f"False and expensive_operation(): {result}")

# === LOGICAL OR OPERATOR ===
# Returns True if AT LEAST ONE operand is True
print("\n=== LOGICAL OR (or) ===")
print(f"True or True: {True or True}")
print(f"True or False: {True or False}")
print(f"False or True: {False or True}")
print(f"False or False: {False or False}")

# OR with truthy/falsy values
# Returns the FIRST TRUTHY value or the LAST value if all are falsy
print(f"\nTruthy/falsy behavior:")
print(f"5 or 10: {5 or 10}")            # Returns 5 (first truthy)
print(f"0 or 10: {0 or 10}")            # Returns 10 (first truthy)
print(f"0 or '': {0 or ''}")            # Returns '' (both falsy, returns last)
print(f"None or False: {None or False}") # Returns False (both falsy, returns last)

# Short-circuit evaluation: second operand not evaluated if first is truthy
print(f"\nShort-circuit demonstration:")
result = True or expensive_operation()  # expensive_operation() never called
print(f"True or expensive_operation(): {result}")

# === LOGICAL NOT OPERATOR ===
# Inverts the boolean value
print("\n=== LOGICAL NOT (not) ===")
print(f"not True: {not True}")
print(f"not False: {not False}")
print(f"not 5: {not 5}")          # 5 is truthy, so not 5 is False
print(f"not 0: {not 0}")          # 0 is falsy, so not 0 is True
print(f"not 'hello': {not 'hello'}")  # Non-empty string is truthy
print(f"not '': {not ''}")        # Empty string is falsy

# === COMBINING LOGICAL OPERATORS ===
# Evaluation order: not > and > or
print("\n=== COMBINING OPERATORS ===")
result = True and False or True
print(f"True and False or True: {result}")  # (True and False) or True = False or True = True

result = True or False and True
print(f"True or False and True: {result}")  # True or (False and True) = True or False = True

# Using parentheses for clarity
result = (True and False) or True
print(f"(True and False) or True: {result}")

result = True or (False and True)
print(f"True or (False and True): {result}")

# === PRACTICAL EXAMPLES ===
# Checking multiple conditions
age = 25
has_id = True
is_student = False

# Can enter club if adult and has ID
can_enter = age >= 18 and has_id
print(f"\nCan enter club: {can_enter}")

# Discount eligibility: student or senior
is_senior = age >= 65
gets_discount = is_student or is_senior
print(f"Gets discount: {gets_discount}")

# Complex condition: adult with ID, not a student
is_adult = age >= 18
can_drink = is_adult and has_id and not is_student
print(f"Can drink: {can_drink}")

# === GUARD PATTERN ===
# Use OR to provide default values
name = ""
default_name = "Guest"
display_name = name or default_name
print(f"\nDisplay name: '{display_name}'")

# None checking with default
user_input = None
safe_value = user_input or "default"
print(f"Safe value: '{safe_value}'")

# === CHAINING WITH COMPARISONS ===
# Combine logical operators with comparisons
x = 5
result = x > 0 and x < 10
print(f"\n{x} > 0 and {x} < 10: {result}")

# Same as chained comparison
result = 0 < x < 10
print(f"0 < {x} < 10: {result}")

# === BOOLEAN ALGEBRA LAWS ===
# Demonstrating De Morgan's Laws
a = True
b = False

# NOT (A AND B) = (NOT A) OR (NOT B)
left1 = not (a and b)
right1 = (not a) or (not b)
print(f"\nDe Morgan's Law 1:")
print(f"not ({a} and {b}) = {left1}")
print(f"(not {a}) or (not {b}) = {right1}")
print(f"Are equal: {left1 == right1}")

# NOT (A OR B) = (NOT A) AND (NOT B)
left2 = not (a or b)
right2 = (not a) and (not b)
print(f"\nDe Morgan's Law 2:")
print(f"not ({a} or {b}) = {left2}")
print(f"(not {a}) and (not {b}) = {right2}")
print(f"Are equal: {left2 == right2}")
