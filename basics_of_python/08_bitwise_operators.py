# Python Bitwise Operators - Complete Reference
# Operate on binary representation of numbers

def binary_repr(num, width=8):
    """Return binary representation as string with fixed width."""
    return format(num & ((1 << width) - 1), f'0{width}b')  # mask to width bits


# === BITWISE AND OPERATOR (&) ===
# Returns 1 if BOTH bits are 1
print("=== BITWISE AND (&) ===")
a = 12  # Binary: 1100
b = 10  # Binary: 1010
result_and = a & b  # Binary: 1000 (8)
print(f"{a} & {b} = {result_and}")
print(f"Binary: {binary_repr(a)} & {binary_repr(b)} = {binary_repr(result_and)}")
print(f"  1100  (12)")
print(f"& 1010  (10)")
print(f"  ----")
print(f"  1000  (8)")

# Use case: Checking if number is even (num & 1 == 0)
num = 42
is_even = (num & 1) == 0
print(f"\n{num} is even: {is_even} (because {binary_repr(num)} & 00000001 = 00000000)")

# Use case: Masking bits (keep only certain bits)
mask = 0b00001111  # Keep only lower 4 bits
value = 0b10110101
masked = value & mask
print(f"\nMasking: {binary_repr(value)} & {binary_repr(mask)} = {binary_repr(masked)}")


# === BITWISE OR OPERATOR (|) ===
# Returns 1 if AT LEAST ONE bit is 1
print("\n=== BITWISE OR (|) ===")
result_or = a | b  # Binary: 1110 (14)
print(f"{a} | {b} = {result_or}")
print(f"Binary: {binary_repr(a)} | {binary_repr(b)} = {binary_repr(result_or)}")
print(f"  1100  (12)")
print(f"| 1010  (10)")
print(f"  ----")
print(f"  1110  (14)")

# Use case: Setting bits (turn on specific bits)
flag = 0b00000000
read_permission = 0b00000100
write_permission = 0b00000010
flag = flag | read_permission | write_permission
print(f"\nSetting permission bits: {binary_repr(flag)}")


# === BITWISE XOR OPERATOR (^) ===
# Returns 1 if bits are DIFFERENT
print("\n=== BITWISE XOR (^) ===")
result_xor = a ^ b  # Binary: 0110 (6)
print(f"{a} ^ {b} = {result_xor}")
print(f"Binary: {binary_repr(a)} ^ {binary_repr(b)} = {binary_repr(result_xor)}")
print(f"  1100  (12)")
print(f"^ 1010  (10)")
print(f"  ----")
print(f"  0110  (6)")

# Use case: Toggling bits (flip specific bits)
toggle_mask = 0b00001111
value = 0b10101010
toggled = value ^ toggle_mask
print(f"\nToggling bits: {binary_repr(value)} ^ {binary_repr(toggle_mask)} = {binary_repr(toggled)}")

# XOR property: A ^ A = 0, A ^ 0 = A
print(f"\nXOR properties:")
print(f"{a} ^ {a} = {a ^ a} (same number cancels out)")
print(f"{a} ^ 0 = {a ^ 0} (0 leaves number unchanged)")


# === BITWISE NOT OPERATOR (~) ===
# Inverts all bits (one's complement)
print("\n=== BITWISE NOT (~) ===")
result_not = ~a
print(f"~{a} = {result_not}")
print(f"Binary: {binary_repr(a)}  ->  {binary_repr(result_not, width=8)} (two's complement view)")
print(f"Note: ~x = -x - 1, so ~{a} = -{a} - 1 = {result_not}")


# === BITWISE LEFT SHIFT (<<) ===
# Shifts bits left, fills zeros on the right
print("\n=== BITWISE LEFT SHIFT (<<) ===")
shift_left_1 = a << 1  # Shift left by 1 bit
shift_left_2 = a << 2  # Shift left by 2 bits
print(f"{a} << 1 = {shift_left_1}")
print(f"{a} << 2 = {shift_left_2}")
print(f"Binary: {binary_repr(a)} << 1 = {binary_repr(shift_left_1, width=8)}")
print(f"Binary: {binary_repr(a)} << 2 = {binary_repr(shift_left_2, width=8)}")
print(f"Effect: left shift by n ~= multiply by 2**n, so {a} << 2 ~= {a} * 2**2 = {a * 4}")


# === BITWISE RIGHT SHIFT (>>) ===
# Shifts bits right, fills zeros on the left for positive numbers
# For negative numbers, the sign bit is extended (arithmetic shift). [web:2][web:5]
print("\n=== BITWISE RIGHT SHIFT (>>) ===")
c = 20   # 00010100
right_1 = c >> 1
right_2 = c >> 2
print(f"{c} >> 1 = {right_1}")
print(f"{c} >> 2 = {right_2}")
print(f"Binary: {binary_repr(c)} >> 1 = {binary_repr(right_1, width=8)}")
print(f"Binary: {binary_repr(c)} >> 2 = {binary_repr(right_2, width=8)}")
print(f"Effect: right shift by n ~= integer division by 2**n, so {c} >> 2 ~= {c} // 4 = {c // 4}")

# Right shift with negative numbers (arithmetic shift keeps sign bit). [web:2]
neg = -20
neg_r1 = neg >> 1
neg_r2 = neg >> 2
print(f"\nNegative right shift:")
print(f"{neg} >> 1 = {neg_r1}")
print(f"{neg} >> 2 = {neg_r2}")
print(f"Approx effect: dividing by powers of 2 with rounding toward negative infinity")

# === PRACTICAL BITWISE USE CASES ===

# 1. Using bit flags (permissions)
print("\n=== PRACTICAL: BIT FLAGS ===")
READ  = 0b001  # 1
WRITE = 0b010  # 2
EXEC  = 0b100  # 4

permissions = 0
permissions |= READ        # turn on READ
permissions |= WRITE       # turn on WRITE
print(f"Permissions after READ+WRITE: {binary_repr(permissions, 3)}")

# Check if WRITE permission is set
has_write = (permissions & WRITE) != 0
print(f"Has WRITE permission: {has_write}")

# Remove READ permission
permissions &= ~READ
print(f"After removing READ: {binary_repr(permissions, 3)}")

# 2. Quick multiply/divide by powers of 2
print("\n=== PRACTICAL: FAST MUL/DIV BY 2^n ===")
num = 7
print(f"{num} << 1 (num * 2): {num << 1}")
print(f"{num} << 2 (num * 4): {num << 2}")
print(f"{num} >> 1 (num // 2): {num >> 1}")
print(f"{num} >> 2 (num // 4): {num >> 2}")
