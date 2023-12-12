class OrderedStream:
    def __init__(self, n: int):
        self.ls = [0] * (n + 1)  
        self.ptr = 1 
        self.n = n
    def insert(self, idKey: int, value: str) -> List[str]:
        self.ls[idKey] = value
        ans = []
        while self.ptr <= self.n and self.ls[self.ptr]:
            ans.append(self.ls[self.ptr])
            self.ptr += 1

        return ans


        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
