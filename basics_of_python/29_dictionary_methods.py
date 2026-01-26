# Python Dictionary Methods - Complete Reference
# All built-in dictionary methods with examples

# === CLEAR() ===
print("=== DICTIONARY CLEAR() ===")
person = {"name": "Alice", "age": 30, "city": "New York"}
print(f"Before clear: {person}")
person.clear()
print(f"After clear(): {person}")

# Clear vs reassign
# clear() modifies existing dict
# reassignment creates new dict object
original = {"key": "value"}
id_before = id(original)
original.clear()
id_after = id(original)
print(f"Same object after clear: {id_before == id_after}")

original = {"key": "value"}
id_before = id(original)
original = {}
id_after = id(original)
print(f"Different object after reassignment: {id_before != id_after}")


# === COPY() ===
print("\n=== DICTIONARY COPY() ===")
original = {"name": "Alice", "age": 30, "city": "New York"}
copy = original.copy()
print(f"Original: {original}")
print(f"Copy: {copy}")
print(f"Same object: {original is copy}")
print(f"Same values: {original == copy}")

# Modify copy
copy["age"] = 31
print(f"After modifying copy['age'] = 31:")
print(f"Original: {original}")
print(f"Copy: {copy}")


# === FROMKEYS() ===
print("\n=== DICTIONARY FROMKEYS() ===")
keys = ["name", "age", "city"]
default_dict = dict.fromkeys(keys, "unknown")
print(f"Keys: {keys}")
print(f"Dict fromkeys with default 'unknown': {default_dict}")

# Different default value
keys = ["a", "b", "c"]
zero_dict = dict.fromkeys(keys, 0)
print(f"Dict fromkeys with default 0: {zero_dict}")

# Mutable default (shared reference warning)
keys = ["a", "b", "c"]
list_dict = dict.fromkeys(keys, [])
print(f"Dict fromkeys with default []: {list_dict}")
list_dict["a"].append(1)
print(f"After appending to key 'a': {list_dict}")  # All keys share same list!

# Better approach for mutable defaults
keys = ["a", "b", "c"]
safe_dict = {k: [] for k in keys}
print(f"\nSafe dict with comprehension: {safe_dict}")
safe_dict["a"].append(1)
print(f"After appending to 'a': {safe_dict}")  # Only 'a' modified


# === GET() ===
print("\n=== DICTIONARY GET() ===")
person = {"name": "Alice", "age": 30}

# Existing key
print(f"person.get('name'): {person.get('name')}")

# Non-existing key (returns None)
print(f"person.get('email'): {person.get('email')}")

# Non-existing key with default
print(f"person.get('email', 'Not found'): {person.get('email', 'Not found')}")

# Existing key (default is ignored)
print(f"person.get('name', 'Default'): {person.get('name', 'Default')}")


# === ITEMS() ===
print("\n=== DICTIONARY ITEMS() ===")
person = {"name": "Alice", "age": 30, "city": "New York"}
items = person.items()
print(f"person.items(): {items}")
print(f"type(items): {type(items)}")

# Convert to list
items_list = list(items)
print(f"list(person.items()): {items_list}")

# Iterate over items
print("Iterating over items:")
for key, value in person.items():
    print(f"  {key}: {value}")

# Items view is dynamic
person["email"] = "alice@example.com"
print(f"After adding email, items view: {items}")  # Automatically updated

# Set operations on items view (Python 3.8+)
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 2, "c": 4, "d": 5}

# Intersection (common key-value pairs)
common = dict1.items() & dict2.items()
print(f"Common items: {common}")

# Difference
diff = dict1.items() - dict2.items()
print(f"Items in dict1 but not dict2: {diff}")


# === KEYS() ===
print("\n=== DICTIONARY KEYS() ===")
person = {"name": "Alice", "age": 30, "city": "New York"}
keys = person.keys()
print(f"person.keys(): {keys}")
print(f"type(keys): {type(keys)}")

# Convert to list
keys_list = list(keys)
print(f"list(person.keys()): {keys_list}")

# Iterate over keys
print("Iterating over keys:")
for key in person.keys():
    print(f"  {key}")

# Keys view is dynamic
person["email"] = "alice@example.com"
print(f"After adding email, keys view: {keys}")  # Automatically updated

