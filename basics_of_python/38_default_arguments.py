# Python Default Arguments - Safe Usage and Mutable Default Trap

print("=== BASIC DEFAULT ARGUMENTS (SAFE) ===")

def greet(name, greeting="Hello", punctuation="!"):
    """Greet someone with optional greeting and punctuation."""
    print(f"{greeting}, {name}{punctuation}")

greet("Alice")                          # Uses both defaults
greet("Bob", "Hi")                      # Override greeting only
greet("Charlie", punctuation="...")     # Override punctuation only
greet("Diana", greeting="Welcome", punctuation=".")  # Override both


print("\n=== EVALUATION TIME OF DEFAULTS ===")

DEFAULT_GREETING = "Hello"

def show_default(name, greeting=DEFAULT_GREETING):
    """Default evaluated at function definition time, not call time.[web:81][web:87]"""
    print(f"{greeting}, {name}")

show_default("Eve")

# Change global DEFAULT_GREETING after definition
DEFAULT_GREETING = "Hi"
# Default inside function does NOT change automatically
show_default("Frank")  # Still uses "Hello"


print("\n=== MUTABLE DEFAULT ARGUMENT TRAP (LIST) ===")

def append_to_list(item, lst=[]):
    """
    DEMO ONLY: This is the classic mutable default trap.[web:75][web:78][web:81][web:84][web:87]
    lst is created ONCE at function definition and reused across calls.
    """
    lst.append(item)
    return lst

print("First call:", append_to_list("a"))       # ['a']
print("Second call:", append_to_list("b"))      # ['a', 'b'] (unexpected for many)
print("Third call:", append_to_list("c"))       # ['a', 'b', 'c']

# All calls without explicit lst shared the same list.


print("\n=== CORRECT PATTERN FOR MUTABLE DEFAULTS (LIST) ===")

def append_to_list_safe(item, lst=None):
    """
    Use None as default, then create new list inside when needed.[web:75][web:78][web:81][web:84]
    This avoids sharing state across calls.
    """
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print("Safe first call:", append_to_list_safe("a"))         # ['a']
print("Safe second call:", append_to_list_safe("b"))        # ['b']
print("Safe with provided list:", append_to_list_safe("c", ["x", "y"]))  # ['x', 'y', 'c']


print("\n=== MUTABLE DEFAULT ARGUMENT TRAP (DICT) ===")

def add_to_mapping(key, value, mapping={}):
    """
    DEMO ONLY: Mutable default dict with same issue as list.
    """
    mapping[key] = value
    return mapping

print("Mapping call 1:", add_to_mapping("a", 1))   # {'a': 1}
print("Mapping call 2:", add_to_mapping("b", 2))   # {'a': 1, 'b': 2} (shared)
print("Mapping call 3:", add_to_mapping("c", 3))   # {'a': 1, 'b': 2, 'c': 3}


print("\n=== CORRECT PATTERN FOR DICT DEFAULTS ===")

def add_to_mapping_safe(key, value, mapping=None):
    """Use None and create new dict as needed."""
    if mapping is None:
        mapping = {}
    mapping[key] = value
    return mapping

print("Safe mapping 1:", add_to_mapping_safe("a", 1))                   # {'a': 1}
print("Safe mapping 2:", add_to_mapping_safe("b", 2))                   # {'b': 2}
print("Safe mapping 3:", add_to_mapping_safe("c", 3, {"x": 9}))         # {'x': 9, 'c': 3}


print("\n=== DEFAULTS WITH IMMUTABLE TYPES (USUALLY SAFE) ===")

def increment(x, step=1):
    """Increment x by step (int default is immutable, so safe)."""
    return x + step

print("increment(10):", increment(10))          # 11
print("increment(10, 5):", increment(10, 5))    # 15

def tag_message(msg, prefix="[INFO] ", suffix=""):
    """Tag message with prefix/suffix (string defaults are immutable)."""
    return f"{prefix}{msg}{suffix}"

print(tag_message("System started"))
print(tag_message("Warning", prefix="[WARN] ", suffix=" !!!"))


print("\n=== SNAPSHOT OF COMPLEX DEFAULTS ===")

import datetime

def log_message(message, timestamp=datetime.datetime.now()):
    """
    DEMO ONLY: timestamp default is evaluated once at definition time.
    All calls without explicit timestamp use the same datetime value.
    """
    print(f"[{timestamp}] {message}")

log_message("First log")
log_message("Second log (same default timestamp)")

# Correct pattern:

def log_message_safe(message, timestamp=None):
    """Compute timestamp at call time if not provided."""
    if timestamp is None:
        timestamp = datetime.datetime.now()
    print(f"[{timestamp}] {message}")

log_message_safe("First safe log")
log_message_safe("Second safe log")


print("\n=== SUMMARY ===")
print("1) Default arguments are evaluated once at function definition time.")
print("2) Using mutable objects (list, dict, set, etc.) as defaults can cause shared state bugs.")
print("3) Preferred pattern: use None as default, create new object inside function when needed.")
