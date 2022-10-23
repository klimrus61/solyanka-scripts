import re
def isValid(s: str) -> bool:
    if s == '':
        return True
    if len(s) % 2 != 0:
        return False
    res = re.sub(r'\(\)|\[\]|\{\}', '', s)
    if res == s:
        return False
    return isValid(res)
    

print(isValid(s='()){[][(]({}))'))