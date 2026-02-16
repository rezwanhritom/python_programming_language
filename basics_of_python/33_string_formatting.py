# Python String Formatting - f-strings, format(), %, Template

from string import Template

# Base variables used in examples
name = "Alice"
age = 30
pi = 3.14159265
items = 3
price_per_item = 19.99
total = items * price_per_item


print("=== F-STRINGS (PYTHON 3.6+) ===")
# f-strings: prefix string with f and put expressions in {}

print(f"Hello, {name}! You are {age} years old.")
print(f"{name} bought {items} items at ${price_per_item} each.")

# Expressions and format specifiers
print(f"Total cost: ${total:.2f}")      # 2 decimal places
print(f"Pi rounded: {pi:.3f}")         # 3 decimal places
print(f"Binary: {age:b}")              # Binary representation
print(f"Hex: {age:x}")                 # Hex representation (lowercase)

# Alignment and width
print(f"|{name:>10}|")  # Right-align in width 10
print(f"|{name:<10}|")  # Left-align in width 10
print(f"|{name:^10}|")  # Center in width 10

# Using expressions directly
print(f"{name.upper()} has been coding for {age - 20} years.")

# Using dictionary with f-string
info = {"name": "Bob", "age": 25}
print(f"{info['name']} is {info['age']} years old.")


print("\n=== str.format() METHOD ===")
# Older but still widely used; works in Python 2.6+ and all Python 3

# Positional arguments
msg1 = "Hello, {}. You are {} years old.".format(name, age)
print(msg1)

# Indexed placeholders
msg2 = "Item {0} costs ${1:.2f}. {0} is on sale!".format("Laptop", 999.99)
print(msg2)

# Named placeholders
msg3 = "Name: {name}, Age: {age}".format(name="Charlie", age=28)
print(msg3)

# Mix positional and named (not recommended for readability)
msg4 = "User {0} (id={id})".format("david", id=42)
print(msg4)

# Alignment and width with format()
print("Right-align: |{:>10}|".format(name))
print("Left-align:  |{:<10}|".format(name))
print("Center:      |{:^10}|".format(name))

# Number formatting
print("Pi: {:.4f}".format(pi))           # 4 decimal places
print("Percent: {:.2%}".format(0.1234))  # percentage with 2 decimals


print("\n=== OLD-STYLE % FORMATTING ===")
# C-style printf formatting; still used in some places (e.g., logging)

# %s for string, %d for integer, %f for float
msg = "Hello, %s. You are %d years old." % (name, age)
print(msg)

# Width and precision
msg_price = "Each item costs $%.2f" % price_per_item
print(msg_price)

# Multiple specifiers
msg_multi = "%s bought %d items for a total of $%.2f" % (name, items, total)
print(msg_multi)

# Named mapping with % (using dictionary)
data = {"user": "admin", "count": 5}
msg_map = "%(user)s has %(count)d messages." % data
print(msg_map)


print("\n=== TEMPLATE STRINGS (string.Template) ===")
# Safer for untrusted input, e.g., user-provided templates

template_str = "Hello, $name! You have $count unread messages."
t = Template(template_str)

result = t.substitute(name="Eve", count=7)
print(result)

# Using a dictionary
user = {"name": "Frank", "count": 3}
result2 = t.substitute(user)
print(result2)

# safe_substitute: leaves placeholders unchanged if missing
partial = Template("Hello, $name! Your balance is $balance.")
safe_result = partial.safe_substitute(name="Grace")
print(safe_result)  # $balance remains as-is


print("\n=== COMPARISON EXAMPLES ===")
# Same message using different methods

item = "book"
cost = 12.5

# f-string
msg_f = f"The {item} costs ${cost:.2f}"
print("f-string:        ", msg_f)

# str.format()
msg_format = "The {} costs ${:.2f}".format(item, cost)
print("str.format():    ", msg_format)

# % formatting
msg_percent = "The %s costs $%.2f" % (item, cost)
print("% formatting:    ", msg_percent)

# Template
msg_template = Template("The $item costs $$${price}")
print("Template:        ", msg_template.substitute(item=item, price=f"{cost:.2f}"))


print("\n=== ADVANCED FORMAT SPECIFIERS ===")
value = 1234.56789

print("Default:        {}".format(value))
print("2 decimals:     {:.2f}".format(value))
print("Comma sep:      {:,.2f}".format(value))
print("Width 10:       |{:10.2f}|".format(value))
print("Left aligned:   |{:<10.2f}|".format(value))
print("Right aligned:  |{:>10.2f}|".format(value))
print("Center aligned: |{:^10.2f}|".format(value))

# Same with f-strings
print(f"\nF-string 2 dec:    {value:.2f}")
print(f"F-string comma:    {value:,.2f}")
print(f"F-string padded:   |{value:10.2f}|")
