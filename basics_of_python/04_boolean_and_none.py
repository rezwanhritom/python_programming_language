# Python Boolean and None Types - Complete Reference

# === BOOLEAN VALUES ===
# True and False are the two boolean values
is_active = True
is_closed = False
print(f"Boolean True: {is_active}, Boolean False: {is_closed}")

# === BOOLEAN FROM COMPARISONS ===
result1 = 5 > 3
result2 = 10 == 20
result3 = "a" != "b"
print(f"5 > 3: {result1}")
print(f"10 == 20: {result2}")
print(f"'a' != 'b': {result3}")

# === TRUTHY AND FALSY VALUES ===
# Values that evaluate to False in boolean context
falsy_values = [
    False,      # Boolean False
    0,          # Zero integer
    0.0,        # Zero float
    "",         # Empty string
    [],         # Empty list
    (),         # Empty tuple
    {},         # Empty dictionary
    set(),      # Empty set
    None        # None type
]

print("\n=== FALSY VALUES ===")
for value in falsy_values:
    print(f"{value} -> bool({value}) = {bool(value)}")

# Truthy values (everything else)
truthy_values = [
    True,
    42,
    -1,
    "hello",
    [1],
    (1,),
    {"key": "value"},
    {1}
]

print("\n=== TRUTHY VALUES ===")
for value in truthy_values:
    print(f"{value} -> bool({value}) = {bool(value)}")

# === BOOLEAN OPERATIONS ===
# AND operation: Returns first falsy value or last truthy value
print(f"\nTrue and True: {True and True}")
print(f"True and False: {True and False}")
print(f"False and True: {False and True}")
print(f"False and False: {False and False}")

# OR operation: Returns first truthy value or last falsy value
print(f"\nTrue or True: {True or True}")
print(f"True or False: {True or False}")
print(f"False or True: {False or True}")
print(f"False or False: {False or False}")

# NOT operation: Inverts boolean
print(f"\nnot True: {not True}")
print(f"not False: {not False}")

# === NONE TYPE ===
# None represents absence of a value
empty_value = None
print(f"\nNone value: {empty_value}")
print(f"Type of None: {type(empty_value)}")
print(f"None is False: {bool(None)}")

# === IS NONE CHECKING ===
def might_return_none(flag):
    if flag:
        return "Value"
    return None

result1 = might_return_none(True)
result2 = might_return_none(False)

print(f"\nResult1 is None: {result1 is None}")
print(f"Result2 is None: {result2 is None}")
print(f"Result1 is not None: {result1 is not None}")
