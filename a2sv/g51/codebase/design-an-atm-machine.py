class ATM:
    def __init__(self):
        self.arr = [0] * 5
        self.p = [20, 50, 100, 200, 500]

    def deposit(self, bank):
        for i in range(len(bank)):
            self.arr[i] += bank[i]

    def withdraw(self, amount):
        v = [0] * 5

        for i in range(4, -1, -1):
            if self.arr[i] > 0:
                x = amount // self.p[i]

                if self.arr[i] >= x:
                    amount -= x * self.p[i]
                    self.arr[i] -= x
                    v[i] = x
                else:
                    amount -= self.arr[i] * self.p[i]
                    v[i] = self.arr[i]
                    self.arr[i] = 0

        if amount == 0:
            return v

        for i in range(5):
            self.arr[i] += v[i]

        return [-1]
