from collections import Counter
from functools import lru_cache


class Solution:
    def minStickers(self, stickers, target: str) -> int:
        # idea is to maintain state of remaining target string s
		# value for s is the min number of stickers used to reach s
        # objective is to reduce s to empty
        # choosing every sticker from valid stickers to try and then simply replacing s using the chars from sticker, wil guarantee correctness
		# let t,w be size of target and sticker respectively
		# naive
        # height is t, worst case one sticker for one char in target
        # branches is n, worst case can choose any sticker
        # each node is t*w time
        # O(n^t * tw)
		# memo
        # we can hit cache if target is seen before
        # worst case is one sticker removes one char only
        # worst case TC is number of subsequences from empty to target, worst case 2^n if all chars are unique
        # O(2^t) TC and SC
        
        def addSticker(sticker,w): # O(t*w)
            for c in sticker: # O(w)
                w = w.replace(c,'',sticker[c]) # replcae first sticker[c] counts, O(t)
            return w
        
        @lru_cache(None)
        def dfs(s): # returns min for this string
            if not s: # base case no stickers needed if target is empty
                return 0
            res = float('inf')
            for sticker in stickers: # O(n)
                if s[0] not in sticker: continue # add this sticker only if it contains char,O(1)
                w = addSticker(sticker,s) # O(t*w)
                res = min(res,1 + dfs(w)) # cost to use this sticker is 1
            return res
        
        stickers = [Counter(s) for s in stickers]
        res = dfs(target) 
        return res if res!=float('inf') else -1

a = Solution()
print(a.minStickers(["with","example","science"], 'thehat'))