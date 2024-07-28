class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        a=[]
        r=[]
        def sol(o,c):
            if o<n:
                a.append("(")
                sol(o+1,c)
                a.pop()
            
            if o==n==c:
                r.append(''.join(a))
            
            if c<o:
                a.append(")")
                sol(o,c+1)
                a.pop()
        sol(0,0)
        return r
