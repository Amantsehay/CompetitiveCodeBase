class Solution:
    def minimumSteps(self, s: str) -> int:


        # for every one count the number of zeros to the right 

        cnt = 0
        n = len(s)
        ans = 0
        for right in range(n - 1, -1, -1):
            if s[right] == '1':
                ans += cnt
            if s[right] == '0':
                cnt += 1
        return ans


        