class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(self.parseInt(num1) * self.parseInt(num2))

    def parseInt(self, w: str) -> int:
        ans = 0
        for i in range(len(w)):
            ans = ans * 10 + int(w[i])
        return ans