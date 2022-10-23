# Удалить противоположные стороны света
COLLAPSE = ['NORTHSOUTH', 'SOUTHNORTH', 'WESTEAST', 'EASTWEST']
def dirReduc(arr):
    n = 0
    for i, s in enumerate(arr[1:]):
        m = str(arr[i])
        n = str(arr[i+1])
        if m + n in COLLAPSE:
            arr[i] = 0
            arr[i+1] = 0
            continue
        else:
            m = arr[i]
    while not all(arr):
        arr = [i for i in arr if i != 0]
        dirReduc(arr)
    return arr

# Чужое решение
opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}

def dirReduc(plan):
    new_plan = []
    for d in plan:
        if new_plan and new_plan[-1] == opposite[d]:
            new_plan.pop()
        else:
            new_plan.append(d)
    return new_plan

# С использованием рекурсии
def dirReduc(arr):
    opposites = [{'NORTH', 'SOUTH'}, {'EAST', 'WEST'}]

    for i in range(len(arr)-1):
        if set(arr[i:i+2]) in opposites:
            del arr[i:i+2]
            return dirReduc(arr)

    return arr
