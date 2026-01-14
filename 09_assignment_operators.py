# Python Assignment Operators - Complete Reference
# These operators assign values to variables, sometimes combining with another operation.

# === SIMPLE ASSIGNMENT (=) ===
# Assigns the value on the right to the variable on the left.
x = 10
y = 5
name = "Alice"
is_active = True

print("=== SIMPLE ASSIGNMENT (=) ===")
print(f"x = {x}, y = {y}, name = {name}, is_active = {is_active}")

# Multiple assignment (you covered this in variable styles, but shown again briefly)
a = b = c = 100
p, q, r = 1, 2, 3
print(f"a = b = c = {a}")
print(f"p = {p}, q = {q}, r = {r}")


# === AUGMENTED ASSIGNMENT OPERATORS ===
# These combine an operation with assignment.
# a <op>= b  is equivalent to  a = a <op> b

print("\n=== ADDITION ASSIGNMENT (+=) ===")
num = 10
print(f"Initial num: {num}")
num += 5           # num = num + 5
print(f"After num += 5: {num}")

print("\n=== SUBTRACTION ASSIGNMENT (-=) ===")
count = 20
print(f"Initial count: {count}")
count -= 3         # count = count - 3
print(f"After count -= 3: {count}")

print("\n=== MULTIPLICATION ASSIGNMENT (*=) ===")
value = 4
print(f"Initial value: {value}")
value *= 3         # value = value * 3
print(f"After value *= 3: {value}")

print("\n=== DIVISION ASSIGNMENT (/=) ===")
total = 20
print(f"Initial total: {total}")
total /= 4         # total = total / 4  (result is float)
print(f"After total /= 4: {total} (type: {type(total)})")

print("\n=== FLOOR DIVISION ASSIGNMENT (//=) ===")
items = 17
group_size = 3
print(f"Initial items: {items}")
items //= group_size   # items = items // group_size
print(f"After items //= {group_size}: {items}")

print("\n=== MODULUS ASSIGNMENT (%=) ===")
remaining = 17
print(f"Initial remaining: {remaining}")
remaining %= 5         # remaining = remaining % 5
print(f"After remaining %= 5: {remaining}")

print("\n=== EXPONENTIATION ASSIGNMENT (**=) ===")
power = 2
print(f"Initial power: {power}")
power **= 3           # power = power ** 3
print(f"After power **= 3: {power}")


# === BITWISE AUGMENTED ASSIGNMENT OPERATORS ===
# These work on integer bit patterns.

print("\n=== BITWISE AND ASSIGNMENT (&=) ===")
flags = 0b1111   # 15
mask  = 0b1010   # 10
print(f"Initial flags: {bin(flags)}, mask: {bin(mask)}")
flags &= mask     # flags = flags & mask
print(f"After flags &= mask: {bin(flags)}")

print("\n=== BITWISE OR ASSIGNMENT (|=) ===")
flags = 0b0101   # 5
mask  = 0b0011   # 3
print(f"Initial flags: {bin(flags)}, mask: {bin(mask)}")
flags |= mask     # flags = flags | mask
print(f"After flags |= mask: {bin(flags)}")

print("\n=== BITWISE XOR ASSIGNMENT (^=) ===")
flags = 0b1100   # 12
mask  = 0b1010   # 10
print(f"Initial flags: {bin(flags)}, mask: {bin(mask)}")
flags ^= mask     # flags = flags ^ mask
print(f"After flags ^= mask: {bin(flags)}")

print("\n=== BITWISE LEFT SHIFT ASSIGNMENT (<<=) ===")
num = 3          # 0b0011
print(f"Initial num: {num} ({bin(num)})")
num <<= 2        # num = num << 2
print(f"After num <<= 2: {num} ({bin(num)})")

print("\n=== BITWISE RIGHT SHIFT ASSIGNMENT (>>=) ===")
num = 16         # 0b10000
print(f"Initial num: {num} ({bin(num)})")
num >>= 2        # num = num >> 2
print(f"After num >>= 2: {num} ({bin(num)})")


# === AUGMENTED ASSIGNMENT WITH DIFFERENT TYPES ===
print("\n=== AUGMENTED ASSIGNMENT WITH STRINGS AND LISTS ===")

# Strings: only += is valid (concatenation)
text = "Hello"
print(f"Initial text: {text}")
text += " World"      # text = text + " World"
print(f"After text += ' World': {text}")

# Lists: += extends the list (like extend)
nums = [1, 2, 3]
print(f"\nInitial list nums: {nums}")
nums += [4, 5]        # nums = nums + [4, 5]
print(f"After nums += [4, 5]: {nums}")

# *= works for sequences (repetition)
letters = ["a"]
letters *= 3          # letters = letters * 3
print(f"\n['a'] *= 3 -> {letters}")

# Invalid combinations raise TypeError (e.g., string -= ...)
# text -= "x"  # TypeError


# === ASSIGNMENT IS RIGHT-ASSOCIATIVE EXAMPLE ===
# Chained assignment is evaluated from right to left.
print("\n=== RIGHT-ASSOCIATIVE CHAINED ASSIGNMENT ===")
x = y = z = 10 + 5
print(f"x = {x}, y = {y}, z = {z}")

# You can also assign expressions
a = 5
b = a * 2
c = b + 3
print(f"a = {a}, b = {b}, c = {c}")
