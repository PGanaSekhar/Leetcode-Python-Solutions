class Solution:
    def numTeams(self, rating: List[int]) -> int:
        r=[]
        def give(sol):
            a={}
            for i in range(len(sol)):
                a[sol[i]]=[j for j in sol[i+1:] if j>sol[i]]
            for i,j in a.items():
                if len(j)>0:
                    for k in a[i]:
                        if len(a[k])>0:
                            r.append(len(a[k]))
        give(rating)
        rating.reverse()
        give(rating)
        return sum(r)
