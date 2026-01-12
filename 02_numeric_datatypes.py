# Python Numeric Data Types - Complete Reference

# === INTEGER TYPE ===
# Whole numbers, unlimited size in Python 3
positive_int = 100
negative_int = -50
zero = 0
print(f"Integers: {positive_int}, {negative_int}, {zero}")

# === BINARY LITERALS ===
# Prefix with 0b or 0B
binary_num = 0b1010  # Decimal 10
print(f"Binary 0b1010 = {binary_num}")

# === OCTAL LITERALS ===
# Prefix with 0o or 0O
octal_num = 0o12  # Decimal 10
print(f"Octal 0o12 = {octal_num}")

# === HEXADECIMAL LITERALS ===
# Prefix with 0x or 0X
hex_num = 0xA  # Decimal 10
print(f"Hexadecimal 0xA = {hex_num}")

# === FLOAT TYPE ===
# Numbers with decimal points
float1 = 3.14
float2 = 2.0
float3 = -0.5
scientific = 1.5e3  # 1500.0
print(f"Floats: {float1}, {float2}, {float3}, Scientific: {scientific}")

# === COMPLEX TYPE ===
# Numbers with real and imaginary parts
complex1 = 3 + 4j
complex2 = 2j
complex3 = complex(5, 6)  # Using complex() constructor
print(f"Complex: {complex1}, Real part: {complex1.real}, Imag part: {complex1.imag}")

# === TYPE CHECKING ===
num = 42
print(f"Type of {num}: {type(num)}")
print(f"Is integer: {isinstance(num, int)}")
print(f"Is float: {isinstance(num, float)}")

# === ARITHMETIC WITH DIFFERENT TYPES ===
# Python automatically promotes types
result1 = 5 + 3.0    # int + float = float
result2 = 10 / 3     # Division always returns float
result3 = 10 // 3    # Floor division returns int
print(f"5 + 3.0 = {result1} (type: {type(result1)})")
print(f"10 / 3 = {result2} (type: {type(result2)})")
print(f"10 // 3 = {result3} (type: {type(result3)})")
