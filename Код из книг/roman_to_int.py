def romanToInt( s: str) -> int:

        # From Smallest Roman value to Biggest.
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # Smaller roman after Bigger: add it to the Bigger one i.e. VIII = 8
        # Smaller roman before Bigger: subtract it to the Bigger one i.e. IV = 5 - 1 = 4

        res = 0

        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:  # if there exist i+1 index and Smaller Roman is before Bigger
                res -= roman[s[i]]
            else:                                                 # if there exist only one index or Smaller Roman is after Bigger
                res += roman[s[i]]
        return res

print(romanToInt('MCMXCVIII'))