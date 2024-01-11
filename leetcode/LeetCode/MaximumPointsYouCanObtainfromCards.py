class Solution:
    def maxScore(self, cardPoints, k):
        n = len(cardPoints)
        ans = 0
        for i in range(n - k, n):
            ans += cardPoints[i]
        
        tot = ans
        for i in range(k):
            ans += cardPoints[i]
            ans -= cardPoints[n - k + i]
            tot = max(tot, ans)
        
        return tot