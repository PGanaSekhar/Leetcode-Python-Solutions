class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.a=nums
        self.b=k
        heapq.heapify(self.a)
        while len(self.a)>k:
            heapq.heappop(self.a)

    def add(self, val: int) -> int:
        heapq.heappush(self.a,val)
        if len(self.a)>self.b:
            heapq.heappop(self.a)
        return self.a[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
