# Сравнивает i-й элемент в ar1**2 должен быть равен элементу в arr2
def comp(arr1, arr2):
    if arr1 is None or arr2 is None:
        return False
    elif arr1 == [] and arr2 == []:
        return True
    arr1.sort(key=lambda x: abs(x))
    arr2.sort()
    res = False
    for i, val in enumerate(arr1):
        if val*val == arr2[i]:
            res = True
        else:
            res = False
            break
    return res

def comp(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False

def comp(a1, a2):
    return None not in (a1,a2) and sorted([i*i for i in a1])==sorted(a2)
