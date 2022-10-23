def generator(arr):
    for i, v in enumerate(arr):
        yield i, v
def find_uniq(arr):
    a = arr[0]
    n = 0
    i = 0
    while n == 0 and i <= 1:
        i += 1
        if a == arr[i]:
            continue
        elif a != arr[i] and a != arr[i+1]:
            return a
        else:
            return arr[i]
    for i, v in generator(arr[3:]):
        if v == a:
            continue
        else:
            return arr[i+3]   # n: unique number in the array

# Чужое решение
def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b

def find_uniq(arr):
    a = sorted(arr)
    return a[0] if a[0] != a[1] else a[-1]
