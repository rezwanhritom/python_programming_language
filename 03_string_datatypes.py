# Python String Data Types - Complete Reference

# === STRING CREATION ===
# Single quotes
single_quoted = 'Hello'
# Double quotes
double_quoted = "World"
# Triple quotes for multiline
multiline = """This is a
multiline string"""
print(f"Single: {single_quoted}, Double: {double_quoted}")
print(f"Multiline:\n{multiline}")

# === STRING INDEXING ===
text = "Python"
first_char = text[0]      # 'P'
last_char = text[-1]      # 'n'
second_last = text[-2]    # 'o'
print(f"First: {first_char}, Last: {last_char}, Second Last: {second_last}")

# === STRING SLICING ===
# Syntax: string[start:end:step]
substring1 = text[0:4]    # 'Pyth' (0 to 3)
substring2 = text[:4]     # 'Pyth' (start to 3)
substring3 = text[2:]     # 'thon' (2 to end)
substring4 = text[:]      # 'Python' (copy)
substring5 = text[::-1]   # 'nohtyP' (reversed)
print(f"Slice [0:4]: {substring1}")
print(f"Slice [:4]: {substring2}")
print(f"Slice [2:]: {substring3}")
print(f"Slice [:]: {substring4}")
print(f"Reversed: {substring5}")

# === STRING ESCAPING ===
escaped1 = "He said \"Hello\""  # Escape double quotes
escaped2 = 'It\'s a string'     # Escape single quote
escaped3 = "Line1\nLine2"       # Newline
escaped4 = "Tab\tseparated"     # Tab
print(f"Escaped quotes: {escaped1}")
print(f"Escaped apostrophe: {escaped2}")
print(f"Newline:\n{escaped3}")
print(f"Tab: {escaped4}")

# === RAW STRINGS ===
# Prefix with r to ignore escape sequences
path = r"C:\Users\Documents\file.txt"
regex = r"\d+\.\d+"
print(f"Raw string path: {path}")
print(f"Raw regex: {regex}")

# === STRING CONCATENATION ===
str1 = "Hello"
str2 = "World"
combined = str1 + " " + str2
repeated = "Hi " * 3
print(f"Concatenated: {combined}")
print(f"Repeated: {repeated}")

# === STRING LENGTH ===
text = "Python"
length = len(text)
print(f"Length of '{text}': {length}")

# === STRING IMMUTABILITY ===
# Strings cannot be changed in-place
# text[0] = 'J'  # Uncomment to see TypeError
