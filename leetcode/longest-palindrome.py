class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        oddMax = 0
        ans = 0
        for letter in count:
            if not count[letter] % 2:
                ans += count[letter]
            else:
                oddMax += 1
                ans += count[letter] - 1
        return ans + 1 if oddMax > 0 else ans 

