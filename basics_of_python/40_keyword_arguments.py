# Python **kwargs - Variable Keyword Arguments

print("=== BASIC **kwargs USAGE ===")

def show_kwargs(**kwargs):
    """
    **kwargs collects any number of keyword arguments into a dict.[web:76][web:79][web:82][web:85][web:88]
    """
    print("kwargs:", kwargs, "| type:", type(kwargs))
    for key, value in kwargs.items():
        print(f"  {key} = {value}")

show_kwargs()
show_kwargs(a=1, b=2)
show_kwargs(name="Alice", age=30, city="Paris")


print("\n=== MIXING REGULAR PARAMETERS WITH **kwargs ===")

def describe_user(username, **details):
    """
    username: regular parameter
    **details: variable keyword arguments (stored in a dict).
    """
    print("Username:", username)
    if not details:
        print("No extra details.")
    else:
        print("Details:")
        for key, value in details.items():
            print(f"  {key}: {value}")

describe_user("alice123")
describe_user("bob456", age=25, city="London")
describe_user("charlie789", age=30, city="Berlin", active=True)


print("\n=== ORDER OF PARAMETERS WITH **kwargs ===")

def order_demo(a, b, *args, c=0, d=0, **kwargs):
    """
    Correct parameter order:
      1) regular parameters (a, b)
      2) *args
      3) keyword-only parameters with defaults (c, d)
      4) **kwargs (catch-all keyword arguments)[web:76][web:79][web:82][web:88]
    """
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"c={c}, d={d}")
    print(f"kwargs={kwargs}")

order_demo(1, 2, 3, 4, c=5, x=10, y=20)


print("\n=== FORWARDING **kwargs TO ANOTHER FUNCTION ===")

def base_config(**options):
    """Print and return configuration options."""
    print("Base config options:", options)
    return options

def configure_system(name, **overrides):
    """
    Start with default config, then apply overrides from **overrides.
    """
    default = {"debug": False, "timeout": 30, "retries": 3}
    print(f"\nConfiguring system '{name}'")
    # Merge defaults and overrides
    config = {**default, **overrides}
    return base_config(**config)  # Forward as keyword arguments

conf1 = configure_system("alpha")
conf2 = configure_system("beta", debug=True, timeout=10)
conf3 = configure_system("gamma", retries=5, log_level="INFO")


print("\n=== UNPACKING DICTS WITH ** IN CALLS ===")

def connect(host, port, use_ssl=False, timeout=30):
    print(f"host={host}, port={port}, use_ssl={use_ssl}, timeout={timeout}")

params = {"host": "example.com", "port": 443, "use_ssl": True}
connect(**params)  # Unpack dict into keyword arguments

# Combine dict and explicit keyword args
more_params = {"host": "localhost", "port": 8000}
connect(**more_params, timeout=5)


print("\n=== COMBINING *args AND **kwargs ===")

def debug(title, *args, **kwargs):
    """
    Demonstrate using both *args and **kwargs together.
    """
    print(f"Title: {title}")
    print("Positional args:", args)
    print("Keyword args:", kwargs)

debug("Run 1", 1, 2, 3, mode="test", verbose=True)
debug("Run 2", user="alice", retries=3)


print("\n=== REALISTIC EXAMPLE: BUILDING QUERY STRING ===")

def build_query(base_url, **params):
    """
    Build a URL with query parameters from **params.
    Order of params in URL is not guaranteed since dicts are ordered by insertion.
    """
    if not params:
        return base_url

    parts = []
    for key, value in params.items():
        parts.append(f"{key}={value}")
    query = "&".join(parts)
    return f"{base_url}?{query}"

print(build_query("https://api.example.com/items"))
print(build_query("https://api.example.com/items", page=2, limit=25, sort="name"))


print("\n=== REALISTIC EXAMPLE: FLEXIBLE LOGGING FUNCTION ===")

def log(level, *messages, **context):
    """
    Simple logging function:
      - level: log level (INFO, WARN, ERROR, etc.)
      - messages: positional messages to join
      - context: extra metadata as keyword args
    """
    line = f"[{level}] " + " ".join(str(m) for m in messages)
    if context:
        meta = " ".join(f"{k}={v}" for k, v in context.items())
        line += " | " + meta
    print(line)

log("INFO", "System started")
log("WARN", "Low disk space", path="/var", free="500MB")
log("ERROR", "Failed to save file", filename="data.txt", user="alice", retry=False)


print("\n=== SUMMARY ===")
print("**kwargs gathers variable keyword arguments into a dict.")
print("Use ** to unpack dictionaries into keyword arguments when calling functions.")
print("Correct parameter order: regular, *args, keyword-only, **kwargs.")
