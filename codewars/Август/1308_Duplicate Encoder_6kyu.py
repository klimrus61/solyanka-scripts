# "recede"   =>  "()()()"
def duplicate_encode(word):
    l = word.lower()
    d = {x: l.count(x) for x in set(l)}
    return ''.join([')' if d[char] > 1 else '(' for char in l])


def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])