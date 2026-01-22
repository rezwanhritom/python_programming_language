# Python Dictionaries - Complete Basics Reference
# Unordered (ordered in Python 3.7+), mutable key-value mappings

# === DICTIONARY CREATION ===
print("=== DICTIONARY CREATION ===")
empty_dict = {}
print(f"Empty dict: {empty_dict}, type: {type(empty_dict)}")

person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "is_student": False
}
print(f"Person dict: {person}")

# Using dict() constructor
from_dict = dict(name="Bob", age=25, city="London")
print(f"From dict(): {from_dict}")

# From list of tuples
pairs = [("name", "Charlie"), ("age", 35), ("city", "Paris")]
from_tuples = dict(pairs)
print(f"From list of tuples: {from_tuples}")

# From zip
keys = ["name", "age", "city"]
values = ["David", 40, "Tokyo"]
from_zip = dict(zip(keys, values))
print(f"From zip: {from_zip}")


# === DICTIONARY KEYS ===
print("\n=== DICTIONARY KEYS ===")
person = {"name": "Alice", "age": 30, "city": "New York"}

# Access keys view
keys_view = person.keys()
print(f"person.keys(): {keys_view}")
print(f"type(keys_view): {type(keys_view)}")

# Convert to list
keys_list = list(person.keys())
print(f"list(person.keys()): {keys_list}")

# Iterate over keys
print("Iterating over keys:")
for key in person.keys():
    print(f"  {key}")


# === DICTIONARY VALUES ===
print("\n=== DICTIONARY VALUES ===")
person = {"name": "Alice", "age": 30, "city": "New York"}

# Access values view
values_view = person.values()
print(f"person.values(): {values_view}")
print(f"type(values_view): {type(values_view)}")

# Convert to list
values_list = list(person.values())
print(f"list(person.values()): {values_list}")

# Iterate over values
print("Iterating over values:")
for value in person.values():
    print(f"  {value}")


# === DICTIONARY ITEMS ===
print("\n=== DICTIONARY ITEMS ===")
person = {"name": "Alice", "age": 30, "city": "New York"}

# Access items view (key-value pairs)
items_view = person.items()
print(f"person.items(): {items_view}")
print(f"type(items_view): {type(items_view)}")

# Convert to list
items_list = list(person.items())
print(f"list(person.items()): {items_list}")

# Iterate over items
print("Iterating over items:")
for key, value in person.items():
    print(f"  {key}: {value}")


# === DICTIONARY LENGTH ===
print("\n=== DICTIONARY LENGTH ===")
person = {"name": "Alice", "age": 30, "city": "New York"}
print(f"len(person): {len(person)}")

empty = {}
print(f"len(empty): {len(empty)}")

nested = {"a": {"x": 1}, "b": {"y": 2}}
print(f"len(nested): {len(nested)}")  # Counts top-level keys only


# === DICTIONARY KEY ACCESS ===
print("\n=== DICTIONARY KEY ACCESS ===")
person = {"name": "Alice", "age": 30, "city": "New York"}

# Access via bracket notation
print(f"person['name']: {person['name']}")
print(f"person['age']: {person['age']}")

# Access via get() method (safe)
print(f"person.get('name'): {person.get('name')}")
print(f"person.get('city'): {person.get('city')}")

# get() with default value
print(f"person.get('country', 'Unknown'): {person.get('country', 'Unknown')}")

# KeyError if key doesn't exist
# print(person["country"])  # KeyError: 'country'


# === DICTIONARY KEY CHECKING ===
print("\n=== DICTIONARY KEY CHECKING ===")
person = {"name": "Alice", "age": 30, "city": "New York"}

print(f"'name' in person: {'name' in person}")
print(f"'country' in person: {'country' in person}")
print(f"'age' not in person: {'age' not in person}")

# Recommended pattern
key = "email"
if key in person:
    print(f"{key}: {person[key]}")
else:
    print(f"{key} not found")


# === ADDING/UPDATING ENTRIES ===
print("\n=== ADDING/UPDATING ENTRIES ===")
person = {"name": "Alice", "age": 30}
print(f"Original: {person}")

# Add new key-value pair
person["city"] = "New York"
print(f"After adding city: {person}")

# Update existing value
person["age"] = 31
print(f"After updating age: {person}")

# Multiple updates
person.update({"city": "London", "email": "alice@example.com", "age": 32})
print(f"After update(): {person}")

# Update with keyword arguments
person.update(country="UK", phone="123-456")
print(f"After update with kwargs: {person}")


# === REMOVING ENTRIES ===
print("\n=== REMOVING ENTRIES ===")
person = {"name": "Alice", "age": 30, "city": "New York", "temp": "to_remove"}
print(f"Original: {person}")

# Remove with del
del person["temp"]
print(f"After del person['temp']: {person}")

