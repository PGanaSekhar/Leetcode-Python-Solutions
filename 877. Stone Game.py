class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        a=0
        b=0
        while piles:
            a+=max(piles[0],piles[-1])
            piles.remove(max(piles[0],piles[-1]))
            a+=max(piles[0],piles[-1])
            piles.remove(max(piles[0],piles[-1]))
        if a>b:
            return True
        return False
