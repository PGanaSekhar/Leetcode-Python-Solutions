class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        a=Counter(v%k for v in arr)
        for i in a.keys():
            b=(k-i)%k
            if i==b:
                if a[b]%2!=0:
                    return False
            else:
                if a[i]!=a[b]:
                    return False
        return True
        # def per(a,k):
        #     for i in list(permutations(a,2)):
        #         if sum(i)%k==0:
        #             return list(i)
        #     return False

        # for i in range(len(arr)//2):
        #     a=per(arr,k)
        #     if a:
        #         for i in a:
        #             arr.remove(i)
        #     else:
        #         return False
        # if len(arr)==0:
        #     return True
        # return False