# Remove with pop() (returns value)
age = person.pop("age")
print(f"Popped age: {age}, dict: {person}")

# pop() with default value
email = person.pop("email", "not found")
print(f"Popped email: {email}, dict: {person}")

# popitem() removes and returns last inserted key-value pair (Python 3.7+)
last_item = person.popitem()
print(f"Popped item: {last_item}, dict: {person}")

# Clear all entries
person.clear()
print(f"After clear(): {person}")


# === DICTIONARY COPYING ===
print("\n=== DICTIONARY COPYING ===")
original = {"name": "Alice", "age": 30, "city": "New York"}

# Shallow copy with copy()
copy1 = original.copy()
print(f"Original: {original}")
print(f"Copy: {copy1}")
print(f"Are same object: {original is copy1}")
print(f"Have same values: {original == copy1}")

# Shallow copy with dict()
copy2 = dict(original)
print(f"Copy with dict(): {copy2}")

# Modify copy
copy1["age"] = 31
print(f"After modifying copy['age'] = 31:")
print(f"Original: {original}")
print(f"Copy: {copy1}")


# === NESTED DICTIONARIES ===
print("\n=== NESTED DICTIONARIES ===")
company = {
    "name": "Tech Corp",
    "employees": {
        "manager": {
            "name": "Bob",
            "age": 40,
            "department": "Engineering"
        },
        "developer": {
            "name": "Charlie",
            "age": 25,
            "department": "Engineering"
        }
    },
    "location": "New York"
}

print(f"Company name: {company['name']}")
print(f"Manager name: {company['employees']['manager']['name']}")
print(f"Developer department: {company['employees']['developer']['department']}")

# Modify nested entries
company["employees"]["manager"]["age"] = 41
print(f"After manager age update: {company['employees']['manager']}")

# Add nested entry
company["employees"]["designer"] = {
    "name": "Diana",
    "age": 28,
    "department": "Design"
}
print(f"After adding designer: {company['employees']}")


# === DICTIONARY COMPREHENSION BASICS ===
print("\n=== DICTIONARY COMPREHENSION BASICS ===")
numbers = [1, 2, 3, 4, 5]
squares = {n: n**2 for n in numbers}
print(f"Original: {numbers}")
print(f"Squares dict: {squares}")

# With condition
even_squares = {n: n**2 for n in numbers if n % 2 == 0}
print(f"Even squares: {even_squares}")

# From two lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
paired = {k: v for k, v in zip(keys, values)}
print(f"Paired dict: {paired}")


# === DICTIONARY FROM KEYS ===
print("\n=== DICTIONARY FROM KEYS ===")
# Create dict with default value for each key
keys = ["name", "age", "city"]
default_dict = dict.fromkeys(keys, "unknown")
print(f"Keys: {keys}")
print(f"Default dict: {default_dict}")

# Default value can be any type
keys = ["a", "b", "c"]
default_list_dict = dict.fromkeys(keys, [])
print(f"Default list dict: {default_list_dict}")

# Be careful with mutable defaults (shared reference)
default_list_dict["a"].append(1)
print(f"After appending to 'a': {default_list_dict}")  # All lists modified!

# Better approach for mutable defaults
keys = ["a", "b", "c"]
safe_dict = {k: [] for k in keys}
print(f"\nSafe dict: {safe_dict}")
safe_dict["a"].append(1)
print(f"After appending to 'a': {safe_dict}")  # Only 'a' modified


# === DICTIONARY ITERATION ===
print("\n=== DICTIONARY ITERATION ===")
person = {"name": "Alice", "age": 30, "city": "New York"}

print("Iterating over keys:")
for key in person:
    print(f"  {key}")

print("\nIterating over values:")
for value in person.values():
    print(f"  {value}")

print("\nIterating over items:")
for key, value in person.items():
    print(f"  {key}: {value}")


# === DICTIONARY BOOLEAN CONTEXT ===
print("\n=== DICTIONARY BOOLEAN CONTEXT ===")
empty = {}
non_empty = {"key": "value"}

print(f"bool({{}}): {bool(empty)}")
print(f"bool({{'key': 'value'}}): {bool(non_empty)}")

if non_empty:
    print("Dictionary has entries")
else:
    print("Dictionary is empty")


# === DICTIONARY TYPE CHECKING ===
print("\n=== DICTIONARY TYPE CHECKING ===")
person = {"name": "Alice", "age": 30}

print(f"type(person): {type(person)}")
print(f"isinstance(person, dict): {isinstance(person, dict)}")
print(f"isinstance(person, (dict, list)): {isinstance(person, (dict, list))}")


# === DICTIONARY KEYS MUST BE HASHABLE ===
print("\n=== DICTIONARY KEYS MUST BE HASHABLE ===")
# Valid keys (immutable types)
valid_dict = {
    "string": "value1",
    42: "value2",
    3.14: "value3",
    True: "value4",
    (1, 2): "value5"  # Tuple is hashable if all elements are hashable
}
print(f"Valid dict: {valid_dict}")

