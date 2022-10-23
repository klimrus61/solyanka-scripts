# 
def high(x):
    s = x.split(' ')
    b = [
        sum([ord(char)-96 for char in word]) 
        for word in s
        ]
    return s[b.index(max(b))]

print(high('what time are we climbing up the volcano'))

def high1(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))