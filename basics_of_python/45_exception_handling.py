# Python Exception Handling - try, except, else, finally

print("=== BASIC try / except ===")

def divide(a, b):
    """Safely divide a by b with basic exception handling."""
    try:
        result = a / b
        print(f"{a} / {b} = {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

divide(10, 2)
divide(10, 0)


print("\n=== CATCHING MULTIPLE EXCEPTION TYPES ===")

def safe_int_division(a, b):
    """Convert to int and divide, catching ValueError and ZeroDivisionError."""
    try:
        x = int(a)
        y = int(b)
        result = x // y
        print(f"{x} // {y} = {result}")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except ValueError:
        print("Error: Invalid integer value.")
    except Exception as e:
        # Catch-all for unexpected exceptions (use sparingly)
        print(f"Unexpected error: {e}")

safe_int_division("10", "2")
safe_int_division("10", "0")
safe_int_division("ten", "2")


print("\n=== USING else WITH try/except ===")
# else runs ONLY if no exception was raised in the try block.[web:101]

def read_number_and_divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Division by zero.")
    else:
        # Only runs when try succeeds without exceptions
        print(f"Result is {result}, computation succeeded.")

read_number_and_divide(10, 2)
read_number_and_divide(10, 0)


print("\n=== USING finally (ALWAYS RUNS) ===")
# finally runs whether or not an exception occurs (even if there is return).[web:95][web:98][web:101]

def open_and_close_dummy():
    print("Entering function")
    try:
        print("In try block")
        return "return from try"
    except Exception:
        print("In except block")
    finally:
        print("In finally block (always runs)")

result = open_and_close_dummy()
print("Function result:", result)


print("\n=== CLEANUP WITH finally (FILES, CONNECTIONS, ETC.) ===")

def read_file_manual(path):
    """Manual open/close using try/finally (for illustration)."""
    f = None
    try:
        f = open(path, "r", encoding="utf-8")
        data = f.read()
        print("File contents (truncated to 60 chars):")
        print(data[:60])
    except FileNotFoundError:
        print(f"File not found: {path}")
    finally:
        if f is not None:
            print("Closing file")
            f.close()

# Uncomment to test with a real file:
# read_file_manual("example.txt")


print("\n=== NESTED try/except AND RE-RAISING ===")

def parse_and_divide(a, b):
    try:
        try:
            x = int(a)
            y = int(b)
        except ValueError as e:
            print("Inner: could not convert to int, re-raising.")
            raise  # re-raise the same exception
        result = x / y
    except ZeroDivisionError:
        print("Outer: division by zero.")
    except ValueError:
        print("Outer: caught ValueError from inner block.")

parse_and_divide("10", "2")
parse_and_divide("ten", "2")
parse_and_divide("10", "0")


print("\n=== CUSTOM EXCEPTIONS (BASIC) ===")

class NegativeNumberError(Exception):
    """Custom exception for negative numbers."""
    pass

def sqrt_non_negative(x):
    if x < 0:
        raise NegativeNumberError(f"Cannot take sqrt of negative: {x}")
    import math
    return math.sqrt(x)

for val in [4, 0, -1]:
    try:
        print(f"sqrt_non_negative({val}) = {sqrt_non_negative(val)}")
    except NegativeNumberError as e:
        print("Caught NegativeNumberError:", e)


print("\n=== SUMMARY ===")
print("Key blocks:")
print("  - try: code that may raise exceptions")
print("  - except: handle specific exceptions")
print("  - else: runs only if no exception occurred in try")
print("  - finally: always runs (cleanup), regardless of exceptions")
