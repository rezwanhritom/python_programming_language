# Python File Reading - open(), read(), readline(), readlines()

# NOTE:
# - These examples assume text files in the current working directory.
# - Use 'with open(...) as f:' so files are closed automatically.[web:90][web:93]


print("=== READING ENTIRE FILE WITH read() ===")

def read_whole_file(path):
    """Read entire file into a single string."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = f.read()            # Reads entire file as one string[web:102]
        print("Full contents:")
        print(data)
    except FileNotFoundError:
        print(f"File not found: {path}")

# Uncomment to test:
# read_whole_file("example.txt")


print("\n=== READING CHUNKS WITH read(size) ===")

def read_in_chunks(path, size=16):
    """Read file in fixed-size chunks using read(size)."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            while True:
                chunk = f.read(size)
                if not chunk:
                    break
                print(repr(chunk))
    except FileNotFoundError:
        print(f"File not found: {path}")

# Uncomment to test:
# read_in_chunks("example.txt", size=32)


print("\n=== READING ONE LINE AT A TIME WITH readline() ===")

def read_lines_with_readline(path):
    """
    Use readline() to read one line at a time.
    Each call returns the next line (including newline). Returns '' when done.[web:93][web:99][web:102]
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            line_number = 1
            while True:
                line = f.readline()
                if not line:  # empty string means EOF
                    break
                print(f"Line {line_number}: {repr(line)}")
                line_number += 1
    except FileNotFoundError:
        print(f"File not found: {path}")

# Uncomment to test:
# read_lines_with_readline("example.txt")


print("\n=== READING ALL LINES WITH readlines() ===")

def read_all_lines_list(path):
    """
    readlines() returns a list of all lines in the file.[web:90][web:93][web:96][web:102]
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        print("Number of lines:", len(lines))
        for i, line in enumerate(lines, start=1):
            print(f"Line {i}: {repr(line)}")
    except FileNotFoundError:
        print(f"File not found: {path}")

# Uncomment to test:
# read_all_lines_list("example.txt")


print("\n=== ITERATING DIRECTLY OVER FILE OBJECT ===")

def read_with_for_loop(path):
    """
    File objects are iterable; looping over them yields lines one by one.
    This is memory-efficient and Pythonic for large files.[web:93][web:102]
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line_number, line in enumerate(f, start=1):
                print(f"Line {line_number}: {repr(line)}")
    except FileNotFoundError:
        print(f"File not found: {path}")

# Uncomment to test:
# read_with_for_loop("example.txt")


print("\n=== READING BINARY FILES (BRIEF) ===")

def read_binary_file(path, size=16):
    """
    Open file in binary mode ('rb') and read bytes.
    """
    try:
        with open(path, "rb") as f:
            chunk = f.read(size)
            print("First chunk of bytes:", chunk)
    except FileNotFoundError:
        print(f"File not found: {path}")

# Uncomment to test with an image or binary:
# read_binary_file("image.png")


print("\n=== SAFETY: USING try/except AROUND FILE OPERATIONS ===")

def safe_open(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            print("First 60 chars:")
            print(f.read(60))
    except FileNotFoundError:
        print(f"[safe_open] File not found: {path}")
    except PermissionError:
        print(f"[safe_open] Permission denied: {path}")
    except OSError as e:
        print(f"[safe_open] OS error: {e}")

# Uncomment to test:
# safe_open("nonexistent.txt")


print("\n=== SUMMARY ===")
print("read():      entire file (or chunk with read(size)) into a string.")
print("readline():  next line as a string (including newline).")
print("readlines(): list of all lines.")
print("for line in f: efficient, line-by-line iteration.")
print("Always prefer 'with open(...) as f:' to ensure files are closed properly.")
