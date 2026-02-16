# Python Function Parameters - Positional and Keyword Arguments

print("=== POSITIONAL PARAMETERS AND ARGUMENTS ===")

def full_name(first_name, last_name):
    """Return full name from first and last name (positional parameters)."""
    return f"{first_name} {last_name}"

# Positional arguments: order matters
print(full_name("Alice", "Smith"))   # Alice Smith
print(full_name("Smith", "Alice"))   # Smith Alice (different result!)

# If you swap the order of positional arguments, meaning changes.[web:74][web:83]


print("\n=== KEYWORD ARGUMENTS ===")

def introduce(name, age, city):
    """Introduce a person with name, age, and city."""
    print(f"{name} is {age} years old and lives in {city}.")

# Positional call
introduce("Bob", 25, "London")

# Keyword arguments: order does NOT matter, names do
introduce(age=30, name="Charlie", city="Berlin")
introduce(city="Paris", name="Diana", age=22)  # order changed

# Mixing positional + keyword: positional MUST come first.[web:74][web:83][web:86]
introduce("Eve", age=29, city="Rome")

# INVALID (keyword before positional) -> SyntaxError:
# introduce(age=29, "Eve", city="Rome")  # ❌ not allowed


print("\n=== DEFAULT VALUES WITH POSITIONAL AND KEYWORD CALLS ===")

def power(base, exponent=2):
    """Raise base to exponent, default exponent=2."""
    return base ** exponent

# Positional: second argument uses default
print("power(3) =", power(3))            # uses exponent=2

# Positional for both
print("power(3, 3) =", power(3, 3))

# Keyword for defaulted parameter
print("power(base=4, exponent=3) =", power(base=4, exponent=3))

# Mixed: positional for base, keyword for exponent
print("power(2, exponent=5) =", power(2, exponent=5))


print("\n=== ENFORCING KEYWORD-ONLY PARAMETERS ( * ) ===")

def connect(host, port, *, use_ssl=False, timeout=30):
    """
    Demonstrate keyword-only parameters.

    Anything after * must be passed as keyword argument in Python 3.[web:77][web:80]
    """
    print(f"Connecting to {host}:{port}, use_ssl={use_ssl}, timeout={timeout}")

# Valid: positional for host, port; keyword for the rest
connect("localhost", 8080, use_ssl=True, timeout=10)
connect("example.com", 80)  # uses defaults use_ssl=False, timeout=30

# INVALID: trying to pass keyword-only as positional
# connect("localhost", 8080, True, 10)  # TypeError


print("\n=== ENFORCING POSITIONAL-ONLY PARAMETERS ( / ) ===")

def ratio(numerator, denominator, /, scale=1):
    """
    Demonstrate positional-only parameters (Python 3.8+).
    Parameters before / must be passed positionally.[web:77][web:80]
    """
    return (numerator / denominator) * scale

# Valid: positional for numerator, denominator; keyword or positional for scale
print("ratio(10, 2):", ratio(10, 2))
print("ratio(10, 2, scale=0.5):", ratio(10, 2, scale=0.5))

# INVALID: cannot pass positional-only parameters by keyword
# ratio(numerator=10, denominator=2)  # TypeError


print("\n=== SUMMARY EXAMPLE: MIXED PARAMETERS ===")

def summary(a, b, /, c, d=0, *, e=0, f=0):
    """
    a, b: positional-only
    c, d: can be positional or keyword
    e, f: keyword-only
    """
    print(f"a={a}, b={b}, c={c}, d={d}, e={e}, f={f}")

# Valid usage:
summary(1, 2, 3)                 # c=3, d=0, e=0, f=0
summary(1, 2, 3, 4, e=5, f=6)    # all specified
summary(1, 2, c=3, e=9)          # c by keyword, d default

# INVALID (a, b must be positional)
# summary(a=1, b=2, c=3)  # TypeError

# INVALID (e, f must be keyword-only)
# summary(1, 2, 3, 4, 5, 6)  # TypeError
