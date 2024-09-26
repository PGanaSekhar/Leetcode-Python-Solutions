class MyCalendar:

    def __init__(self):
        self.s=[]

    def book(self, start: int, end: int) -> bool:
        for s,e in self.s:
            if not(e<=start or end<=s):
                return False
        self.s.append((start,end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
