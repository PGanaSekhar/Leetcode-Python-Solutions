class Solution:
    def romanToInt(self, s: str) -> int:
        rom_nums = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        
        ans = 0

        for n in range(len(s)):
            if n < len(s) - 1 and rom_nums[s[n]] < rom_nums[s[n+1]]:
                ans -= rom_nums[s[n]]
            else:
                ans += rom_nums[s[n]]
        
        return ans