# Set operations on keys view
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 20, "c": 30, "d": 4}

print(f"dict1 keys: {dict1.keys()}")
print(f"dict2 keys: {dict2.keys()}")
print(f"Intersection: {dict1.keys() & dict2.keys()}")
print(f"Union: {dict1.keys() | dict2.keys()}")
print(f"Difference: {dict1.keys() - dict2.keys()}")
print(f"Symmetric difference: {dict1.keys() ^ dict2.keys()}")


# === POP() ===
print("\n=== DICTIONARY POP() ===")
person = {"name": "Alice", "age": 30, "city": "New York"}
print(f"Original: {person}")

# Pop existing key
age = person.pop("age")
print(f"Popped age: {age}")
print(f"After pop('age'): {person}")

# Pop non-existing key (with default)
email = person.pop("email", "not found")
print(f"Popped email: {email}")

# Pop non-existing key (without default)
# country = person.pop("country")  # KeyError: 'country'

# Pop with default value
city = person.pop("city", "unknown")
print(f"Popped city: {city}")
print(f"After pop operations: {person}")


# === POPITEM() ===
print("\n=== DICTIONARY POPITEM() ===")
# Removes and returns last inserted key-value pair (Python 3.7+)

person = {"name": "Alice", "age": 30, "city": "New York"}
print(f"Original: {person}")

last_item = person.popitem()
print(f"Popped item: {last_item}")
print(f"Type: {type(last_item)}")  # Returns tuple
print(f"After popitem(): {person}")

# Pop another item
another_item = person.popitem()
print(f"Popped another item: {another_item}")
print(f"After second popitem(): {person}")

# Pop from empty dict
# empty = {}
# empty.popitem()  # KeyError: 'popitem(): dictionary is empty'


# === SETDEFAULT() ===
print("\n=== DICTIONARY SETDEFAULT() ===")
# Gets value for key if exists, otherwise sets default value and returns it

person = {"name": "Alice", "age": 30}
print(f"Original: {person}")

# Key exists
age = person.setdefault("age", 25)
print(f"setdefault('age', 25): {age}")  # Returns existing value
print(f"Dict unchanged: {person}")

# Key doesn't exist (sets and returns default)
country = person.setdefault("country", "USA")
print(f"setdefault('country', 'USA'): {country}")  # Returns new value
print(f"Dict updated: {person}")

# Without default value (uses None)
email = person.setdefault("email")
print(f"setdefault('email'): {email}")  # Returns None
print(f"Dict updated with None: {person}")


# === UPDATE() ===
print("\n=== DICTIONARY UPDATE() ===")
person = {"name": "Alice", "age": 30}
print(f"Original: {person}")

# Update with another dict
person.update({"city": "New York", "email": "alice@example.com"})
print(f"After update with dict: {person}")

# Update with keyword arguments
person.update(country="USA", phone="123-456")
print(f"After update with kwargs: {person}")

# Update with list of key-value pairs
person.update([("occupation", "Engineer"), ("salary", 50000)])
print(f"After update with list: {person}")

# Update with tuple of key-value pairs
person.update((("company", "Tech Corp"), ("years", 5)))
print(f"After update with tuple: {person}")

# Update with another dict (overwrites existing keys)
person.update({"age": 31, "salary": 55000})
print(f"After update (overwrites): {person}")


# === VALUES() ===
print("\n=== DICTIONARY VALUES() ===")
person = {"name": "Alice", "age": 30, "city": "New York"}
values = person.values()
print(f"person.values(): {values}")
print(f"type(values): {type(values)}")

# Convert to list
values_list = list(values)
print(f"list(person.values()): {values_list}")

# Iterate over values
print("Iterating over values:")
for value in person.values():
    print(f"  {value}")

# Values view is dynamic
person["email"] = "alice@example.com"
print(f"After adding email, values view: {values}")  # Automatically updated


# === COMPARISON: GET() VS [] ACCESS ===
print("\n=== GET() VS [] ACCESS COMPARISON ===")
person = {"name": "Alice", "age": 30}

# Existing key (both work)
print(f"person['name']: {person['name']}")
print(f"person.get('name'): {person.get('name')}")

