# Python pass Statement - Complete Reference
# pass is a placeholder that does nothing

# === PASS IN IF STATEMENTS ===
print("=== PASS IN IF STATEMENTS ===")
age = 15

if age < 18:
    pass  # TODO: implement minor handling
else:
    print("Adult logic here")

print("Continuing with program...")


# === PASS IN LOOPS ===
print("\n=== PASS IN LOOPS ===")
for i in range(5):
    if i == 2:
        pass  # Skip processing for i=2 but continue loop
    print(f"Processing {i}")


# === PASS IN FUNCTION DEFINITIONS ===
print("\n=== PASS IN FUNCTION DEFINITIONS ===")
def placeholder_function():
    pass  # Will implement later

def another_placeholder(param1, param2):
    """This function will do something soon"""
    pass

# Call the placeholder functions
placeholder_function()
another_placeholder("a", "b")
print("Functions called successfully (did nothing)")


# === PASS IN CLASS DEFINITIONS ===
print("\n=== PASS IN CLASS DEFINITIONS ===")
class PlaceholderClass:
    pass  # Will add attributes and methods later

class AnotherClass:
    def method1(self):
        pass
    
    def method2(self, x):
        pass

# Create instances
obj = PlaceholderClass()
obj2 = AnotherClass()
print("Objects created successfully")


# === PASS WITH TRY/EXCEPT ===
print("\n=== PASS WITH TRY/EXCEPT ===")
data = ["10", "20", "thirty", "40"]

for item in data:
    try:
        num = int(item)
        print(f"Number: {num}")
    except ValueError:
        pass  # Silently ignore non-numeric data

print("Processing complete (errors ignored)")


# === PASS VS CONTINUE ===
print("\n=== PASS VS CONTINUE ===")
print("With pass:")
for i in range(3):
    if i == 1:
        pass  # Does nothing, continues to print
    print(f"After pass: {i}")

print("\nWith continue:")
for i in range(3):
    if i == 1:
        continue  # Skips rest of loop, goes to next iteration
    print(f"After continue: {i}")


# === PASS IN IF-ELIF-ELSE ===
print("\n=== PASS IN IF-ELIF-ELSE ===")
value = 5

if value < 0:
    print("Negative")
elif value == 0:
    pass  # Do nothing for zero
elif value < 10:
    print("Small positive")
else:
    pass  # Do nothing for large values


# === PASS IN WHILE LOOP ===
print("\n=== PASS IN WHILE LOOP ===")
count = 0
while count < 5:
    if count == 2:
        pass  # Skip special processing for 2
    print(f"Count: {count}")
    count += 1


# === PASS IN MATCH/CASE (PYTHON 3.10+) ===
print("\n=== PASS IN MATCH/CASE (PYTHON 3.10+) ===")
def handle_command(command):
    match command:
        case "start":
            print("Starting...")
        case "stop":
            print("Stopping...")
        case "status":
            pass  # TODO: implement status check
        case _:
            print(f"Unknown command: {command}")

handle_command("start")
handle_command("status")  # Does nothing
handle_command("unknown")


# === PASS IN CONTEXT MANAGERS ===
print("\n=== PASS IN CONTEXT MANAGERS ===")
# Simulate resource that might not be needed
resource_needed = False

# Without pass, you'd need to indent or use conditional
if resource_needed:
    # with open_resource() as resource:
    #     use_resource(resource)
    pass
else:
    print("Resource not needed, skipping")


# === PASS IN ABSTRACT METHODS ===
print("\n=== PASS IN ABSTRACT METHODS ===")
from abc import ABC, abstractmethod

class AbstractBase(ABC):
    @abstractmethod
    def must_implement(self):
        pass  # Subclasses must override this

class ConcreteClass(AbstractBase):
    def must_implement(self):
        print("Concrete implementation")

# obj = AbstractBase()  # Can't instantiate abstract class
obj = ConcreteClass()
obj.must_implement()


# === PASS WITH LAMBDAS (PLACEHOLDER) ===
print("\n=== PASS WITH LAMBDAS ===")
# Can't use pass in lambda, but can use None or 0
placeholder_func = lambda x: None  # Does nothing
result = placeholder_func(10)
print(f"Lambda result: {result}")


# === PRACTICAL: STUB IMPLEMENTATION ===
print("\n=== PRACTICAL: STUB IMPLEMENTATION ===")
class DatabaseConnection:
    def connect(self):
        pass  # Will implement actual connection logic
    
    def query(self, sql):
        pass  # Will implement query execution
    
    def close(self):
        pass  # Will implement connection closing

# Use stub in development
db = DatabaseConnection()
db.connect()
db.query("SELECT * FROM users")
db.close()
print("Database operations completed (stubbed)")


# === PASS IN CONDITIONAL EXPRESSIONS ===
print("\n=== PASS IN CONDITIONAL EXPRESSIONS ===")
# Can't use pass directly, but can use None
value = 10
result = "large" if value > 5 else None  # None acts as placeholder
print(f"Result: {result}")


# === PASS IN COMPREHENSIONS ===
print("\n=== PASS IN COMPREHENSIONS ===")
# Can't use pass in comprehensions directly
# Use filtering instead
numbers = [1, 2, 3, 4, 5]
# Instead of: [process(x) if x > 2 else pass for x in numbers]
# Use: [process(x) for x in numbers if x > 2]
filtered = [x for x in numbers if x > 2]  # Implicit pass for x <= 2
print(f"Filtered numbers: {filtered}")

# Equivalent explicit loop
result = []
for x in numbers:
    if x > 2:
        result.append(x)
    else:
        pass  # Explicit pass for clarity
print(f"Same result: {result}")


# === PASS AS CODE SKELETON ===
print("\n=== PASS AS CODE SKELETON ===")
class MyAPI:
    def __init__(self):
        pass
    
    def authenticate(self, token):
        pass
    
    def get_data(self, endpoint):
        pass
    
    def post_data(self, endpoint, data):
        pass
    
    def close(self):
        pass

# This skeleton can be filled in incrementally
api = MyAPI()
# api.authenticate("token")
# data = api.get_data("/users")
# api.close()
print("API skeleton created")


# === PASS INFINAL SUMMARY ===
print("\n=== SUMMARY ===")
print("pass is a null operation - nothing happens when it executes")
print("Use it when syntax requires a statement but you need no action")
print("Common uses: placeholders, stubs, ignored exceptions, empty blocks")
