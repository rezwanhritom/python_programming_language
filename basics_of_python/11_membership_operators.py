# Python Membership Operators - Complete Reference
# Membership operators test whether a value is present in a sequence or collection.
# Operators: 'in' and 'not in'

# === MEMBERSHIP IN STRINGS ===
# Strings are sequences of characters
print("=== MEMBERSHIP IN STRINGS ===")
text = "hello world"

# Check if substring exists
print(f"'hello' in '{text}': {'hello' in text}")
print(f"'world' in '{text}': {'world' in text}")
print(f"'python' in '{text}': {'python' in text}")

# Check single character
print(f"'h' in '{text}': {'h' in text}")
print(f"'x' in '{text}': {'x' in text}")

# Case-sensitive check
print(f"'Hello' in '{text}': {'Hello' in text}")  # False (case matters)

# Using not in
print(f"'python' not in '{text}': {'python' not in text}")


# === MEMBERSHIP IN LISTS ===
print("\n=== MEMBERSHIP IN LISTS ===")
fruits = ["apple", "banana", "cherry", "date"]

print(f"'apple' in {fruits}: {'apple' in fruits}")
print(f"'mango' in {fruits}: {'mango' in fruits}")
print(f"'banana' not in {fruits}: {'banana' not in fruits}")

# Membership check is O(n) for lists (linear search)
large_list = list(range(10000))
print(f"\n9999 in large_list: {9999 in large_list}")  # True
print(f"10000 in large_list: {10000 in large_list}")  # False


# === MEMBERSHIP IN TUPLES ===
print("\n=== MEMBERSHIP IN TUPLES ===")
coordinates = (10, 20, 30, 40, 50)

print(f"20 in {coordinates}: {20 in coordinates}")
print(f"25 in {coordinates}: {25 in coordinates}")
print(f"60 not in {coordinates}: {60 not in coordinates}")

# Tuples have same O(n) membership performance as lists


# === MEMBERSHIP IN SETS ===
print("\n=== MEMBERSHIP IN SETS ===")
unique_fruits = {"apple", "banana", "cherry"}

print(f"'apple' in {unique_fruits}: {'apple' in unique_fruits}")
print(f"'mango' in {unique_fruits}: {'mango' in unique_fruits}")

# Sets have O(1) average case for membership checks (hash table)
# This makes them much faster than lists/tuples for large collections
large_set = set(range(1000000))
print(f"\n999999 in large_set: {999999 in large_set}")  # Very fast
print(f"1000000 in large_set: {1000000 in large_set}")  # Very fast


# === MEMBERSHIP IN DICTIONARIES ===
print("\n=== MEMBERSHIP IN DICTIONARIES ===")
person = {"name": "Alice", "age": 30, "city": "New York"}

# 'in' checks KEYS by default
print(f"'name' in person: {'name' in person}")
print(f"'Alice' in person: {'Alice' in person}")  # False (checks keys, not values)
print(f"'country' in person: {'country' in person}")

# Check values explicitly
print(f"'Alice' in person.values(): {'Alice' in person.values()}")
print(f"30 in person.values(): {30 in person.values()}")

# Check items (key-value pairs as tuples)
print(f"('name', 'Alice') in person.items(): {('name', 'Alice') in person.items()}")


# === PRACTICAL EXAMPLES ===

# 1. Input validation
valid_options = ["yes", "no", "maybe"]
user_input = "yes"
if user_input in valid_options:
    print(f"\nValid input: {user_input}")
else:
    print(f"\nInvalid input: {user_input}")

# 2. Filtering data
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [n for n in numbers if n % 2 == 0]
print(f"Even numbers: {evens}")

# 3. Checking for forbidden characters
username = "user@name"
forbidden_chars = ["@", "#", "$"]
if any(char in username for char in forbidden_chars):
    print(f"\nUsername '{username}' contains forbidden characters")

# 4. Set operations for fast lookups
allowed_ips = {"192.168.1.1", "192.168.1.2", "10.0.0.1"}
request_ip = "192.168.1.1"
if request_ip in allowed_ips:
    print(f"\nAccess granted for IP: {request_ip}")

# 5. Checking dictionary keys before access
config = {"host": "localhost", "port": 8080}
key = "host"
if key in config:
    print(f"\n{key}: {config[key]}")
else:
    print(f"\nKey '{key}' not found in config")
