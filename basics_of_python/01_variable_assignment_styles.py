# Python Variable Assignment Styles - All Possible Ways

# === SINGLE ASSIGNMENT ===
# Most basic form: variable = value
a = 10
name = "Alice"
is_active = True

# === MULTIPLE ASSIGNMENT (UNPACKING) ===
# Assign multiple variables in one line
x, y, z = 1, 2, 3
print(f"x={x}, y={y}, z={z}")

# === CHAINED ASSIGNMENT ===
# Assign same value to multiple variables
p = q = r = 100
print(f"p={p}, q={q}, r={r}")

# === PARALLEL ASSIGNMENT (SWAP) ===
# Swap values without temporary variable
a, b = 5, 10
print(f"Before swap: a={a}, b={b}")
a, b = b, a
print(f"After swap: a={a}, b={b}")

# === AUGMENTED ASSIGNMENT ===
# Combine operation with assignment
count = 0
count += 1   # Same as: count = count + 1
count -= 1   # Same as: count = count - 1
count *= 2   # Same as: count = count * 2
count /= 2   # Same as: count = count / 2
count //= 2  # Same as: count = count // 2
count %= 3   # Same as: count = count % 3
count **= 2  # Same as: count = count ** 2

# === SEQUENCE UNPACKING ===
# Unpack sequences into variables
coordinates = (10, 20, 30)
lat, lon, alt = coordinates
print(f"Latitude: {lat}, Longitude: {lon}, Altitude: {alt}")

# === EXTENDED UNPACKING (PYTHON 3+) ===
# Grab remaining items with *
first, *middle, last = [1, 2, 3, 4, 5]
print(f"First: {first}, Middle: {middle}, Last: {last}")

# === UNDERSCORE VARIABLE ===
# Use _ to ignore values
_, important, _ = (10, 20, 30)
print(f"Important value: {important}")

# === DYNAMIC TYPING DEMONSTRATION ===
dynamic = 42
print(f"Type of dynamic: {type(dynamic)}")
dynamic = "Now I'm a string"
print(f"Type of dynamic: {type(dynamic)}")
dynamic = [1, 2, 3]
print(f"Type of dynamic: {type(dynamic)}")
