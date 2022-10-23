def number(lines):
    if lines:
        return [f'{i+1}: {s}' for i, s in enumerate(lines)]

number(["a", "b", "c"])