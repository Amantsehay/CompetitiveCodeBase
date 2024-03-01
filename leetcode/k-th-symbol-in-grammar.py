class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        curr = 0
        start, end = 1, 2 ** (n - 1)

        while start < end:
            mid = (start + end) // 2
            if k <= mid:
                end = mid 
            else:
                start = mid + 1
                curr = 0 if curr == 1 else 1
        return curr
