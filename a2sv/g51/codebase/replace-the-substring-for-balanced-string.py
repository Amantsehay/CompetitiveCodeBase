class Solution:
    def balancedString(self, s: str) -> int:
        d = [0] * (128)
        n = len(s)
        for i in range(n):
            d[ord(s[i]) - ord('A')] += 1

        q = ord('Q') - ord('A')
        w = ord('W') - ord('A')
        e = ord('E') - ord('A')
        r = ord('R') - ord('A')
        ans = n 
        l = 0
        k = n//4
        for i in range(n):
            d[ord(s[i]) - ord('A')] -= 1
        
            while l < n and d[q] <= k and d[w] <= k and d[e] <= k and d[r] <= k:
                ans = min(ans, i - l + 1)
                d[ord(s[l]) - ord('A')]+= 1
                l += 1
        return ans
        