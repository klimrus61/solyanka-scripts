def twoSum( nums, target: int):
        sorted_list = sorted(nums)
        
        for i, _ in enumerate(sorted_list):
            if i != len(sorted_list) - 1:
                low = i + 1
                high = len(sorted_list) - 1
                
                while low <= high:
                    mid = (low+high) // 2
                    guess = sorted_list[mid]
                    if guess == target - sorted_list[i]:
                        return [i, mid]
                    elif guess > target - sorted_list[i]:
                        high = mid - 1
                    else:
                        low = mid + 1
            else:
                return None

print(twoSum([2,7,11,15], 9))
                
            