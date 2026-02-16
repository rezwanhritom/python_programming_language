# Python String Methods - Common Operations
# Methods covered: upper, lower, strip, lstrip, rstrip, split, rsplit, splitlines, join, replace

print("=== BASIC STRING ===")
text = "  Hello, World!  "
print(f"Original: '{text}'")


# === CASE CONVERSION METHODS ===
print("\n=== CASE CONVERSION ===")
s = "Python Programming"

lower_s = s.lower()      # All characters to lowercase
upper_s = s.upper()      # All characters to uppercase
title_s = s.title()      # First letter of each word uppercase
capitalize_s = s.capitalize()  # First character uppercase, rest lowercase
swapcase_s = s.swapcase()      # Swap case of each character

print(f"Original: '{s}'")
print(f"lower():      '{lower_s}'")
print(f"upper():      '{upper_s}'")
print(f"title():      '{title_s}'")
print(f"capitalize(): '{capitalize_s}'")
print(f"swapcase():   '{swapcase_s}'")


# === STRIP METHODS ===
print("\n=== STRIP METHODS ===")
s = "   \t  hello world  \n  "

print(f"Original (repr): {repr(s)}")
print(f"strip():  {repr(s.strip())}")   # Remove leading/trailing whitespace
print(f"lstrip(): {repr(s.lstrip())}")  # Remove leading whitespace
print(f"rstrip(): {repr(s.rstrip())}")  # Remove trailing whitespace

# strip with custom characters (not substring, but a set of chars)
s2 = "---hello---"
print(f"\nCustom strip:")
print(f"Original: {repr(s2)}")
print(f"s2.strip('-'):  {repr(s2.strip('-'))}")
print(f"s2.lstrip('-'): {repr(s2.lstrip('-'))}")
print(f"s2.rstrip('-'):{repr(s2.rstrip('-'))}")


# === SPLIT METHODS ===
print("\n=== SPLIT METHODS ===")
sentence = "one two  three   four"
print(f"Sentence: {repr(sentence)}")

# Default split: splits on any whitespace, treats multiple as one
parts_default = sentence.split()
print(f"split():         {parts_default}")

# Split with explicit separator
csv_line = "apple,banana,cherry,,date"
print(f"\nCSV line: {repr(csv_line)}")
print(f"csv_line.split(','): {csv_line.split(',')}")

# Split with maxsplit
print(f"csv_line.split(',', 2): {csv_line.split(',', 2)}")

# rsplit: split from the right
print(f"csv_line.rsplit(',', 2): {csv_line.rsplit(',', 2)}")

# splitlines: split on line breaks
multi_line = "line1\nline2\r\nline3\n"
print(f"\nMulti-line: {repr(multi_line)}")
print(f"multi_line.splitlines(): {multi_line.splitlines()}")
print(f"multi_line.splitlines(keepends=True): {multi_line.splitlines(keepends=True)}")


# === JOIN METHOD ===
print("\n=== JOIN METHOD ===")
words = ["Python", "is", "fun"]
joined_space = " ".join(words)
joined_dash = "-".join(words)
print(f"Words: {words}")
print(f"' '.join(words): '{joined_space}'")
print(f"'-'.join(words): '{joined_dash}'")

# Joining characters of a string
chars = list("ABC")
print(f"\nChars: {chars}")
print(f"':'.join(chars): '{':'.join(chars)}'")

# Be careful: join() takes an iterable of strings only
# mixed = ['a', 1, 'b']
# ','.join(mixed)  # TypeError: sequence item 1: expected str instance, int found


# === REPLACE METHOD ===
print("\n=== REPLACE METHOD ===")
s = "cats are great. I love cats. cats everywhere!"
print(f"Original: {s}")

# Replace all occurrences
all_replaced = s.replace("cats", "dogs")
print(f"replace('cats', 'dogs'): {all_replaced}")

# Replace with limit (count)
first_two = s.replace("cats", "dogs", 2)
print(f"replace('cats', 'dogs', 2): {first_two}")

# Replace substring not present (no change)
no_change = s.replace("tigers", "lions")
print(f"replace('tigers', 'lions'): {no_change}")


# === COMBINATION EXAMPLE ===
print("\n=== COMBINATION EXAMPLE: CLEAN AND NORMALIZE ===")
raw = "   Hello,   PYTHON   world!  "
print(f"Raw: {repr(raw)}")

# Steps: trim, normalize spaces, lowercase
clean = raw.strip()
parts = clean.split()           # splits on any whitespace -> tokens
normalized = " ".join(parts)    # join with single spaces
lowered = normalized.lower()

print(f"strip():           {repr(clean)}")
print(f"split():           {parts}")
print(f\"' '.join(parts):   {repr(normalized)}\")
print(f\"lower():           {repr(lowered)}\")
