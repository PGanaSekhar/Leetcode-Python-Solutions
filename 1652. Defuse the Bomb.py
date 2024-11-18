class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k==0:
            return [0]*len(code)
        t=code[:]
        t.extend(code)
        if k>0:
            for i in range(len(code)):
                code[i]=sum(t[i+1:i+k+1])
        else:
            for i in range(len(code)):
                code[i]=sum(t[len(code)+k+i:len(code)+i])
        return code
