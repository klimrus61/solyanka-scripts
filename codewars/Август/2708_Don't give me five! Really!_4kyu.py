# import re

# def dont_give_me_five(start, end):
#     count = lambda n: int(re.sub(r'5(\d*)', lambda m: '4' + '9' * len(m[1]), str(n)).translate(str.maketrans("56789", "45678")), 9)
#     if start > 0:
#         return count(end) - count(start - 1)
#     elif end < 0:
#         return count(-start) - count(-end - 1)
#     else:
#         return count(end) + count(-start) + 1
def dont_give_me_five(start, end):
    if not (start == 1 and end >= 1):
        if start > end: return 0
        if start == end: return int('5' not in str(start))
        if start == 0: return 1 + dont_give_me_five(1, end)
        if end == 0: return 1 + dont_give_me_five(1, -start)
        if start <= 0 and end <= 0: return dont_give_me_five(1, -start) - dont_give_me_five(1, -end-1)
        if start <= 0 and end >= 1: return dont_give_me_five(1, -start) + 1 + dont_give_me_five(1, end)
        return dont_give_me_five(1, end) - dont_give_me_five(1, start-1)
    total, i = 0, 0
    while end != 0: 
        digit, x = end % 10, 9 ** i
        if digit == 5:
            total = -1
        elif digit > 5: 
            total -= x
        total += digit * x
        i += 1
        end //= 10
    return total;
print(dont_give_me_five(end=-4977779768738428491, start=-7771343902412479705))