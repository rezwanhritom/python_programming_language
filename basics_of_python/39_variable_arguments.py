# Python *args - Variable Positional Arguments

print("=== BASIC *args USAGE ===")

def print_numbers(*args):
    """
    *args collects any number of positional arguments into a tuple.[web:76][web:79][web:82][web:88]
    """
    print("args:", args, "| type:", type(args))

print_numbers()                 # ()
print_numbers(1)                # (1,)
print_numbers(1, 2, 3, 4, 5)    # (1, 2, 3, 4, 5)


print("\n=== MIXING REGULAR PARAMETERS WITH *args ===")

def log(message, *values):
    """
    First parameter is regular, remaining positional arguments go into *values.
    """
    print("Message:", message)
    print("Values:", values)

log("No extra values")
log("One value", 42)
log("Many values", 1, 2, 3, "x")


print("\n=== ITERATING OVER *args ===")

def add_all(*numbers):
    """Return sum of all positional arguments."""
    total = 0
    for n in numbers:
        total += n
    return total

print("add_all():", add_all())
print("add_all(1, 2, 3):", add_all(1, 2, 3))
print("add_all(5, 10, 15, 20):", add_all(5, 10, 15, 20))


print("\n=== UNPACKING SEQUENCES INTO *args ===")

def show_three(a, b, c):
    """Show three values."""
    print(f"a={a}, b={b}, c={c}")

triple = (1, 2, 3)
show_three(*triple)  # Unpacks tuple into a, b, c

triple_list = [4, 5, 6]
show_three(*triple_list)  # Unpacks list

# Using * to merge iterables
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
merged = [*nums1, *nums2]
print("Merged list via * unpacking:", merged)


print("\n=== ORDER OF PARAMETERS WITH *args ===")

def demo_order(a, b, *args):
    """
    Order: regular parameters first, then *args.[web:76][web:79]
    a, b are required positional parameters, extra go into args.
    """
    print(f"a={a}, b={b}, args={args}")

demo_order(1, 2)
demo_order(1, 2, 3, 4, 5)

# INVALID: *args must appear after regular positional params
# def bad(*args, a):  # SyntaxError in most cases (except keyword-only designs)
#     pass


print("\n=== COMBINING *args WITH KEYWORD-ONLY PARAMS ===")

def report(title, *items, footer="END"):
    """
    title: regular param
    *items: variable number of items
    footer: keyword-only because it comes after *items
    """
    print("Title:", title)
    print("Items:", items)
    print("Footer:", footer)

report("Shopping List", "apples", "bananas", "milk")
report("Scores", 10, 20, 30, footer="DONE")


print("\n=== FORWARDING *args TO ANOTHER FUNCTION ===")

def base_sum(*numbers):
    """Sum of numbers."""
    return sum(numbers)

def add_with_offset(offset, *numbers):
    """Add offset to the sum of all other positional arguments."""
    base = base_sum(*numbers)  # Forward args
    return offset + base

print("add_with_offset(10, 1, 2, 3):", add_with_offset(10, 1, 2, 3))


print("\n=== USING * TO EXPAND ITERABLES IN CALLS ===")

def multiply(a, b, c):
    return a * b * c

values = (2, 3, 4)
print("multiply(*values):", multiply(*values))  # multiply(2, 3, 4)

# Mix unpacked and regular arguments
print("multiply(2, *[3, 4]):", multiply(2, *[3, 4]))


print("\n=== *args IN REALISTIC EXAMPLE ===")

def debug_print(prefix, *values):
    """
    Print values with a prefix, using variable number of positional args.
    """
    print(prefix, end=" ")
    for v in values:
        print(repr(v), end=" ")
    print()

debug_print("[DEBUG]", 1, 2, 3)
debug_print("[STATE]", {"x": 10}, [1, 2, 3], "ok")


print("\n=== SUMMARY ===")
print("*args gathers extra positional arguments into a tuple.")
print("Place *args after all required positional parameters.")
print("Use * to unpack sequences when calling functions.")
