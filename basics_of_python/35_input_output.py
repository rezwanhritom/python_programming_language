# Python Input and Output - input(), print(), sep, end

# NOTE:
# - input() ALWAYS returns a string in Python 3, even if you type a number.[web:61][web:70][web:73]
# - You must convert it manually with int(), float(), etc. when needed.


print("=== BASIC input() USAGE ===")
# Single input value
# Uncomment to try interactively:
# name = input("Enter your name: ")
# print(f"Hello, {name}!")


print("\n=== input() ALWAYS RETURNS STRING ===")
# Demonstration (this will pause waiting for input when run)
# Uncomment when you want to test.

# age = input("How old are you? ")
# print("You typed:", age)
# print("Type of age:", type(age))  # <class 'str'>

# To get a number, convert explicitly:
# age_int = int(age)  # Will raise ValueError if input is not a valid integer string
# print("As integer + 1:", age_int + 1)


print("\n=== SAFE NUMERIC INPUT WITH CONVERSION ===")
# Example pattern: keep asking until valid integer is entered

# Uncomment to test:
# while True:
#     user_input = input("Enter an integer: ")
#     try:
#         number = int(user_input)
#         print("You entered integer:", number)
#         break
#     except ValueError:
#         print("That was not a valid integer. Try again.")


print("\n=== MULTIPLE INPUT VALUES ===")
# Read two numbers and add them

# Uncomment to test:
# a_str = input("Enter first number: ")
# b_str = input("Enter second number: ")
# a = float(a_str)
# b = float(b_str)
# print(f"{a} + {b} = {a + b}")


print("\n=== BASIC print() USAGE ===")
# print() can take multiple arguments; they are separated by sep (default: space).[web:59][web:68]
print("Hello", "World")          # Hello World
print("A", "B", "C")            # A B C

# print() automatically ends with a newline by default (end = "\n").[web:68]


print("\n=== print() WITH sep PARAMETER ===")
# sep controls the separator between multiple arguments.[web:59][web:62][web:65][web:71]

print("Using default sep (space):")
print("apple", "banana", "cherry")  # apple banana cherry

print("\nUsing custom sep=',':")
print("apple", "banana", "cherry", sep=",")  # apple,banana,cherry

print("\nUsing custom sep=' - ':")
print("apple", "banana", "cherry", sep=" - ")  # apple - banana - cherry

print("\nUsing empty sep (no separator):")
print("A", "B", "C", sep="")  # ABC


print("\n=== print() WITH end PARAMETER ===")
# end controls what is printed at the end; default is '\n'.[web:59][web:62][web:68]

print("Default end:")
print("Line 1")
print("Line 2")   # Line 1\nLine 2\n

print("\nCustom end=' ' (space):")
for i in range(1, 6):
    print(i, end=" ")  # numbers on one line separated by space
print()  # print final newline

print("\nCustom end='...\\n':")
print("Processing", end="...")
print("done")  # Output: Processing...done


print("\n=== COMBINING sep AND end ===")
# You can use sep and end together for fine-grained control.[web:62][web:68][web:71]

print("Numbers with comma and custom ending:")
print(1, 2, 3, 4, 5, sep=", ", end=" <-- end of list\n")

print("\nWords joined with ' | ' and no newline at end:")
print("alpha", "beta", "gamma", sep=" | ", end="")
print(" <- continues on same line")


print("\n=== PRINTING WITHOUT NEWLINE (END='') ===")
# Use end='' to avoid newline
print("First part", end="")
print(" and second part on same line")

print("\nUse loops with end to control layout:")
for i in range(3):
    print("Loop", i, end="; ")
print()  # newline


print("\n=== ESCAPE SEQUENCES IN STRINGS ===")
# Common escapes: \n (newline), \t (tab), \\ (backslash), \' and \" for quotes
print("Line1\nLine2")
print("Column1\tColumn2")
print("C:\\Users\\Name")


print("\n=== FORMATTED OUTPUT WITH f-STRINGS AND format() ===")
name = "Alice"
score = 95.5

# f-string (recommended in modern Python)[web:48]
print(f"Student {name} scored {score:.1f} points.")

# str.format()
print("Student {} scored {:.1f} points.".format(name, score))


print("\n=== SIMPLE ECHO PROGRAM (input + print) ===")
# Uncomment this block to test a simple echo.

# user_text = input("Type something and press Enter: ")
# print("You typed:", user_text)

print("\n=== SUMMARY ===")
print("input() always returns a string; convert with int(), float(), etc. when needed.")
print("print() can be customized with sep (between arguments) and end (line ending).")
