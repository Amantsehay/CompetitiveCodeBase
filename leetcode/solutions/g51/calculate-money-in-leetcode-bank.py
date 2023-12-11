class Solution:
    def totalMoney(self, n: int) -> int:
        return (1 + 2 + 3 + 4 + 5 + 6 + 7) * (n // 7) + sum([7 * i for i in range(n // 7)]) + sum([i+1 for i in range(n % 7)]) + (n % 7) * (n // 7) if n >= 7 else sum([i+1 for i in range(n % 7)])