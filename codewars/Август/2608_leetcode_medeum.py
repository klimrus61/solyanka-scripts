from itertools import permutations # Перестановки

def reorderedPowerOf2(n: int) -> bool:
    '''Проверить есть ли среди перестановок числа n, не начинающихся с 0, степени двойки'''
    return any(cand[0] != '0' and bin(int("".join(cand))).count('1') == 1
                   for cand in permutations(str(n)))

print(reorderedPowerOf2(n=10))