# Non-existing key
# print(person["email"])  # KeyError: 'email'
print(f"person.get('email'): {person.get('email')}")  # Returns None
print(f"person.get('email', 'N/A'): {person.get('email', 'N/A')}")  # Returns default

# Performance: [] is slightly faster for existing keys
# but get() is safer and avoids exceptions


# === COMPARISON: POP() VS DEL ===
print("\n=== POP() VS DEL COMPARISON ===")
person = {"name": "Alice", "age": 30, "city": "New York"}

# del statement
del person["age"]
print(f"After del person['age']: {person}")

# pop() method
person = {"name": "Alice", "age": 30, "city": "New York"}
age = person.pop("age")
print(f"Popped value: {age}")
print(f"After pop: {person}")

# Key differences:
# - del is a statement, pop() is a method
# - pop() returns the value, del doesn't
# - pop() can provide default value, del raises KeyError


# === PRACTICAL EXAMPLES ===

# 1. Merging dictionaries
print("\n=== PRACTICAL: MERGING DICTIONARIES ===")
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = dict1.copy()
merged.update(dict2)
print(f"Merged dict: {merged}")

# 2. Dictionary as cache with setdefault()
print("\n=== PRACTICAL: CACHE WITH SETDEFAULT() ===")
cache = {}

def get_data(key):
    return cache.setdefault(key, f"computed-{key}")

print(f"Data for 'item1': {get_data('item1')}")
print(f"Data for 'item2': {get_data('item2')}")
print(f"Data for 'item1' again: {get_data('item1')}")  # Returns cached value
print(f"Cache: {cache}")

# 3. Safe nested dictionary access
print("\n=== PRACTICAL: SAFE NESTED ACCESS ===")
data = {"user": {"profile": {"name": "Alice"}}}

# Unsafe access
# city = data["company"]["address"]["city"]  # KeyError

# Safe access with get()
city = data.get("company", {}).get("address", {}).get("city", "Unknown")
print(f"City: {city}")

# 4. Pop all items
print("\n=== PRACTICAL: POP ALL ITEMS ===")
person = {"name": "Alice", "age": 30, "city": "New York"}
print(f"Original: {person}")

while person:
    key, value = person.popitem()
    print(f"Removed: {key} = {value}")
    print(f"Remaining: {person}")

print(f"Empty after popping all: {person}")


# 5. Update with conditional logic
print("\n=== PRACTICAL: CONDITIONAL UPDATE ===")
config = {"debug": False, "verbose": False}
new_settings = {"debug": True, "log_level": "INFO"}

# Update only if debug is being enabled
if new_settings.get("debug", False):
    config.update(new_settings)
    print(f"Config updated: {config}")
else:
    print(f"Debug not enabled, config unchanged: {config}")


# 6. Dictionary with default values for missing keys
print("\n=== PRACTICAL: DEFAULT VALUES PATTERN ===")
class DefaultDict:
    def __init__(self, default_factory):
        self.default_factory = default_factory
        self.data = {}
    
    def __getitem__(self, key):
        if key not in self.data:
            self.data[key] = self.default_factory()
        return self.data[key]

# Usage
dd = DefaultDict(list)
dd["fruits"].append("apple")
dd["fruits"].append("banana")
dd["veggies"].append("carrot")
print(f"DefaultDict result: {dd.data}")


# === PERFORMANCE CHARACTERISTICS ===
print("\n=== PERFORMANCE CHARACTERISTICS ===")
print("get(): O(1) average case")
print("setdefault(): O(1) average case")
print("pop(): O(1) average case")
print("popitem(): O(1) average case")
print("update(): O(k) where k is number of items being added")
print("keys/values/items(): O(1) to create view")
print("clear(): O(n) where n is number of items")


# === METHOD SUMMARY ===
print("\n=== METHOD SUMMARY ===")
print("Dictionary methods:")
print("  - clear(): Remove all items")
print("  - copy(): Shallow copy of dict")
print("  - fromkeys(): Create dict with default values")
print("  - get(): Get value with optional default")
print("  - items(): Return key-value pairs view")
print("  - keys(): Return keys view")
print("  - pop(): Remove and return value")
print("  - popitem(): Remove and return last item")
print("  - setdefault(): Get or set value")
print("  - update(): Update with key-value pairs")
print("  - values(): Return values view")
