class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        p = [(capital[i], profits[i]) for i in range(n)]
        p.sort()
        i = 0
        m = []
        while k > 0:
            while i < n and p[i][0] <= w:
                heapq.heappush(m, -p[i][1])
                i += 1
            if not m:
                break
            w -= heapq.heappop(m)
            k -= 1
        return w
