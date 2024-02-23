class MinStack:

    def __init__(self):
        self.stack = []
        self.minn = float('inf')

    def push(self, val: int) -> None:
        self.minn = min(self.minn, val)
        self.stack.append((val, self.minn))

    def pop(self) -> None:
        self.stack.pop()
        self.minn = self.stack[-1][1] if self.stack else float('inf')

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.minn
