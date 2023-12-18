
class Bitset:
    def __init__(self, size):
        self.size = size
        self.ones = set()
        self.zeroes = set(range(size))

    def fix(self, idx):
        if idx not in self.ones:
            self.ones.add(idx)
            self.zeroes.remove(idx)

    def unfix(self, idx):
        if idx not in self.zeroes:
            self.ones.remove(idx)
            self.zeroes.add(idx)

    def flip(self):
        self.ones, self.zeroes = self.zeroes, self.ones

    def all(self):
        return len(self.ones) == self.size

    def one(self):
        return len(self.ones) >= 1

    def count(self):
        return len(self.ones)

    def toString(self):
        result = []
        for i in range(self.size):
            if i in self.ones:
                result.append("1")
            elif i in self.zeroes:
                result.append("0")
        return "".join(result)
        

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()