def greet(name, owner):
    return "Hello boss" if name == owner else "Hello guest"

def greet(name, owner):
    return "Hello {}".format("boss" if name == owner else "guest")

def greet(name, owner):
    return f"Hello {'boss' if name == owner else 'guest'}"

def greet(name, owner):
    return 'Hello '+['guest','boss'][name==owner]
