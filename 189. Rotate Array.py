class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        a=nums[::-1]
        b=a[k:][::-1]
        a=a[:k][::-1]
        j=0
        for i in a:
            nums[j]=i
            j+=1
        for i in b:
            nums[j]=i
            j+=1
