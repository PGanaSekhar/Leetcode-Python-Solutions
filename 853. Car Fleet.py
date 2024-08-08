class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        a=[]
        b={i:j for i,j in zip(position,speed)}
        b=dict(sorted(b.items())[::-1])
        for i,j in b.items():
            a.append((target-i)/j)
            if len(a)>1 and a[-1]<=a[-2]:
                a.pop()
        return len(a)