# Invalid keys (mutable types)
# invalid_dict = {
#     [1, 2]: "value"  # TypeError: unhashable type: 'list'
# }

# invalid_dict = {
#     {"key": "value"}: "value"  # TypeError: unhashable type: 'dict'
# }

# invalid_dict = {
#     {1, 2}: "value"  # TypeError: unhashable type: 'set'
# }


# === DICTIONARY VALUES CAN BE ANY TYPE ===
print("\n=== DICTIONARY VALUES CAN BE ANY TYPE ===")
mixed_values = {
    "string": "text",
    "number": 42,
    "list": [1, 2, 3],
    "dict": {"nested": "value"},
    "set": {1, 2, 3},
    "tuple": (1, 2, 3),
    "function": lambda x: x * 2
}
print(f"Mixed values dict: {mixed_values}")


# === DICTIONARY VIEW OBJECTS ===
print("\n=== DICTIONARY VIEW OBJECTS ===")
person = {"name": "Alice", "age": 30, "city": "New York"}

keys = person.keys()
values = person.values()
items = person.items()

print(f"Keys view: {keys}")
print(f"Values view: {values}")
print(f"Items view: {items}")

# Views are dynamic
person["email"] = "alice@example.com"
print(f"\nAfter adding email:")
print(f"Keys view: {keys}")    # Automatically includes new key
print(f"Values view: {values}")  # Automatically includes new value
print(f"Items view: {items}")   # Automatically includes new item

# Views support set operations (keys and items only)
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 2, "c": 4, "d": 5}

print(f"\ndict1 keys: {dict1.keys()}")
print(f"dict2 keys: {dict2.keys()}")
print(f"Intersection: {dict1.keys() & dict2.keys()}")
print(f"Union: {dict1.keys() | dict2.keys()}")
print(f"Difference: {dict1.keys() - dict2.keys()}")


# === DICTIONARY PERFORMANCE ===
print("\n=== DICTIONARY PERFORMANCE ===")
print("Key lookup: O(1) average case")
print("Insertion: O(1) average case")
print("Deletion: O(1) average case")
print("Iteration: O(n) where n is number of items")


# === PRACTICAL EXAMPLES ===

# 1. Word frequency counter
print("\n=== PRACTICAL: WORD FREQUENCY COUNTER ===")
text = "hello world hello python world hello"
words = text.split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(f"Text: '{text}'")
print(f"Word frequency: {frequency}")

# Using count() approach
frequency2 = {}
for word in set(words):
    frequency2[word] = words.count(word)
print(f"Alternative frequency: {frequency2}")


# 2. Phone book simulation
print("\n=== PRACTICAL: PHONE BOOK ===")
phone_book = {
    "Alice": "555-0101",
    "Bob": "555-0102",
    "Charlie": "555-0103"
}

name = input("Enter name to lookup: ")
if name in phone_book:
    print(f"{name}: {phone_book[name]}")
else:
    print(f"{name} not found")


# 3. Configuration management
print("\n=== PRACTICAL: CONFIGURATION ===")
config = {
    "host": "localhost",
    "port": 8080,
    "debug": True,
    "database": {
        "name": "myapp",
        "user": "admin",
        "password": "secret"
    }
}

print(f"Host: {config['host']}")
print(f"Database name: {config['database']['name']}")


# 4. Data grouping
print("\n=== PRACTICAL: DATA GROUPING ===")
students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob", "grade": "B"},
    {"name": "Charlie", "grade": "A"},
    {"name": "David", "grade": "C"}
]

grouped = {}
for student in students:
    grade = student["grade"]
    if grade not in grouped:
        grouped[grade] = []
    grouped[grade].append(student["name"])

print(f"Students grouped by grade: {grouped}")


# 5. Caching/memoization
print("\n=== PRACTICAL: CACHING ===")
cache = {}

def expensive_function(n):
    """Simulate expensive computation with caching"""
    if n in cache:
        return cache[n]
    
    # Simulate expensive computation
    import time
    time.sleep(0.1)
    result = n ** 2
    
    cache[n] = result
    return result

print("First call (slow):")
result1 = expensive_function(42)
print(f"Result: {result1}")

print("\nSecond call (fast from cache):")
result2 = expensive_function(42)
print(f"Result: {result2}")
print(f"Cache: {cache}")


# === FINAL SUMMARY ===
print("\n=== FINAL SUMMARY ===")
print("Dictionaries are key-value mappings with O(1) lookup")
print("Keys must be immutable and hashable")
print("Values can be any type")
print("Use bracket notation or get() for access")
print("Use in/not in for membership testing")
print("Methods: keys(), values(), items() return dynamic views")
print("Comprehensions: {k: v for ...}")
