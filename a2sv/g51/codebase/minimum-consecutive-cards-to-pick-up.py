class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ind = {}
        n = len(cards)
        ans = n + 1
        for i in range(n):
            if cards[i] in ind:
                ans = min(ans,i + 1 - ind[cards[i]])
            ind[cards[i]] = i
        return ans if ans < n + 1 else -1




        