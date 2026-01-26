# Python Comparison Operators - Complete Reference
# These operators compare values and return True or False

# === EQUALITY OPERATOR (==) ===
# Checks if values are equal
print("=== EQUALITY OPERATOR (==) ===")
print(f"5 == 5: {5 == 5}")
print(f"5 == 3: {5 == 3}")
print(f"'hello' == 'hello': {'hello' == 'hello'}")
print(f"'hello' == 'world': {'hello' == 'world'}")
print(f"[1, 2] == [1, 2]: {[1, 2] == [1, 2]}")
print(f"[1, 2] == [2, 1]: {[1, 2] == [2, 1]}")

# === INEQUALITY OPERATOR (!=) ===
# Checks if values are not equal
print("\n=== INEQUALITY OPERATOR (!=) ===")
print(f"5 != 3: {5 != 3}")
print(f"5 != 5: {5 != 5}")
print(f"'a' != 'b': {'a' != 'b'}")
print(f"'a' != 'a': {'a' != 'a'}")

# === GREATER THAN (>) ===
# Checks if left is greater than right
print("\n=== GREATER THAN (>) ===")
print(f"10 > 5: {10 > 5}")
print(f"5 > 10: {5 > 10}")
print(f"7 > 7: {7 > 7}")
print(f"'b' > 'a': {'b' > 'a'}")  # String comparison (lexicographical)
print(f"'apple' > 'banana': {'apple' > 'banana'}")

# === LESS THAN (<) ===
# Checks if left is less than right
print("\n=== LESS THAN (<) ===")
print(f"5 < 10: {5 < 10}")
print(f"10 < 5: {10 < 5}")
print(f"7 < 7: {7 < 7}")
print(f"'a' < 'b': {'a' < 'b'}")
print(f"'banana' < 'apple': {'banana' < 'apple'}")

# === GREATER THAN OR EQUAL (>=) ===
# Checks if left is greater than or equal to right
print("\n=== GREATER THAN OR EQUAL (>=) ===")
print(f"10 >= 5: {10 >= 5}")
print(f"10 >= 10: {10 >= 10}")
print(f"5 >= 10: {5 >= 10}")

# === LESS THAN OR EQUAL (<=) ===
# Checks if left is less than or equal to right
print("\n=== LESS THAN OR EQUAL (<=) ===")
print(f"5 <= 10: {5 <= 10}")
print(f"10 <= 10: {10 <= 10}")
print(f"10 <= 5: {10 <= 5}")

# === COMPARISON CHAINING ===
# Python allows chaining comparisons naturally
print("\n=== COMPARISON CHAINING ===")
x = 5
result = 1 < x < 10  # Same as: 1 < x and x < 10
print(f"1 < {x} < 10: {result}")

result = 10 < x < 20
print(f"10 < {x} < 20: {result}")

# Chain multiple comparisons
result = 0 < x <= 5 < 20
print(f"0 < {x} <= 5 < 20: {result}")

# === COMPARING DIFFERENT TYPES ===
# Python 3 doesn't allow comparison of incompatible types
# print(5 < "hello")  # TypeError: '<' not supported between instances of 'int' and 'str'

# But some comparisons work
print(f"5 == 5.0: {5 == 5.0}")  # True (same numeric value)
print(f"True == 1: {True == 1}")  # True
print(f"False == 0: {False == 0}")  # True

# === IS OPERATOR vs == OPERATOR ===
# == compares values, is compares object identity
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"\nlist1 == list2: {list1 == list2}")  # True (same content)
print(f"list1 is list2: {list1 is list2}")    # False (different objects)
print(f"list1 is list3: {list1 is list3}")    # True (same object)

# === COMPARING SEQUENCES ===
# Sequences compare element by element
print(f"\n[1, 2, 3] < [1, 2, 4]: {[1, 2, 3] < [1, 2, 4]}")
print(f"[1, 2, 3] < [1, 2]: {[1, 2, 3] < [1, 2]}")  # Longer is greater
print(f"'abc' < 'abd': {'abc' < 'abd'}")
print(f"'abc' < 'abcd': {'abc' < 'abcd'}")

# === COMPARING WITH NONE ===
print(f"\nNone == None: {None == None}")
print(f"None is None: {None is None}")
print(f"0 == None: {0 == None}")
print(f"0 is None: {0 is None}")

# === PRACTICAL EXAMPLES ===
# Finding if value is in range
age = 25
is_adult = 18 <= age <= 65
print(f"\nAge {age} is adult (18-65): {is_adult}")

# Checking valid percentage
percentage = 85
is_valid = 0 <= percentage <= 100
print(f"Percentage {percentage} is valid: {is_valid}")

# Sorting based on comparison
numbers = [5, 2, 8, 1, 9]
sorted_numbers = sorted(numbers)
print(f"\nOriginal: {numbers}")
print(f"Sorted: {sorted_numbers}")
print(f"Is sorted: {sorted_numbers == sorted(numbers)}")
