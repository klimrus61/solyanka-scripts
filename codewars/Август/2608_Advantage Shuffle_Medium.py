from itertools import permutations

def advantageCount(nums1 = [2,7,11,15], nums2 = [1,10,4,11]):
    count_old = 0
    for permutation in permutations(nums1):
        count_curr = 0
        for i in range(len(permutation)):
            if permutation[i] > nums2[i]:
                count_curr += 1
        if count_curr > count_old:
            m = permutation
            count_old = count_curr
    return list(m)

print(advantageCount())
            