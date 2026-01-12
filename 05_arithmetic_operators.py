# Python Arithmetic Operators - Complete Reference
# This file demonstrates all arithmetic operators with every possible variation

# === ADDITION OPERATOR (+) ===
# Adds two numbers or concatenates sequences
num1 = 15
num2 = 7
result_add = num1 + num2
print(f"Addition: {num1} + {num2} = {result_add}")

# Addition with different types (type promotion)
int_float_add = 5 + 3.0
print(f"Int + Float: 5 + 3.0 = {int_float_add} (type: {type(int_float_add)})")

# String concatenation
str1 = "Hello"
str2 = "World"
combined = str1 + " " + str2
print(f"String addition: '{str1}' + ' ' + '{str2}' = '{combined}'")

# List concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print(f"List addition: {list1} + {list2} = {combined_list}")

# === SUBTRACTION OPERATOR (-) ===
# Subtracts right operand from left operand
result_sub = num1 - num2
print(f"\nSubtraction: {num1} - {num2} = {result_sub}")

# Negative numbers
negative = -42
print(f"Negative number: {negative}")

# Unary minus (negation)
positive = 50
negated = -positive
print(f"Unary minus: -{positive} = {negated}")

# === MULTIPLICATION OPERATOR (*) ===
# Multiplies two numbers or repeats sequences
result_mul = num1 * num2
print(f"\nMultiplication: {num1} * {num2} = {result_mul}")

# String repetition
repeated = "Hi " * 3
print(f"String repetition: 'Hi ' * 3 = '{repeated}'")

# List repetition
repeated_list = [0] * 5
print(f"List repetition: [0] * 5 = {repeated_list}")

# === DIVISION OPERATOR (/) ===
# Always returns float in Python 3
result_div = num1 / num2
print(f"\nDivision: {num1} / {num2} = {result_div} (type: {type(result_div)})")

# Division by zero raises ZeroDivisionError
# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Cannot divide by zero!")

# Division with negative numbers
neg_div = -15 / 7
print(f"Negative division: -15 / 7 = {neg_div}")

# === FLOOR DIVISION OPERATOR (//) ===
# Divides and rounds down to nearest integer
result_floor = num1 // num2
print(f"\nFloor division: {num1} // {num2} = {result_floor}")

# Floor division with negative numbers (rounds toward negative infinity)
neg_floor = -15 // 7
print(f"Negative floor division: -15 // 7 = {neg_floor} (rounds down)")

# Floor division with floats
float_floor = 15.0 // 7.0
print(f"Float floor division: 15.0 // 7.0 = {float_floor} (type: {type(float_floor)})")

# === MODULUS OPERATOR (%) ===
# Returns remainder of division
result_mod = num1 % num2
print(f"\nModulus: {num1} % {num2} = {result_mod}")

# Modulus use cases: checking even/odd
number = 42
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# Modulus with negative numbers
neg_mod = -15 % 7
print(f"Negative modulus: -15 % 7 = {neg_mod} (result is always non-negative)")

# === EXPONENTIATION OPERATOR (**) ===
# Raises left operand to power of right operand
result_exp = num1 ** num2
print(f"\nExponentiation: {num1} ** {num2} = {result_exp}")

# Square root (power of 0.5)
sqrt_16 = 16 ** 0.5
print(f"Square root: 16 ** 0.5 = {sqrt_16}")

# Cube root (power of 1/3)
cbrt_27 = 27 ** (1/3)
print(f"Cube root: 27 ** (1/3) = {cbrt_27}")

# Negative exponent (reciprocal)
reciprocal = 2 ** -1
print(f"Reciprocal: 2 ** -1 = {reciprocal}")

# === AUGMENTED ARITHMETIC ASSIGNMENT ===
# Combine arithmetic operation with assignment
value = 10
print(f"\nInitial value: {value}")

value += 5  # Same as: value = value + 5
print(f"After += 5: {value}")

value -= 3  # Same as: value = value - 3
print(f"After -= 3: {value}")

value *= 2  # Same as: value = value * 2
print(f"After *= 2: {value}")

value /= 4  # Same as: value = value / 4
print(f"After /= 4: {value}")

value //= 2  # Same as: value = value // 2
print(f"After //= 2: {value}")

value %= 3  # Same as: value = value % 3
print(f"After %= 3: {value}")

value **= 2  # Same as: value = value ** 2
print(f"After **= 2: {value}")

# === OPERATOR PRECEDENCE ===
# Python evaluates operators in specific order
# 1. Parentheses
# 2. Exponentiation
# 3. Multiplication, Division, Floor Division, Modulus
# 4. Addition, Subtraction
# 5. Assignment (lowest)

result = 2 + 3 * 4  # Multiplication first: 3*4=12, then 2+12=14
print(f"\nOperator precedence: 2 + 3 * 4 = {result}")

result_with_parens = (2 + 3) * 4  # Parentheses first: 2+3=5, then 5*4=20
print(f"With parentheses: (2 + 3) * 4 = {result_with_parens}")

# Complex precedence example
complex_result = 2 + 3 * 4 ** 2 // 5 - 1
print(f"Complex: 2 + 3 * 4 ** 2 // 5 - 1 = {complex_result}")
# Steps: 4**2=16, 3*16=48, 48//5=9, 2+9=11, 11-1=10

# === DIVMOD FUNCTION ===
# Returns both quotient and remainder
quotient, remainder = divmod(num1, num2)
print(f"\ndivmod({num1}, {num2}) = ({quotient}, {remainder})")

# === ABSOLUTE VALUE ===
# abs() returns magnitude without sign
negative = -42
positive = abs(negative)
print(f"Absolute value: abs({negative}) = {positive}")

# === ROUND FUNCTION ===
# Rounds to nearest integer or specified decimal places
float_num = 3.14159
rounded1 = round(float_num)
rounded2 = round(float_num, 2)
rounded3 = round(float_num, 4)
print(f"\nround({float_num}) = {rounded1}")
print(f"round({float_num}, 2) = {rounded2}")
print(f"round({float_num}, 4) = {rounded3}")

# Round with negative precision
large_num = 12345
rounded_large = round(large_num, -2)  # Round to nearest hundred
print(f"round({large_num}, -2) = {rounded_large}")
