# Python Type Conversion - int, float, str, bool, list, tuple, set, dict

print("=== int() CONVERSION ===")
# int() converts numbers or numeric strings to integer

print(int(3.9))             # 3 (truncates toward 0)
print(int(-2.7))            # -2
print(int("42"))            # 42
print(int("  10  "))        # 10 (whitespace ok)

# int() with base (string only)
print(int("1010", 2))       # 10 (binary)
print(int("FF", 16))        # 255 (hex)

# Invalid conversions raise ValueError
# int("3.14")    # ValueError
# int("hello")   # ValueError


print("\n=== float() CONVERSION ===")
# float() converts integers or numeric strings to float

print(float(10))            # 10.0
print(float("3.14"))        # 3.14
print(float("  2.5  "))     # 2.5

# Special float strings
print(float("inf"))         # Infinity
print(float("-inf"))        # Negative infinity
print(float("nan"))         # Not-a-Number (NaN)

# Invalid conversions raise ValueError
# float("abc")  # ValueError


print("\n=== str() CONVERSION ===")
# str() converts almost any object to its string representation

print(str(42))              # "42"
print(str(3.14))            # "3.14"
print(str(True))            # "True"
print(str(None))            # "None"
print(str([1, 2, 3]))       # "[1, 2, 3]"
print(str({"a": 1, "b": 2}))  # "{'a': 1, 'b': 2}"


print("\n=== bool() CONVERSION ===")
# bool() converts a value to True or False
# Falsy values: False, 0, 0.0, "", [], (), {}, set(), None

values = [False, 0, 0.0, "", [], (), {}, set(), None, 1, "0", "False", [0], (0,), {"x": 0}]
for v in values:
    print(f"value={repr(v):>10}, bool(value)={bool(v)}")

# Note: any non-empty string is True, even "0" or "False"


print("\n=== list() CONVERSION ===")
# list() converts an iterable to a list

print(list("hello"))        # ['h', 'e', 'l', 'l', 'o']
print(list((1, 2, 3)))      # [1, 2, 3] from tuple
print(list({1, 2, 3}))      # [1, 2, 3] from set (order arbitrary)
print(list(range(5)))       # [0, 1, 2, 3, 4]

# From dictionary: list of keys
d = {"a": 1, "b": 2}
print(list(d))              # ['a', 'b']
print(list(d.keys()))       # ['a', 'b']
print(list(d.values()))     # [1, 2]


print("\n=== tuple() CONVERSION ===")
# tuple() converts an iterable to a tuple

print(tuple("abc"))         # ('a', 'b', 'c')
print(tuple([1, 2, 3]))     # (1, 2, 3)
print(tuple({1, 2, 3}))     # (1, 2, 3) from set (order arbitrary)

# From dictionary: tuple of keys
print(tuple(d))             # ('a', 'b')


print("\n=== set() CONVERSION ===")
# set() converts an iterable to a set (unique elements)

print(set("banana"))        # {'b', 'a', 'n'} (order arbitrary)
print(set([1, 2, 2, 3, 3])) # {1, 2, 3}

# From tuple
print(set((1, 2, 3, 3)))    # {1, 2, 3}

# From dict: set of keys
print(set(d))               # {'a', 'b'}
print(set(d.keys()))        # {'a', 'b'}
print(set(d.values()))      # {1, 2}


print("\n=== dict() CONVERSION ===")
# dict() converts key-value pairs to a dictionary

# From list of pairs
pairs_list = [("a", 1), ("b", 2), ("c", 3)]
print(dict(pairs_list))     # {'a': 1, 'b': 2, 'c': 3}

# From tuple of pairs
pairs_tuple = (("x", 10), ("y", 20))
print(dict(pairs_tuple))    # {'x': 10, 'y': 20}

# From list of 2-char strings (not recommended, but works)
pairs_str = ["ab", "cd"]    # 'a'->'b', 'c'->'d'
print(dict(pairs_str))      # {'a': 'b', 'c': 'd'}

# From zip of keys and values
keys = ["name", "age"]
values = ["Alice", 30]
print(dict(zip(keys, values)))  # {'name': 'Alice', 'age': 30}

# From existing dict (copy)
original = {"k1": "v1", "k2": "v2"}
copy_dict = dict(original)
print(copy_dict)


print("\n=== COMBINED CONVERSION EXAMPLES ===")
# String to list/tuple/set
s = "hello"
print(f"String: {s}")
print(f"list(s):  {list(s)}")   # ['h', 'e', 'l', 'l', 'o']
print(f"tuple(s): {tuple(s)}")  # ('h', 'e', 'l', 'l', 'o')
print(f"set(s):   {set(s)}")    # {'h', 'e', 'l', 'o'}

# List of pairs to dict, then back to list of items
pairs = [("a", 1), ("b", 2), ("c", 3)]
d = dict(pairs)
print(f"\nPairs: {pairs}")
print(f"Dict:  {d}")
print(f"Items as list: {list(d.items())}")

# Numeric string to int then to float
num_str = "42"
n_int = int(num_str)
n_float = float(num_str)
print(f"\nnum_str: {num_str}, int: {n_int}, float: {n_float}")

# Bool conversions in practice
user_input = "False"
print(f"\nuser_input: {user_input}, bool(user_input): {bool(user_input)}  # non-empty string is True")

# Safer explicit check
print(f"user_input.lower() == 'true': {user_input.lower() == 'true'}")


print("\n=== TYPE AND VALUE CHECKS ===")
values = [42, 3.14, "hello", True, [1, 2], (1, 2), {1, 2}, {"a": 1}]
for v in values:
    print(f"value={repr(v):>10}, type={type(v)}")

