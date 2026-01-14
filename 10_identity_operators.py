# Python Identity Operators - Complete Reference
# Identity operators compare OBJECTS, not just values.

# Two identity operators:
#   is      -> True if both variables refer to the SAME object in memory
#   is not  -> True if they refer to DIFFERENT objects in memory


print("=== BASIC IDENTITY CHECKS WITH LISTS ===")

x = [1, 2, 3]
y = [1, 2, 3]
z = x  # z references the same list object as x

print(f"x: {x}, id(x): {id(x)}")
print(f"y: {y}, id(y): {id(y)}")
print(f"z: {z}, id(z): {id(z)}")

# == checks value equality
print(f"\nx == y: {x == y}")       # True: contents are equal
# is checks identity (same object)
print(f"x is y: {x is y}")         # False: different list objects
print(f"x is z: {x is z}")         # True: z points to x's object

# is not is the opposite of is
print(f"x is not y: {x is not y}") # True: different objects
print(f"x is not z: {x is not z}") # False: same object


print("\n=== IDENTITY WITH IMMUTABLE TYPES (INT, STR) ===")
# Small integers and some strings may be cached by Python (implementation detail),
# so sometimes is can appear to behave like ==, but you must NOT rely on this.

a = 5
b = 5
c = 1000
d = 1000

print(f"a = {a}, b = {b}, id(a)={id(a)}, id(b)={id(b)}")
print(f"a == b: {a == b}")
print(f"a is b: {a is b}   # May be True due to interning")

print(f"\nc = {c}, d = {d}, id(c)={id(c)}, id(d)={id(d)}")
print(f"c == d: {c == d}")
print(f"c is d: {c is d}   # Often False, but DO NOT depend on identity of ints")

s1 = "hello world"
s2 = "hello world"
print(f"\ns1 == s2: {s1 == s2}")
print(f"s1 is s2: {s1 is s2}   # May be True or False depending on interning")


print("\n=== IDENTITY VS EQUALITY ===")

# Equality compares values
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(f"list1 == list2: {list1 == list2}")  # True (same contents)
print(f"list1 is list2: {list1 is list2}")  # False (different objects)

# Change list1 and see list2 unaffected
list1.append(4)
print(f"\nAfter list1.append(4):")
print(f"list1: {list1}")
print(f"list2: {list2}")
print(f"list1 == list2: {list1 == list2}")
print(f"list1 is list2: {list1 is list2}")


print("\n=== SHARED REFERENCES AND MUTABILITY ===")
# Demonstrate how identity matters for mutable objects

original = [10, 20, 30]
alias = original          # alias is just another reference to the same list
copy_list = original[:]   # shallow copy (new list object with same elements)

print(f"original id: {id(original)}")
print(f"alias id:    {id(alias)}")
print(f"copy id:     {id(copy_list)}")

print(f"\noriginal is alias: {original is alias}")        # True
print(f"original is copy_list: {original is copy_list}") # False
print(f"original == copy_list: {original == copy_list}") # True (same contents)

# Modifying through alias affects original
alias.append(40)
print(f"\nAfter alias.append(40):")
print(f"original: {original}")
print(f"alias:    {alias}")
print(f"copy_list: {copy_list}")


print("\n=== IDENTITY WITH NONE ===")
# The recommended way to check for None is using 'is' and 'is not'.

value = None

if value is None:
    print("value is None (using 'is')")

if value is not None:
    print("value is not None")  # This will not print here

# Bad style: using == or != for None checks
print(f"\nvalue == None: {value == None}   # Works but not recommended")
print(f"value is None: {value is None}   # Preferred")


print("\n=== PRACTICAL USE CASES ===")

# 1. Singleton checks (e.g., None, sentinel objects)
sentinel = object()  # unique sentinel object

def fetch_value(flag):
    if flag:
        return 42
    return sentinel

result1 = fetch_value(True)
result2 = fetch_value(False)

print(f"\nresult1 is sentinel: {result1 is sentinel}")
print(f"result2 is sentinel: {result2 is sentinel}")

# 2. Distinguishing between two empty containers
empty_list1 = []
empty_list2 = []
print(f"\nempty_list1 == empty_list2: {empty_list1 == empty_list2}")  # True
print(f"empty_list1 is empty_list2: {empty_list1 is empty_list2}")    # False

same_ref = empty_list1
print(f"empty_list1 is same_ref: {empty_list1 is same_ref}")          # True


print("\n=== SUMMARY NOTE (IN COMMENTS) ===")
# Use '==' when you care if two values are equal.
# Use 'is' when you care if two variables point to the exact same object
# (especially for None and sentinel objects).
