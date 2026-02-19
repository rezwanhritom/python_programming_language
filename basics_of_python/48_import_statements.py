# Python Import Statements - import, from ... import, aliases, __name__ == "__main__"

print("=== BASIC import MODULE ===")
# import <module>
# Access names as module.name

import math  # Standard library math module

print("math.pi:", math.pi)
print("math.sqrt(16):", math.sqrt(16))


print("\n=== from MODULE import NAME ===")
# from <module> import <name1>, <name2>, ...

from math import sqrt, pi

print("sqrt(25):", sqrt(25))  # Directly available
print("pi:", pi)

# Note: 'from math import *' is allowed but discouraged in real code
# because it pollutes the namespace and can cause name conflicts.[web:108]


print("\n=== USING ALIASES WITH as ===")
# import <module> as <alias>
# from <module> import <name> as <alias>

import math as m
from datetime import datetime as dt

print("m.sin(m.pi / 2):", m.sin(m.pi / 2))
print("Current year via dt:", dt.now().year)


print("\n=== IMPORTING ONLY WHEN NEEDED (INSIDE FUNCTIONS) ===")

def compute_stats(numbers):
    """
    Importing inside a function is sometimes used to avoid heavy imports
    at module load time, or to break circular imports.
    """
    import statistics  # Local import
    mean = statistics.mean(numbers)
    median = statistics.median(numbers)
    return mean, median

print("compute_stats([1, 2, 3, 4]):", compute_stats([1, 2, 3, 4]))


print("\n=== IMPORTING FROM YOUR OWN MODULES ===")
# Suppose you have:
#   utils.py   with function: def greet(name): ...
#
# Then in this file you can:
#   import utils
#   from utils import greet
#
# For demonstration we define a dummy function instead of real import.

def dummy_greet(name):
    print(f"Hello from dummy_greet, {name}!")


print("\n=== __name__ AND if __name__ == \"__main__\" ===")
# Every module has a built-in variable __name__.[web:107][web:110][web:113][web:116]
# - When run as a script: __name__ == "__main__"
# - When imported:        __name__ == module's name (e.g., 'mymodule')

print("In this module, __name__ is:", __name__)

def main():
    """Main entry point when this file is executed as a script."""
    print("Running main() in 48_import_statements.py")
    dummy_greet("Alice")
    print("Done.")

# This guard ensures main() runs only when the file is executed directly,
# not when imported as a module.[web:107][web:110]
if __name__ == "__main__":
    main()
