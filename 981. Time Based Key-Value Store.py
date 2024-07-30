class TimeMap:

    def __init__(self):
        self.a={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.a:
            self.a[key].append((value,timestamp))
        else:
            self.a[key]=[(value,timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.a:
            t=len(self.a[key])
            for i in range(t):
                if self.a[key][t-i-1][1]<=timestamp:
                    return self.a[key][t-i-1][0]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
