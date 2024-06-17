class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c==0:
            return True
        for i in range(ceil(sqrt(c))):
            if sqrt(c-i*i)==int(sqrt(c-i*i)):
                return True
        return False
