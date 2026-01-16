# Python Nested if Statements - Complete Reference
# if statements inside other if statements

# === TWO-LEVEL NESTING ===
print("=== TWO-LEVEL NESTING ===")
age = 20
has_id = True

if age >= 18:
    print("Age check passed")
    if has_id:
        print("ID check passed")
        print("Access granted")
    else:
        print("ID check failed")
        print("Access denied")
else:
    print("Age check failed")
    print("Access denied")


# === THREE-LEVEL NESTING ===
print("\n=== THREE-LEVEL NESTING ===")
temperature = 75
humidity = 60
wind_speed = 10

if temperature > 70:
    print("It's warm outside")
    if humidity > 50:
        print("And humid")
        if wind_speed < 15:
            print("Light breeze - comfortable")
        else:
            print("Windy - might be uncomfortable")
    else:
        print("But not humid")
        if wind_speed < 15:
            print("Pleasant conditions")
        else:
            print("Windy but dry")
else:
    print("It's cool outside")
    if humidity > 50:
        print("And humid - might feel chilly")
    else:
        print("Dry cool weather")


# === NESTING WITH ELIF ===
print("\n=== NESTING WITH ELIF ===")
score = 85
attendance = 95

if score >= 90:
    if attendance >= 90:
        grade = "A+"
    elif attendance >= 80:
        grade = "A"
    else:
        grade = "A-"
elif score >= 80:
    if attendance >= 90:
        grade = "B+"
    elif attendance >= 80:
        grade = "B"
    else:
        grade = "B-"
else:
    grade = "C or below"

print(f"Score: {score}, Attendance: {attendance} -> Grade: {grade}")


# === REAL-WORLD: USER AUTHENTICATION ===
print("\n=== REAL-WORLD: USER AUTHENTICATION ===")
username = "admin"
password = "secret123"
is_active = True
has_2fa = False

if username == "admin":
    if password == "secret123":
        if is_active:
            print("Login successful")
            if has_2fa:
                print("2FA verified")
            else:
                print("Warning: 2FA not enabled")
        else:
            print("Account is deactivated")
    else:
        print("Incorrect password")
else:
    print("Username not found")


# === REAL-WORLD: ORDER VALIDATION ===
print("\n=== REAL-WORLD: ORDER VALIDATION ===")
item_in_stock = True
quantity_available = 50
order_quantity = 30
customer_is_premium = True
payment_method_valid = True

if item_in_stock:
    if order_quantity <= quantity_available:
        if customer_is_premium:
            print("Premium customer discount applied")
            if payment_method_valid:
                print("Order confirmed with premium discount")
            else:
                print("Payment method invalid")
        else:
            print("Standard pricing applied")
            if payment_method_valid:
                print("Order confirmed")
            else:
                print("Payment method invalid")
    else:
        print(f"Insufficient quantity. Available: {quantity_available}")
else:
    print("Item is out of stock")


# === FLATTENING VS NESTING ===
print("\n=== COMPARISON: NESTED VS FLATTENED ===")

# Nested version (harder to read)
value = 42
if value > 0:
    if value < 100:
        if value % 2 == 0:
            print("Nested: Positive, less than 100, even")
        else:
            print("Nested: Positive, less than 100, odd")
    else:
        print("Nested: Positive, 100 or more")
else:
    print("Nested: Zero or negative")

# Flattened version (easier to read with 'and')
if value > 0 and value < 100 and value % 2 == 0:
    print("Flattened: Positive, less than 100, even")
elif value > 0 and value < 100 and value % 2 != 0:
    print("Flattened: Positive, less than 100, odd")
elif value > 0 and value >= 100:
    print("Flattened: Positive, 100 or more")
else:
    print("Flattened: Zero or negative")


# === DEEPLY NESTED EXAMPLE (4 LEVELS) ===
print("\n=== DEEPLY NESTED (4 LEVELS) ===")
weather = "sunny"
temperature = 80
time_of_day = "afternoon"
activity = "hiking"

if weather == "sunny":
    if temperature > 75:
        if time_of_day == "morning":
            if activity == "hiking":
                print("Perfect morning hike weather")
            elif activity == "swimming":
                print("Good morning for swimming")
            else:
                print("Nice morning for outdoor activities")
        elif time_of_day == "afternoon":
            if activity == "hiking":
                print("Hot afternoon hike - bring water")
            elif activity == "swimming":
                print("Perfect afternoon swim weather")
            else:
                print("Hot afternoon - stay hydrated")
        else:
            print("Warm evening")
    else:
        print("Cool sunny day")
else:
    print("Not sunny - check weather conditions")
