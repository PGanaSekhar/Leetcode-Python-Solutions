class ProductOfNumbers:

    def __init__(self):
        self.r=[1]

    def add(self, num: int) -> None:
        if num==0:
            self.r=[1]
        else:
            self.r.append(self.r[-1]*num)

    def getProduct(self, k: int) -> int:
        if k>=len(self.r):
            return 0
        return self.r[-1]//self.r[-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
