class RandomizedSet:
    def __init__(self):
        self.d = {}
        self.ls = []
        
    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        self.d[val] = len(self.ls)
        self.ls.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.d:
            return False
        i = self.d[val]
        self.d[self.ls[-1]] = i
        self.ls[i], self.ls[-1] = self.ls[-1], self.ls[i] 
        del self.d[val] 
        self.ls.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.ls)
