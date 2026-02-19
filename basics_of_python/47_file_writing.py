# Python File Writing - write(), writelines(), append mode

# Modes:
#   "w"  - write (truncate/overwrite file or create new)
#   "a"  - append (write at end, keep existing content)[web:91][web:94][web:97][web:100]
#   "x"  - exclusive creation (fail if file exists)
#   "r+" - read/write (must exist)


print("=== WRITING TEXT WITH write() (MODE='w') ===")

def write_single_file(path):
    """
    Open file in write mode and write text.
    'w' will create the file or overwrite if it exists.[web:94][web:100]
    """
    with open(path, "w", encoding="utf-8") as f:
        f.write("First line\n")
        f.write("Second line\n")
        f.write("Third line\n")
    print(f"Wrote 3 lines to {path} (overwriting any existing content).")

# Uncomment to test:
# write_single_file("output.txt")


print("\n=== APPENDING TEXT WITH write() (MODE='a') ===")

def append_to_file(path):
    """
    Open file in append mode and add new content at the end.[web:91][web:94][web:97][web:100]
    """
    with open(path, "a", encoding="utf-8") as f:
        f.write("Appended line A\n")
        f.write("Appended line B\n")
    print(f"Appended 2 lines to {path}.")

# Uncomment to test:
# append_to_file("output.txt")


print("\n=== WRITING MULTIPLE LINES WITH writelines() ===")

def write_lines_with_writelines(path):
    """
    writelines() writes a sequence of strings to the file;
    it does NOT add newlines automatically.[web:91][web:94][web:97][web:103]
    """
    lines = [
        "Line 1\n",
        "Line 2\n",
        "Line 3\n",
    ]
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(lines)
    print(f"writelines() wrote {len(lines)} lines to {path}.")

# Uncomment to test:
# write_lines_with_writelines("lines.txt")


print("\n=== APPENDING MULTIPLE LINES WITH writelines() ===")

def append_lines_with_writelines(path):
    more_lines = [
        "Extra 1\n",
        "Extra 2\n",
        "Extra 3\n",
    ]
    with open(path, "a", encoding="utf-8") as f:
        f.writelines(more_lines)
    print(f"Appended {len(more_lines)} lines to {path} using writelines().")

# Uncomment to test:
# append_lines_with_writelines("lines.txt")


print("\n=== USING print(..., file=f) TO WRITE ===")

def write_using_print(path):
    """
    print() can write to files when given file= parameter.
    It automatically adds newline unless end= is overridden.
    """
    with open(path, "a", encoding="utf-8") as f:
        print("This line is written via print().", file=f)
        print("Another printed line.", file=f)
    print(f"Wrote 2 lines to {path} via print().")

# Uncomment to test:
# write_using_print("print_out.txt")


print("\n=== WRITING BINARY FILES (BRIEF) ===")

def write_binary_file(path):
    """
    Open file in binary write mode ('wb') and write bytes.
    """
    data = b"\x00\x01\x02\x03hello"
    with open(path, "wb") as f:
        f.write(data)
    print(f"Wrote {len(data)} bytes to {path} in binary mode.")

# Uncomment to test:
# write_binary_file("binary.dat")


print("\n=== READ-BACK HELPER FOR DEMO ===")

def show_file(path):
    """Utility to display file contents."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            print(f"--- {path} contents ---")
            print(f.read())
            print("------ end ------")
    except FileNotFoundError:
        print(f"{path} does not exist.")

# Uncomment a mini demo:
# write_single_file("demo.txt")
# append_to_file("demo.txt")
# append_lines_with_writelines("demo.txt")
# write_using_print("demo.txt")
# show_file("demo.txt")


print("\n=== CONTEXT MANAGERS AND ERROR HANDLING ===")

def safe_write(path, content):
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Successfully wrote to {path}")
    except PermissionError:
        print(f"Permission denied when writing to {path}")
    except OSError as e:
        print(f"OS error while writing to {path}: {e}")

# Uncomment to test:
# safe_write("safe_output.txt", "Some safe content\n")


print("\n=== SUMMARY ===")
print("write():      write a string (or bytes in binary mode) to a file.")
print("writelines(): write an iterable of strings (no newlines added automatically).")
print("Mode 'w':     overwrite or create file.")
print("Mode 'a':     append to end without erasing existing data.")
print("Always prefer 'with open(...) as f:' so files are closed, even on errors.")
