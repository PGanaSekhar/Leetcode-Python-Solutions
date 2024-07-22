class MinStack:

    def __init__(self):
        self.a=[]

    def push(self, val: int) -> None:
        self.a.append(val)

    def pop(self) -> None:
        self.a.pop(-1)

    def top(self) -> int:
        return self.a[-1]

    def getMin(self) -> int:
        return min(self.a)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
