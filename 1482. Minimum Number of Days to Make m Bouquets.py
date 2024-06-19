class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if k*m>len(bloomDay):
            return -1
        def canMakeBouquets(days):
            bouquets = 0
            flowers = 0

            for day in bloomDay:
                if day <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
            
            return bouquets >= m
        left, right = 0, 10**9
        ans = -1

        while left <= right:
            mid = (left + right) // 2
            if canMakeBouquets(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
