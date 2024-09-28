class MyCircularDeque:

    def __init__(self, k: int):
        self.l=k
        self.li=[]

    def insertFront(self, value: int) -> bool:
        if len(self.li)==self.l:
            return False
        self.li.insert(0,value)
        return True

    def insertLast(self, value: int) -> bool:
        if len(self.li)==self.l:
            return False
        self.li.append(value)
        return True

    def deleteFront(self) -> bool:
        if self.li:
            self.li.pop(0)
            return True
        return False

    def deleteLast(self) -> bool:
        if self.li:
            self.li.pop(-1)
            return True
        return False

    def getFront(self) -> int:
        if not self.li:
            return -1
        return self.li[0]

    def getRear(self) -> int:
        if not self.li:
            return -1
        return self.li[-1]

    def isEmpty(self) -> bool:
        return not self.li

    def isFull(self) -> bool:
        if len(self.li)==self.l:
            return True
        return False 


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
