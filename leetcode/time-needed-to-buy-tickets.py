class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        kth = tickets[k]
        ans = 0
        for i in range(n):
            if i <= k:
                ans += min(kth, tickets[i])
            else:
                ans += min(kth -1, tickets[i])
        return ans
        